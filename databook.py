import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Arquivo importado
df = pd.read_csv('vendas_databook.csv')

# Convertendo coluna em data
df['data'] = pd.to_datetime(df['data']) # convertendo para o formato de data
df['mes'] = df['data'].dt.month # número do mês
df['ano'] = df['data'].dt.year # ano
df['mes_ano'] = df['data'].dt.to_period('M').astype(str) # AAAA-MM
df['nome_mes'] = df['data'].dt.strftime('%B/%Y') # Janeiro/ 2024

# Criando colunas calculadas
df['receita'] = df['quantidade'] * df['preco_unitario']
df['total'] = (df['quantidade'] * df['preco_unitario']) *(1- df['desconto_pct'] / 100)

# Filtros
categorias = [{'label': c, 'value': c} for c in sorted(df['categoria'].unique())]

# Inicio da página
app = Dash(__name__)

app.layout = html.Div([
    # Título
    html.H1('Livraria DataBook',
            style={'textAlign': 'center', 'color': "#556F96",
                   'fontFamily': 'Arial', 'paddingTop': '20px'}),

    # Filtros
    html.Div([
        html.Div([
            html.Label('Filtrar por categoria:'),
            dcc.Dropdown(
                id='filtro-categoria',
                options=[{'label': c, 'value': c} for c in df['categoria'].unique()],
                value=None,
                placeholder='Todas as categorias',
                clearable=True,
            ),
        ], style={'width': '25%', 'margin': '20px 10px'}),

        html.Div([
            html.Label('Faixa de preço (R$):'),
            dcc.RangeSlider(
                id='filtro-preco',
                min=df['preco_unitario'].min(),   # mínimo real dos dados
                max=df['preco_unitario'].max(),   # máximo real dos dados
                step=5,                           # passo de R$ 5,00
                value=[                           # valor inicial = range completo
                    df['preco_unitario'].min(),
                    df['preco_unitario'].max()
                ],
                marks=None,
                tooltip={'placement': 'bottom', 'always_visible': True}
            ),
        ], style={'width': '30%', 'margin': '20px 10px'}),

    ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center', 'margin': '20px 30px'}),

    # Gráficos
    html.Div([
        html.Div([dcc.Graph(id='fig_barras')],
            style={'width': '60%'}),
        html.Div([dcc.Graph(id='fig_pizza')],
            style={'width': '40%'}),
    ], style={'display': 'flex'}),

    dcc.Graph(id='fig_linha'),

    dcc.Graph(id='fig_vend')

], style={'fontFamily': 'Arial', 'maxWidth': '1200px', 'margin': 'auto'})
# Final da página

# Callback
@app.callback(
    Output('fig_barras', 'figure'),
    Output('fig_pizza', 'figure'),
    Output('fig_linha', 'figure'),
    Output('fig_vend', 'figure'),
    Input('filtro-categoria', 'value'),
    Input('filtro-preco', 'value')
)

def atualizar_dash(categoria, faixa_preco):
    df_f = df.copy()

    if categoria:
        df_f = df_f[df_f['categoria'] == categoria]

    df_f = df_f[
        (df_f['preco_unitario'] >= faixa_preco[0]) &
        (df_f['preco_unitario'] <= faixa_preco[1])
    ]
    
    titulo_sufixo = f'- {categoria or "Todas"}'

    # Gráfico de barra
    # Vendas por Mês
    vendas_mes = df_f.groupby('mes_ano')['quantidade'].sum().reset_index()
    fig_barras = px.bar(
        vendas_mes,
        x='mes_ano',
        y='quantidade',
        title=f'Livros Vendidos por Mês {titulo_sufixo}',
        labels={'mes_ano': 'Mês',    # labels renomeia os eixos
                'quantidade': 'Qtd. Vendida'},
        color='quantidade',
        color_continuous_scale='Blues',
        text='quantidade' # mostrar o valor em cima de cada barra
    )

    fig_barras.update_traces(
        textposition='inside'
    )

    fig_barras.update_layout(
        plot_bgcolor='white'
    )

    # Gráfico de pizza
    # Receita por canal vendas
    receita_cat = df_f.groupby('canal_venda')['receita'].sum().reset_index()
    receita_cat['receita'] = receita_cat['receita'].round(2)
    fig_pizza = px.pie(
        receita_cat,
        names='canal_venda',
        values='receita',
        title='Receita por Canal de Vendas',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    # Gráfico de linha
    # Receita por Mês
    receita_mes = df_f.groupby('mes_ano')['receita'].sum().reset_index()
    receita_mes['receita'] = receita_mes['receita'].round(2)
    fig_linha = px.line(
        receita_mes,
        x='mes_ano',
        y='receita',
        title=f'Receita mensal {titulo_sufixo}',
        markers=True, # bolinha nos pontos de dados
        labels={'mes_ano': 'Mês', 'receita': 'Receita (R$)'},
        line_shape='spline', # curva entre os pontos
        text='receita'
    )

    fig_linha.update_traces(
        textposition='top center',
        line_color='#2E75B6',
        line_width=2.5
    )

    fig_linha.update_layout(
        plot_bgcolor='white',
        yaxis=dict(showgrid=True, gridcolor='lightgrey')
    )


    m_vendedor = df_f.groupby('vendedor')['quantidade'].sum().reset_index()
    fig_vend = px.bar(
        m_vendedor,
        x='vendedor',
        y='quantidade',
        color='quantidade',
        title=f'Top Vendedores {titulo_sufixo}',
        labels={'vendedor': 'Vendedor', 'quantidade': 'Livros Vendidos'},
        color_continuous_scale='Purples',
        text='quantidade'
    )

    fig_vend.update_traces(
        textposition='inside'
    )
    
    fig_vend.update_layout(
        plot_bgcolor='white'
    )

    return fig_barras, fig_pizza, fig_linha, fig_vend


if __name__ == '__main__':
    app.run(debug=True, port=8071)


