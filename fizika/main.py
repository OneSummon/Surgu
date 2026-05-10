import tkinter as tk
from tkinter import ttk, font as tkfont
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Цвета
BG       = "#0d1117"
PANEL    = "#161b22"
BORDER   = "#30363d"
TEXT     = "#cdd5e0" 
MUTED    = "#8b949e"
ACCENT   = "#1f6feb"
ACCENT_H = "#388bfd"
ENTRY_BG = "#21262d"
GREEN    = "#3fb950"
YELLOW   = "#e3b341"
RED      = "#f85149"
PURPLE   = "#a371f7"
CYAN     = "#39d3f0"

GRAPH_COLORS = ["#4FC3F7", "#81C784", "#FFB74D", "#CE93D8", "#EF9A9A"]

# ─────────────────────────────────────────────────────────────────────────────
# Физика
# ─────────────────────────────────────────────────────────────────────────────
def simulate(mass, x0, y0, vx0, vy0, fx, fy, t_end, dt=0.01):
    t  = np.arange(0, t_end + dt, dt)
    ax = fx / mass
    ay = fy / mass - 9.81

    x  = x0  + vx0 * t + 0.5 * ax * t**2
    y  = y0  + vy0 * t + 0.5 * ay * t**2
    vx = vx0 + ax * t
    vy = vy0 + ay * t
    v  = np.sqrt(vx**2 + vy**2)

    KE = 0.5 * mass * v**2
    PE = mass * 9.81 * y

    # Обрезаем при касании земли
    ground = np.where(y < 0)[0]
    if len(ground) > 0 and ground[0] > 0:
        s = ground[0]
        t, x, y, vx, vy, v, KE, PE = (
            t[:s], x[:s], y[:s],
            vx[:s], vy[:s], v[:s],
            KE[:s], PE[:s],
        )

    return t, x, y, vx, vy, v, KE, PE

# ─────────────────────────────────────────────────────────────────────────────
# Графики
# ─────────────────────────────────────────────────────────────────────────────
def draw_graphs(axes, t, x, y, v, KE, PE, fx, fy):
    titles = [
        "X(t)  перемещение по горизонтали",
        "Y(t)  высота",
        "V(t)  полная скорость",
        "Траектория  Y(X)",
        "Кинетич. / Потенц. энергия",
    ]
    data = [
        (t, x,  "t, с", "x, м"),
        (t, y,  "t, с", "y, м"),
        (t, v,  "t, с", "|v|, м/с"),
        (x, y,  "x, м", "y, м"),
        (t, KE, "t, с", "Дж"),
    ]

    for i, ax in enumerate(axes):
        ax.cla()
        ax.set_facecolor(BG)
        ax.tick_params(colors=TEXT, labelsize=8)
        for spine in ax.spines.values():
            spine.set_edgecolor(BORDER)

        dx, dy, xl, yl = data[i]
        ax.plot(dx, dy, color=GRAPH_COLORS[i], lw=1.8)

        if i == 4:
            ax.plot(t, PE, color=CYAN, lw=1.8, linestyle="--")
            ax.legend(
                handles=[
                    mpatches.Patch(color=GRAPH_COLORS[4], label="Кинетич."),
                    mpatches.Patch(color=CYAN,            label="Потенц."),
                ],
                facecolor=PANEL, edgecolor=BORDER,
                labelcolor=TEXT, fontsize=7, loc="upper right",
            )

        ax.set_title(titles[i], color=TEXT, fontsize=8.5, pad=4)
        ax.set_xlabel(xl, color=MUTED, fontsize=8)
        ax.set_ylabel(yl, color=MUTED, fontsize=8)
        ax.grid(color=BORDER, linewidth=0.6)

    # Стрелка силы на траектории
    if len(x) > 4:
        mid   = len(x) // 4
        f_mag = np.sqrt(fx**2 + fy**2) + 1e-9
        fx_n  = fx / f_mag
        fy_n  = fy / f_mag
        sc    = 0.1 * max(np.ptp(x) or 1, np.ptp(y) or 1)
        axes[3].annotate(
            "", xy=(x[mid] + fx_n*sc, y[mid] + fy_n*sc),
            xytext=(x[mid], y[mid]),
            arrowprops=dict(arrowstyle="->", color="#FF7043", lw=2),
        )

