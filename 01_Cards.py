import streamlit as st
import json
from random import choice


st.markdown("""
# 📚 Meus Cards

Carregue um arquivo de cards que você já tem e comece a estudar.

**Formato aceito:** arquivo `.json`

> 💡 Ainda não tem um arquivo? Crie seus cards em **✨ Gerar Cards com IA** ou **📄 Gerar Cards com Arquivo**. Os cards gerados podem ser salvos e carregados aqui depois.

""")


arquivo = st.file_uploader("Carregue seu arquivo", type=".json")

st.markdown("""
<style>
    /* Fonte moderna estilo tech/sci-fi */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');

    /* Fundo geral da aplicação */
    .stApp {
        background-color: #0b0f0e;
        color: #d1dcd6;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Estilização da Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0e1613;
        border-right: 1px solid #1c2b24;
    }

    [data-testid="stSidebar"] h1 {
        font-family: 'Orbitron', sans-serif;
        color: #4ade80;
        letter-spacing: 1px;
    }

    /* Títulos principais */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #e2e8f0;
    }
    
    h1 {
        background: linear-gradient(90deg, #4ade80, #2dd4bf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 25px rgba(74, 222, 128, 0.15);
    }

    /* Textos secundários e containers */
    div.stMarkdownContainer, .element-container {
        color: #cbd5e1;
    }

    /* Botões personalizados */
    .stButton>button {
        background: linear-gradient(135deg, #14532d 0%, #064e3b 100%);
        color: #86efac;
        border: 1px solid #15803d;
        border-radius: 10px;
        font-family: 'Orbitron', sans-serif;
        font-weight: 600;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 12px rgba(20, 83, 45, 0.3);
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #166534 0%, #047857 100%);
        color: #ffffff;
        border-color: #4ade80;
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.25);
        transform: translateY(-2px);
    }

    /* Blockquotes estilo painel de controle */
    blockquote {
        background: rgba(14, 22, 19, 0.7);
        border-left: 4px solid #22c55e !important;
        padding: 1.2rem;
        border-radius: 0 12px 12px 0;
        backdrop-filter: blur(10px);
        margin: 20px 0;
    }

    /* Linhas divisórias */
    hr {
        border-color: #1c2b24;
    }
</style>
""", unsafe_allow_html=True)



# =========================
# CARREGAR ARQUIVO
# =========================

if arquivo is not None and st.button("Carregar"):

    cards = json.load(arquivo)

    st.session_state["dados"] = cards
    st.session_state["carregado"] = True

    # Escolhe a primeira pergunta
    st.session_state["pergunta"] = choice(list(cards.keys()))


# =========================
# EXIBIR CARD
# =========================

if st.session_state.get("carregado", False):

    dados = st.session_state["dados"]
    pergunta = st.session_state["pergunta"]
    resposta = dados[pergunta]

    st.success("Arquivo carregado")

    with open("style.txt", "r", encoding="utf-8") as f:
        estilo = f.read()

    st.markdown(estilo, unsafe_allow_html=True)

    st.html(f"""
    <div class="card">
        <div class="upper-part">
            <div class="upper-part-face">{pergunta}</div>
            <div class="upper-part-back">
                {resposta}
            </div>
        </div>

        <div class="lower-part">
            <div class="lower-part-face">Pergunta</div>
            <div class="lower-part-back">Resposta</div>
        </div>
    </div>
    """)

    if st.button('Outra Pergunta'):
        st.session_state["pergunta"] = choice(list(st.session_state["dados"].keys()))
        st.rerun()
