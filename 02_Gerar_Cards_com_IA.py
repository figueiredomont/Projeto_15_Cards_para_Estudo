import streamlit as st
from gerador import Gerador
import json
from random import choice


# ============================================================
# CONFIGURAÇÕES INICIAIS
# ============================================================

st.set_page_config(
    page_title="Gerador de Cards",
    page_icon="🧠"
)
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


gerador = Gerador("openai/gpt-oss-120b")

# ============================================================
# INTERFACE
# ============================================================

st.markdown("""
# ✨ Gerar Cards com IA

Digite um tema e a IA cria cards de perguntas e respostas para você estudar.

**Exemplos de temas:**
- Revolução Francesa
- Fundamentos de Python
- Anatomia do coração
- Verbos irregulares em inglês

> 💡 **Dica:** quanto mais específico o tema, melhores os cards. Em vez de "História", tente "Causas da Primeira Guerra Mundial".

> ℹ️ Os cards são gerados por IA. Vale conferir as respostas, principalmente em assuntos importantes.
""")

tema = st.text_input("Digite o tema escolhido")


# ============================================================
# GERAR CARDS
# ============================================================

if st.button("Gerar cards") and tema:

    try:

        resultado = gerador.gerar_perguntas(tema)

        st.session_state["dados"] = resultado


    except Exception as e:
        st.session_state["dados"] = None
        st.warning(f'Erro: {e}')


# ============================================================
# EXIBIR Perguntas
# ============================================================

try:
    if st.session_state["dados"]:
        st.markdown("""
        ## ✅ Seus cards estão prontos!

        Confira as perguntas e respostas abaixo antes de estudar. Como foram geradas por IA, vale verificar se estão corretas.

        Quando estiver satisfeito, baixe o arquivo e carregue-o na página **📚 Cards** para começar a estudar.
        """)
        # st.write(st.session_state["dados"])
        for i,kv in enumerate(st.session_state["dados"].items()):
            st.markdown(f"# Pergunta {i+1}")
            st.markdown(f"### {kv[0]}")
            st.markdown(f'- Resposta: {kv[1]}')
            st.markdown('---')


        # ========================================================
        # DOWNLOAD
        # ========================================================

        with st.popover("Salvar Arquivo"):

            nome_arquivo = st.text_input(
                "Nome do Arquivo"
            ).replace(' ', '_')
            st.write(f'{nome_arquivo}.json')
            st.download_button(
                label="Download",

                data=json.dumps(
                    st.session_state["dados"],
                    indent=4,
                    ensure_ascii=False
                ),

                file_name=f"{nome_arquivo}.json",

                mime="application/json",

                icon=":material/download:",

                width=600
            )
except:
    pass