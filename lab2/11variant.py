import numpy as np
import matplotlib.pyplot as plt


def f(x):
    # Кусочная функция f(x)
    return np.where(
        (x >= 0) & (x <= 1),
        x**2 * np.arctan(x),
        np.where(
            (x > 1) & (x <= 2),
            np.sin(1 / x**2),
            np.nan
        )
    )

def f_prime(x):
    # Производная f(x) в точке x
    if 0 <= x <= 1:
        return 2 * x * np.arctan(x) + x**2 / (1 + x**2)
    elif 1 < x <= 2:
        return np.cos(1 / x**2) * (-2 / x**3)
    else:
        return np.nan

x0 = 0.7
y0 = float(f(np.array([x0]))[0])
k  = f_prime(x0)


x1 = np.linspace(0,   1,   500)
x2 = np.linspace(1,   2,   500)
x_tan = np.linspace(0.2, 1.2, 300)
y_tan = y0 + k * (x_tan - x0)


fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0f0f1a')
ax.set_facecolor('#0f0f1a')


ax.plot(x1, f(x1), color='#00d4ff', linewidth=2.5,
        label=r'$f(x) = x^2 \arctan x,\quad x \in [0,\,1]$', zorder=3)
ax.plot(x2, f(x2), color='#ff6b9d', linewidth=2.5,
        label=r'$f(x) = \sin\dfrac{1}{x^2},\quad x \in (1,\,2]$', zorder=3)


ax.plot(x_tan, y_tan, color='#ffd166', linewidth=1.8, linestyle='--',
        label=f'Касательная в точке $x_0 = {x0}$', zorder=3)


ax.scatter([x0], [y0], color='#ffd166', s=100, zorder=5)


ax.annotate(
    f'Точка касания\n$x_0={x0}$,  $y_0={y0:.4f}$\n$k={k:.4f}$',
    xy=(x0, y0),
    xytext=(x0 + 0.3, y0 + 0.05),
    fontsize=9,
    color='#ffd166',
    arrowprops=dict(arrowstyle='->', color='#ffd166', lw=1.5),
    bbox=dict(boxstyle='round,pad=0.4',
              facecolor='#1a1a2e', edgecolor='#ffd166', alpha=0.9)
)


ax.set_title(r'График функции $f(x)$ и касательная',
             fontsize=14, color='white', pad=15, fontweight='bold')
ax.set_xlabel('x',    fontsize=12, color='#aaaacc')
ax.set_ylabel('f(x)', fontsize=12, color='#aaaacc')
ax.tick_params(colors='#aaaacc')
ax.grid(True, color='#ffffff15', linewidth=0.8)

for spine in ax.spines.values():
    spine.set_edgecolor('#333355')

ax.legend(facecolor='#1a1a2e', edgecolor='#333355',
          labelcolor='white', fontsize=9)

plt.tight_layout()

plt.show()