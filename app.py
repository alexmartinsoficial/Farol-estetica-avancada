import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Xô Curioso! - Qualificação de Clientes",
    page_icon="🚫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS customizado
st.markdown("""
<style>
    /* Esconder menu padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Estilo geral */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    
    /* Container branco */
    .stApp > div > div {
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    /* Título principal */
    .big-title {
        font-size: 48px;
        font-weight: bold;
        color: #e74c3c;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Subtítulo */
    .subtitle {
        font-size: 24px;
        color: #2c3e50;
        text-align: center;
        line-height: 1.4;
        margin-bottom: 10px;
    }
    
    /* Disclaimer */
    .disclaimer {
        font-size: 18px;
        color: #7f8c8d;
        text-align: center;
        font-style: italic;
        margin-bottom: 40px;
    }
    
    /* Lista de dores */
    .pain-list {
        background: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 20px;
        border-radius: 10px;
        margin: 30px 0;
    }
    
    .pain-item {
        font-size: 18px;
        color: #2c3e50;
        margin: 10px 0;
        display: flex;
        align-items: center;
    }
    
    /* Benefícios */
    .benefits {
        background: #e7f3ff;
        border-left: 5px solid #2196F3;
        padding: 20px;
        border-radius: 10px;
        margin: 30px 0;
    }
    
    .benefit-item {
        font-size: 16px;
        color: #2c3e50;
        margin: 8px 0;
    }
    
    /* Footer da capa */
    .footer-info {
        text-align: center;
        color: #7f8c8d;
        font-size: 14px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session state
if 'page' not in st.session_state:
    st.session_state.page = 'capa'

# ==========================================
# FUNÇÕES DE NAVEGAÇÃO
# ==========================================

def go_to_scenarios():
    st.session_state.page = 'scenarios'
    st.rerun()

# ==========================================
# TELA 1: CAPA PROVOCATIVA
# ==========================================

def show_capa():
    st.markdown('<div class="big-title">🚫 XÔ CURIOSO!</div>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="subtitle">
        Identifique em 5 minutos quem <strong>TEM DINHEIRO</strong><br>
        e quem só quer <strong>ORÇAMENTO GRÁTIS</strong>.
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div class="disclaimer">Não é curso! É um guia prático.</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Seção de dores
    st.markdown('''
    <div class="pain-list">
        <h3 style="margin-top: 0; color: #856404;">Você está cansado de:</h3>
        <div class="pain-item">❌ Clientes pedindo desconto sem parar</div>
        <div class="pain-item">❌ "Vou pensar" que nunca mais voltam</div>
        <div class="pain-item">❌ Perder horas em orçamentos vazios</div>
        <div class="pain-item">❌ Competir só por preço com a concorrência</div>
        <div class="pain-item">❌ Agenda cheia mas faturamento baixo</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Seção de benefícios
    st.markdown('''
    <div class="benefits">
        <h3 style="margin-top: 0; color: #0d47a1;">O que você vai aprender:</h3>
        <div class="benefit-item">✅ Identificar em 30 segundos quem tem orçamento</div>
        <div class="benefit-item">✅ Fazer perguntas certas sem parecer mercenário</div>
        <div class="benefit-item">✅ Desqualificar clientes errados sem culpa</div>
        <div class="benefit-item">✅ Focar energia apenas em quem vai fechar</div>
        <div class="benefit-item">✅ Parar de dar desconto por insegurança</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botão CTA principal
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 QUERO IDENTIFICAR CLIENTES DE VERDADE", 
                     type="primary", 
                     use_container_width=True,
                     key="cta_inicio"):
            go_to_scenarios()
    
    # Footer
    st.markdown('''
    <div class="footer-info">
        ⚡ Gratuito • 5 minutos • Resultado imediato
    </div>
    ''', unsafe_allow_html=True)

# ==========================================
# TELA 2: SELEÇÃO DE CENÁRIOS (PLACEHOLDER)
# ==========================================

def show_scenarios():
    st.markdown('<div class="big-title">Escolha um Cenário</div>', unsafe_allow_html=True)
    
    st.markdown("### 3 Situações Reais do Dia a Dia")
    
    st.info("🚧 **Em construção** - Os cenários interativos serão adicionados na próxima etapa!")
    
    # Prévia dos cenários
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🟢 CENÁRIO 1: MÁRCIA**
        
        Cliente com orçamento definido.
        Já pesquisou e quer começar logo.
        
        *Dificuldade: Fácil*
        """)
        st.button("Em breve", disabled=True, key="c1")
    
    with col2:
        st.markdown("""
        **🟡 CENÁRIO 2: PAULA**
        
        Interessada mas sem verba pronta.
        "Vou ver se consigo juntar..."
        
        *Dificuldade: Média*
        """)
        st.button("Em breve", disabled=True, key="c2")
    
    with col3:
        st.markdown("""
        **🔴 CENÁRIO 3: CARLA**
        
        Só pesquisando preços.
        "Talvez ano que vem..."
        
        *Dificuldade: Difícil*
        """)
        st.button("Em breve", disabled=True, key="c3")
    
    st.markdown("---")
    
    if st.button("⬅️ Voltar para o Início", key="back_capa"):
        st.session_state.page = 'capa'
        st.rerun()

# ==========================================
# ROTEAMENTO DE PÁGINAS
# ==========================================

if st.session_state.page == 'capa':
    show_capa()
elif st.session_state.page == 'scenarios':
    show_scenarios()