# ─────────────────────────────────────────────────────────────────────────────
# Главное окно
# ─────────────────────────────────────────────────────────────────────────────
def main():
    root = tk.Tk()
    root.title("Законы Ньютона - F = ma")
    root.configure(bg=BG)
    root.state("zoomed")

    # ── Шрифты ────────────────────────────────────────────────────────────────
    fnt_label  = ("Segoe UI", 8)
    fnt_entry  = ("Segoe UI", 10)
    fnt_btn    = ("Segoe UI", 10, "bold")
    fnt_title  = ("Segoe UI", 13, "bold")
    fnt_res_h  = ("Segoe UI", 8,  "bold")
    fnt_res_v  = ("Segoe UI", 11, "bold")
    fnt_res_u  = ("Segoe UI", 7)

    # ── Заголовок ─────────────────────────────────────────────────────────────
    tk.Label(root, text="Законы Ньютона - F = ma",
             bg=BG, fg=TEXT, font=fnt_title).pack(pady=(8, 0))

    # ──────────────────────────────────────────────────────────────────────────
    # ВЕРХНЯЯ ПАНЕЛЬ: поля ввода + кнопка
    # ──────────────────────────────────────────────────────────────────────────
    top = tk.Frame(root, bg=PANEL, bd=0)
    top.pack(fill="x", padx=10, pady=6)

    # Описания полей: (ключ, строка 1, строка 2, единица)
    fields_cfg = [
        ("mass", "m", "Масса", "кг"),
        ("x0", "x₀", "нач. позиция", "м"),
        ("y0", "y₀", "нач. высота", "м"),
        ("vx0", "vx₀", "нач. скорость по X", "м/с"),
        ("vy0", "vy₀", "нач. скорость по Y", "м/с"),
        ("fx", "Fx", "сила по оси X", "Н"),
        ("fy", "Fy", "сила по оси Y", "Н"),
        ("t_end","t", "время симуляции", "с"),
    ]

    entries = {}
    defaults = {
        "mass": "1.0", "x0": "0.0", "y0": "10.0",
        "vx0":  "0.0", "vy0": "0.0",
        "fx":   "0.0", "fy": "0.0", "t_end": "10.0",
    }

    for col, (key, line1, line2, unit) in enumerate(fields_cfg):
        cell = tk.Frame(top, bg=PANEL)
        cell.grid(row=0, column=col, padx=8, pady=6, sticky="nsew")
        top.columnconfigure(col, weight=1)

        # Подпись сверху (две строки + единица)
        lbl_text = line1
        if line2:
            lbl_text += f"\n{line2}"
        lbl_text += f" ({unit})"
        tk.Label(cell, text=lbl_text, bg=PANEL, fg=MUTED,
                 font=fnt_label, justify="center").pack()

        # Поле ввода
        e = tk.Entry(cell, font=fnt_entry, bg=ENTRY_BG, fg=TEXT,
                     insertbackground=TEXT, relief="flat",
                     justify="center", width=9,
                     highlightthickness=1, highlightcolor=ACCENT,
                     highlightbackground=BORDER)
        e.insert(0, defaults[key])
        e.pack(ipady=4, fill="x")
        entries[key] = e

    # ── Кнопка ────────────────────────────────────────────────────────────────
    btn_cell = tk.Frame(top, bg=PANEL)
    btn_cell.grid(row=0, column=len(fields_cfg), padx=(12, 8), pady=6)
    top.columnconfigure(len(fields_cfg), weight=0)

    btn = tk.Button(
        btn_cell, text="▶  Рассчитать",
        font=fnt_btn, bg=ACCENT, fg="white",
        activebackground=ACCENT_H, activeforeground="white",
        relief="flat", padx=14, pady=8, cursor="hand2",
        command=lambda: on_calculate(),
    )
    btn.pack(expand=True)

    # ──────────────────────────────────────────────────────────────────────────
    # СРЕДНЯЯ ПАНЕЛЬ: результаты
    # ──────────────────────────────────────────────────────────────────────────
    res_frame = tk.Frame(root, bg=PANEL, bd=0)
    res_frame.pack(fill="x", padx=10, pady=(0, 6))

    # Заголовок панели результатов
    tk.Label(res_frame, text="  Результаты расчёта",
             bg=PANEL, fg=MUTED, font=("Segoe UI", 8)).pack(anchor="w", pady=(4, 0))

    # Сетка результатов: каждая ячейка - название + значение + единица
    res_grid = tk.Frame(res_frame, bg=PANEL)
    res_grid.pack(fill="x", padx=6, pady=(2, 6))

    result_keys = [
        ("|F| внешн.", "Н", "Внешняя сила (без g)"),
        ("|F| полная", "Н", "Полная сила (с g)"),
        ("|a| полное", "м/с²", "Полное ускорение тела"),
        ("ax", "м/с²", "Ускорение по X"),
        ("ay", "м/с²", "Ускорение по Y с g"),
        ("t полёта", "с", "Время до земли"),
        ("x приземл.", "м", "Дальность полёта"),
        ("y max", "м", "Макс. высота"),
        ("v max", "м/с", "Макс. скорость"),
        ("v приземл.", "м/с", "Скорость при падении"),
        ("KE max", "Дж", "Макс. кин. энергия"),
        ("PE пик", "Дж", "Пиковая пот. энергия"),
    ]

    # Цвета значений
    val_colors = [
        YELLOW, YELLOW, CYAN, CYAN,
        GREEN,  GREEN,  GREEN, YELLOW,
        RED,    PURPLE, PURPLE, ACCENT,
    ]

    res_labels = {}
    COLS = 6 

    for i, ((name, unit, tip), color) in enumerate(zip(result_keys, val_colors)):
        row, col = divmod(i, COLS)

        cell = tk.Frame(res_grid, bg=BORDER, bd=0)
        cell.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
        res_grid.columnconfigure(col, weight=1)

        inner = tk.Frame(cell, bg=PANEL)
        inner.pack(fill="both", expand=True, padx=1, pady=1)

        # Название параметра
        tk.Label(inner, text=name, bg=PANEL, fg=MUTED,
                 font=fnt_res_h).pack(pady=(4, 0))

        # Значение
        val_lbl = tk.Label(inner, text="-", bg=PANEL, fg=color,
                           font=fnt_res_v)
        val_lbl.pack()

        # Единица измерения
        tk.Label(inner, text=unit, bg=PANEL, fg=TEXT,
                 font=fnt_res_u).pack(pady=(0, 4))

        res_labels[name] = val_lbl

    # ──────────────────────────────────────────────────────────────────────────
    # НИЖНЯЯ ЧАСТЬ: matplotlib графики
    # ──────────────────────────────────────────────────────────────────────────
    fig = plt.Figure(figsize=(15, 5.2), facecolor=BG)
    fig.subplots_adjust(hspace=0.45, wspace=0.35,
                        left=0.05, right=0.97, top=0.93, bottom=0.1)

    axes = [
        fig.add_subplot(2, 3, 1),
        fig.add_subplot(2, 3, 2),
        fig.add_subplot(2, 3, 3),
        fig.add_subplot(2, 3, 4),
        fig.add_subplot(2, 3, 5),
    ]

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=(0, 8))

    # ── Обработчик кнопки ─────────────────────────────────────────────────────
    def on_calculate():
        vals = {}
        for key, e in entries.items():
            try:
                vals[key] = float(e.get())
            except ValueError:
                vals[key] = 0.0

        mass  = max(vals["mass"], 0.001)
        t_end = max(vals["t_end"], 0.1)

        t, x, y, vx, vy, v, KE, PE = simulate(
            mass,
            vals["x0"], vals["y0"],
            vals["vx0"], vals["vy0"],
            vals["fx"],  vals["fy"],
            t_end,
        )

        # Рисуем графики
        draw_graphs(axes, t, x, y, v, KE, PE, vals["fx"], vals["fy"])
        canvas.draw()

        # ── Физически корректные результаты ──────────────────────────────────
        fx_v = vals["fx"]
        fy_v = vals["fy"]

        # Ускорения по осям (второй закон Ньютона + гравитация по Y)
        ax_val = fx_v / mass
        ay_val = fy_v / mass - 9.81

        # Полное ускорение тела с учётом гравитации
        a_full = np.sqrt(ax_val**2 + ay_val**2)

        # Внешняя приложенная сила (без гравитации)
        F_ext   = np.sqrt(fx_v**2 + fy_v**2)

        # Полная сила на тело включает силу тяжести m*g вниз
        F_grav  = mass * 9.81
        F_total = np.sqrt(fx_v**2 + (fy_v - F_grav)**2)

        # Энергии
        E_start = KE[0]  + PE[0]   # полная энергия в начале
        E_end   = KE[-1] + PE[-1]  # полная энергия в конце

        # PE_max: берём максимум по модулю с учётом знака
        PE_peak = PE[np.argmax(np.abs(PE))]

        results = {
            "|F| внешн.":  F_ext,     # модуль только внешней силы
            "|F| полная":  F_total,   # полная сила включая гравитацию
            "|a| полное":  a_full,    # полное ускорение тела
            "ax":          ax_val,    # ускорение по X
            "ay":          ay_val,    # ускорение по Y с учётом g
            "t полёта":    t[-1],     # время до приземления
            "x приземл.":  x[-1],     # горизонтальная дальность
            "y max":       y.max(),   # максимальная высота
            "v max":       v.max(),   # максимальная скорость
            "v приземл.":  v[-1],     # скорость в момент касания
            "KE max":      KE.max(),  # максимальная кинетическая энергия
            "PE пик":      PE_peak,   # пиковая потенциальная энергия
        }

        for name, val in results.items():
            res_labels[name].config(text=f"{val:.2f}")

    # Первый расчёт при запуске
    on_calculate()

    root.mainloop()

if __name__ == "__main__":
    main()
