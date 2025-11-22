
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("h2a_imobiliaria_dados_limpos.csv")

# Título
st.title("📊 Dashboard - H2A Imobiliária")

# Filtro por imóvel
imoveis = df.iloc[:, 0].dropna().unique()
imovel_selecionado = st.sidebar.selectbox("Selecionar Imóvel", options=["Todos"] + list(imoveis))

# Aplicar filtro
if imovel_selecionado != "Todos":
    df = df[df[df.columns[0]] == imovel_selecionado]

# Indicadores principais
st.subheader("📌 Indicadores Gerais")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Receita Total (R$)", f"{df['VALOR ALUGUEL'].sum():,.2f}")
with col2:
    st.metric("Média de Aluguel (R$)", f"{df['VALOR ALUGUEL'].mean():,.2f}")
with col3:
    st.metric("ROI Médio (%)", f"{df['ROI (%)'].mean():.2f}")

# Gráfico de barras - Aluguel por Imóvel
st.subheader("💰 Valor do Aluguel por Imóvel")
fig_aluguel = px.bar(df, x=df.columns[0], y="VALOR ALUGUEL", text="VALOR ALUGUEL",
                     labels={df.columns[0]: "Imóvel"}, height=400)
st.plotly_chart(fig_aluguel, use_container_width=True)

# Gráfico de barras - ROI por Imóvel
st.subheader("📈 ROI (%) por Imóvel")
fig_roi = px.bar(df, x=df.columns[0], y="ROI (%)", text="ROI (%)",
                 labels={df.columns[0]: "Imóvel"}, height=400)
st.plotly_chart(fig_roi, use_container_width=True)

# Tabela com dados
st.subheader("🧾 Dados Detalhados")
st.dataframe(df)
