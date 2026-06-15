# 📚 Livraria DataBook — Dashboard de Vendas

Projeto de estudo desenvolvido para aprender na prática os fundamentos de **Python para análise de dados**, utilizando Pandas, Plotly e Dash para construir um dashboard interativo de vendas de uma livraria fictícia.

---

## 📊 Preview

![Dashboard DataBook](preview.gif)

---

## 🎯 Objetivo

Consolidar os seguintes aprendizados:

- Leitura e transformação de dados com **Pandas** (`read_csv`, `to_datetime`, `groupby`)
- Criação de colunas calculadas (receita, total com desconto)
- Construção de página web interativa com **Dash** sem escrever HTML manualmente
- Criação de gráficos interativos com **Plotly Express** (barras, linha, pizza)
- Uso de **Callbacks** para conectar filtros a múltiplos gráficos simultaneamente

---

## 📈 Funcionalidades do Dashboard

- **Filtro por Categoria** — dropdown para selecionar o gênero literário
- **Filtro por Faixa de Preço** — RangeSlider para definir o intervalo de preço
- **Gráfico de Barras** — livros vendidos por mês
- **Gráfico de Pizza (Donut)** — receita por canal de venda (Loja Física, E-commerce, App)
- **Gráfico de Linha** — evolução da receita mensal
- **Gráfico de Barras** — ranking de vendedores por quantidade vendida

Todos os gráficos atualizam automaticamente ao aplicar qualquer filtro.

---

## 🗂️ Estrutura do Projeto

```
livraria-databook/
├── databook.py                  # Aplicação principal (Dash + Plotly)
├── vendas_databook.csv     # Base de dados fictícia (300 registros)
├── requirements.txt        # Dependências do projeto
└── README.md
```

---

## 🗃️ Sobre os Dados

O arquivo `vendas_databook.csv` contém **300 registros fictícios** de vendas ao longo de 2024, com as seguintes colunas:

| Coluna | Descrição |
|---|---|
| `data` | Data da venda (AAAA-MM-DD) |
| `titulo` | Nome do livro |
| `categoria` | Gênero literário |
| `quantidade` | Exemplares vendidos |
| `preco_unitario` | Preço unitário em R$ |
| `desconto_pct` | Percentual de desconto aplicado |
| `vendedor` | Nome do vendedor responsável |
| `canal_venda` | Canal de venda (Loja Física, E-commerce, App Mobile) |

---

## 🚀 Como Rodar

**1. Clone o repositório**
```bash
git clone https://github.com/luiz1997martins-ship-it/livraria-databook.git
cd livraria-databook
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute a aplicação**
```bash
python databook.py
```

**4. Acesse no navegador**
```
http://127.0.0.1:8071
```

---

## 🛠️ Tecnologias Utilizadas

| Biblioteca | Versão | Uso |
|---|---|---|
| Python | 3.8+ | Linguagem base |
| Pandas | 2.x | Leitura e transformação dos dados |
| Plotly Express | 5.x | Criação dos gráficos interativos |
| Dash | 2.x | Framework da aplicação web |

---

## 📚 Conceitos Praticados

- `pd.read_csv()` com `parse_dates`
- `dt.to_period()`, `dt.strftime()` para manipulação de datas
- `groupby()` + `sum()` para agregações
- `dcc.Dropdown` e `dcc.RangeSlider` como componentes de filtro
- `@app.callback` com múltiplos `Input` e `Output`
- Layout responsivo com `display: flex` via `style` do Dash

---

## 👤 Autor

**Felipe Martins**  
IT Analyst | Transição para Data Analytics  
[LinkedIn](https://linkedin.com/in/felipemrs) · [GitHub](https://github.com/luiz1997martins-ship-it)
