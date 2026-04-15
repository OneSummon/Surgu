import numpy as np
import plotly.graph_objects as go


def f(x):
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
    if 0 <= x <= 1:
        return 2 * x * np.arctan(x) + x**2 / (1 + x**2)
    elif 1 < x <= 2:
        return np.cos(1 / x**2) * (-2 / x**3)
    else:
        return np.nan

x0 = 0.7
y0 = float(f(np.array([x0]))[0])
k  = f_prime(x0)

x1 = np.linspace(0, 1, 500)
x2 = np.linspace(1, 2, 500)
x_tan = np.linspace(0.2, 1.2, 300)
y_tan = y0 + k * (x_tan - x0)

fig = go.Figure()


fig.add_trace(go.Scatter(
    x=x1, y=f(x1),
    mode='lines',
    name=r'f(x) = x² arctan(x), x ∈ [0, 1]',
    line=dict(color='#00d4ff', width=2.5),
    hovertemplate='x = %{x:.3f}<br>f(x) = %{y:.4f}<extra>Ветвь 1</extra>'
))


fig.add_trace(go.Scatter(
    x=x2, y=f(x2),
    mode='lines',
    name='f(x) = sin(1/x²), x ∈ (1, 2]',
    line=dict(color='#ff6b9d', width=2.5),
    hovertemplate='x = %{x:.3f}<br>f(x) = %{y:.4f}<extra>Ветвь 2</extra>'
))

# Касательная
fig.add_trace(go.Scatter(
    x=x_tan, y=y_tan,
    mode='lines',
    name=f'Касательная в x₀ = {x0}',
    line=dict(color='#ffd166', width=1.8, dash='dash'),
    hovertemplate='x = %{x:.3f}<br>y = %{y:.4f}<extra>Касательная</extra>'
))

# Точка касания
fig.add_trace(go.Scatter(
    x=[x0], y=[y0],
    mode='markers',
    name=f'Точка касания (x₀={x0})',
    marker=dict(color='#ffd166', size=12, symbol='circle',
                line=dict(color='white', width=2)),
    hovertemplate=f'x₀ = {x0}<br>y₀ = {y0:.4f}<br>k = {k:.4f}<extra>Точка касания</extra>'
))


fig.add_annotation(
    x=x0, y=y0,
    ax=x0 + 0.28, ay=y0 + 0.06,
    axref='x', ayref='y',
    text=f'Точка касания<br>x₀ = {x0},  y₀ = {y0:.4f}<br>k = {k:.4f}',
    showarrow=True,
    arrowhead=2,
    arrowcolor='#ffd166',
    arrowwidth=1.5,
    font=dict(color='#ffd166', size=11),
    bgcolor='#1a1a2e',
    bordercolor='#ffd166',
    borderwidth=1.5,
    borderpad=6
)

fig.update_layout(
    title=dict(
        text='График функции f(x) и касательная',
        font=dict(size=16, color='white'),
        x=0.5
    ),
    xaxis=dict(
        title='x',
        color='#aaaacc',
        gridcolor='rgba(255,255,255,0.12)',
        zerolinecolor='rgba(255,255,255,0.18)',
        tickfont=dict(color='#aaaacc')
    ),
    yaxis=dict(
        title='f(x)',
        color='#aaaacc',
        gridcolor='rgba(255,255,255,0.12)',
        zerolinecolor='rgba(255,255,255,0.18)',
        tickfont=dict(color='#aaaacc')
    ),
    plot_bgcolor='#0f0f1a',
    paper_bgcolor='#0f0f1a',
    legend=dict(
        bgcolor='#1a1a2e',
        bordercolor='#333355',
        borderwidth=1,
        font=dict(color='white', size=11)
    ),
    hovermode='x unified',
    width=900,
    height=560
)

fig.write_html('/media/scroll/BCACABD8ACAB5C09/Surgu/lab2/plotly.html',
               include_plotlyjs='cdn',
               full_html=True)

print("Saved.")