import pandas as pd 
import streamlit as st 
from datetime import datetime

from utils.credits import display_credits
from scripts.etl import etl

st.set_page_config(
    page_title="Comércio Exterior de Alagoas",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("📦 Comércio Exterior de Alagoas")

current_year = datetime.now().year

col1, col2 = st.columns(2)
with col1:
    start_year = st.selectbox("Ano inicial", list(range(1997, current_year + 1)), index=18)
with col2:
    end_year = st.selectbox("Ano final", list(range(1997, current_year + 1)), index=current_year - 1997)

@st.cache_data
def carregamento(ano_inicio, ano_fim):
    with st.spinner("🔄 Processando os dados..."):
        return etl(ano_inicio, ano_fim)

df = pd.DataFrame()  

if "pesquisa_realizada" not in st.session_state:
    st.session_state.pesquisa_realizada = False

if st.button("Pesquisar", use_container_width=True, type="primary"):
    st.session_state.pesquisa_realizada = True
    st.session_state.df = carregamento(start_year, end_year)

if st.session_state.pesquisa_realizada:
    df = st.session_state.df
else:
    pass

if not df.empty:
    items_per_page = 100  
    total_pages = (len(df) + items_per_page - 1) // items_per_page  
    page = st.number_input("Página", min_value=1, max_value=total_pages, value=1, step=1)

    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    paginated_df = df.iloc[start_idx:end_idx]

    st.dataframe(paginated_df)
    st.write(f"Exibindo página {page} de {total_pages}")

display_credits()