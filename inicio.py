import streamlit as st

# ============================================================
# CONFIGURAÇÕES INICIAIS
# ============================================================

st.set_page_config(
    page_title="Study Cards | Future AI",
    page_icon="🧠",
    layout="wide"
)

# ============================================================
# DESIGN FUTURISTA EM TONS DE VERDE (CUSTOM CSS)
# ============================================================
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


# ========================= SIDEBAR
st.sidebar.title('Study Cards')
st.sidebar.markdown("---")
st.sidebar.markdown("🚀 **Engine:** Groq API")
st.sidebar.markdown("🛡️ **Status:** Conectado")


# ========================= BODY
st.title('STUDY CARDS // IA')
st.subheader('🧠 Estude qualquer assunto com cards inteligentes de alta performance.', text_alignment="center")
st.markdown('---')

st.write('Crie cards com inteligência artificial a partir de um tema ou de um texto seu, ou carregue cards que você já tem. Depois é só virar, responder e revisar no seu ritmo em uma interface otimizada.')

st.markdown("""
## ⚡ Por onde começar

Escolha uma opção no menu à esquerda para iniciar sua jornada de aprendizado:

### 📚 Meus Cards
Abra um arquivo de cards existente e comece o processo de revisão ativa.

### ✨ Gerar Cards com IA
Insira um prompt ou tema (ex: *Arquitetura de Microsserviços* ou *Física Quântica*) e deixe o motor da Groq estruturar o seu material.

---

## ⚙️ Como funciona

1. **Definição de Parâmetros:** Escolha a fonte do conteúdo (Tema, Texto ou Base Local).
2. **Processamento Neuronal:** A API da Groq gera e estrutura o banco de dados.
3. **Imersão e Estudo:** Execute o ciclo de perguntas e respostas para fixação de longo prazo.

---

## 💡 Por que este método funciona?

O aprendizado ativo através de *active recall* supera a leitura passiva. A tecnologia acopla a geração de questões direcionadas para acelerar a sua retenção cognitiva.

---

> ℹ️ *Os dados são sintetizados via Inteligência Artificial. Recomenda-se a validação cruzada em conteúdos acadêmicos críticos.*

**Pronto para inicializar? Selecione uma opção no menu lateral.** 👈
""")