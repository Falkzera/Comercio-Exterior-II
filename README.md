# 📦 Comercio-Exterior-II

Está é a segunda versão do projeto! Caso não tenha visto a primeira, acesse a [primeira versão](https://github.com/Falkzera/Comercio-Exterior-I)

A principal diferença da primeira versão para está, é na maneira como os dados são coletados. Na primeira versão foi utilizado o download direto dos arquivos CSV públicos disponibilizados pelo ComexStat. Agora, no Projeto 2, a coleta foi totalmente reformulada utilizando API oficial do ComexStat.

## Buscador completo

Um buscador de bases de dados do comércio exterior, desenvolvido em Python com interface via [Streamlit](https://streamlit.io/). Com ele, o usuário pode visualizar e filtrar dados por ano.

## 🌐 Acesse Agora

Você pode acessar o app diretamente pelo navegador, sem precisar instalar nada:

👉 [https://comercio-exterior-2.streamlit.app/](https://comercio-exterior-2.streamlit.app/)

## 🚀 Funcionalidades

- 🔎 Filtragem de dados por ano
- 🔁 Atualização automática dos dados do ano corrente
- 📊 Visualização tabular interativa dos dados com paginação
- 💾 Download completo dos dados em formato `.parquet`
- 📦 Dados disponíveis nos modos:
  - `EXP`: Exportações brasileiras
  - `IMP`: Importações brasileiras

## 🛠 Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- PyArrow
- Requests
- Logging (built-in)

## ⚙️ Instalação Local

Caso queira rodar o projeto localmente:

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Comercio-Exterior-II.git
cd Comercio-Exterior-II
```
2. Crie um ambiente virtual e ative:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Rode o projeto
```bash
streamlit run app.py
```

## ✍️ Créditos

Desenvolvido por: [Lucas Falcão](https://falkzera.streamlit.app/)