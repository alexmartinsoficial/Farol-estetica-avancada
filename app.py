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
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    
    .stApp > div > div {
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    .big-title {
        font-size: 48px;
        font-weight: bold;
        color: #e74c3c;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .subtitle {
        font-size: 24px;
        color: #2c3e50;
        text-align: center;
        line-height: 1.4;
        margin-bottom: 10px;
    }
    
    .disclaimer {
        font-size: 18px;
        color: #7f8c8d;
        text-align: center;
        font-style: italic;
        margin-bottom: 40px;
    }
    
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
    }
    
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
    
    .footer-info {
        text-align: center;
        color: #7f8c8d;
        font-size: 14px;
        margin-top: 20px;
    }
    
    .cliente-bubble {
        background: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0;
    }
    
    .feedback-success {
        background: #d4edda;
        border-left: 4px solid #28a745;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
    
    .feedback-warning {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
    
    .feedback-danger {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
    
    .score-display {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #667eea;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DADOS DO CENÁRIO: MÁRCIA (VERDE)
# ==========================================

MARCIA_SCENARIO = {
    'nome': 'Márcia',
    'perfil': '🟢 SINAL VERDE',
    'contexto': '''Uma potencial cliente chamada **Márcia (35 anos)** enviou mensagem no WhatsApp perguntando sobre harmonização facial.

**Seu objetivo:** Descobrir se ela TEM ORÇAMENTO sem parecer mercenário e sem dar desconto desnecessário.''',
    
    'steps': [
        {
            'cliente_fala': 'Oi! Vi suas fotos no Instagram. Quanto custa harmonização facial completa?',
            'opcoes': [
                {
                    'texto': 'Custa R$ 3.500',
                    'pontos': -2,
                    'tipo': 'danger',
                    'feedback': '❌ **ERRO:** Você passou o preço direto sem criar valor ou qualificar. Ela vai comparar com outros 5 profissionais só por preço.',
                    'resposta_cliente': 'Nossa, achei caro. Vou ver outros profissionais. Obrigada!'
                },
                {
                    'texto': 'Antes de falar sobre valores, me conta: você já pesquisou sobre o procedimento?',
                    'pontos': 3,
                    'tipo': 'success',
                    'feedback': '✅ **ÓTIMO!** Você não entregou o preço de bandeja e começou a qualificar. Criou rapport antes de vender.',
                    'resposta_cliente': 'Já sim! Já fiz toxina antes e agora quero fazer preenchimento também. Pesquisei bastante.'
                },
                {
                    'texto': 'Posso te passar um orçamento! Quando você pode vir aqui para avaliação?',
                    'pontos': 1,
                    'tipo': 'warning',
                    'feedback': '⚠️ **PODE MELHORAR:** Você tentou avançar mas não qualificou se ela tem orçamento. Pode perder tempo com avaliação gratuita.',
                    'resposta_cliente': 'Posso ir semana que vem. Mas antes, quanto custa mais ou menos?'
                },
            ]
        },
        {
            'cliente_fala': 'Legal! E quanto custa mais ou menos?',
            'opcoes': [
                {
                    'texto': 'Entre R$ 2.500 e R$ 4.000. Você já tem uma ideia de quanto pode investir?',
                    'pontos': 3,
                    'tipo': 'success',
                    'feedback': '✅ **EXCELENTE!** Você deu uma faixa E qualificou o orçamento dela. Perfeito!',
                    'resposta_cliente': 'Tenho uns R$ 4.000 guardados para isso. Dá para fazer um bom trabalho?'
                },
                {
                    'texto': 'Depende muito do caso. Melhor vir fazer avaliação.',
                    'pontos': 0,
                    'tipo': 'warning',
                    'feedback': '⚠️ **EVASIVO:** Você não respondeu a pergunta dela. Clientes querem transparência.',
                    'resposta_cliente': 'Mas você não consegue me dar nem uma ideia? Preciso saber se cabe no meu orçamento.'
                },
                {
                    'texto': 'Normalmente R$ 3.500, mas posso fazer por R$ 3.000 se você fechar hoje.',
                    'pontos': -2,
                    'tipo': 'danger',
                    'feedback': '❌ **ERRO:** Você deu desconto SEM NEM SABER se ela precisa! Desvalorizou seu trabalho.',
                    'resposta_cliente': 'Ah legal! Então fica R$ 3.000 mesmo? Vou pensar...'
                },
            ]
        },
        {
            'cliente_fala': 'Tenho uns R$ 4.000 guardados. Dá para fazer um bom trabalho com isso?',
            'opcoes': [
                {
                    'texto': 'Dá sim! Mas preciso avaliar para fazer um plano exato. Tem urgência para fazer?',
                    'pontos': 3,
                    'tipo': 'success',
                    'feedback': '✅ **PERFEITO!** Confirmou o orçamento E já começou a qualificar urgência (Timeline). Excelente!',
                    'resposta_cliente': 'Tenho sim! Tenho um casamento em 6 semanas e quero estar linda.'
                },
                {
                    'texto': 'Dá! Quando você quer marcar a avaliação?',
                    'pontos': 2,
                    'tipo': 'success',
                    'feedback': '✅ **BOM!** Você avançou para o próximo passo, mas perdeu chance de qualificar urgência.',
                    'resposta_cliente': 'Posso ir semana que vem!'
                },
                {
                    'texto': 'Para fazer completo fica R$ 5.500. Consegue aumentar o orçamento?',
                    'pontos': -3,
                    'tipo': 'danger',
                    'feedback': '❌ **PÉSSIMO!** Ela tem R$ 4.000 e você pediu mais! Perdeu a cliente.',
                    'resposta_cliente': 'Não posso gastar mais que isso. Vou procurar outro lugar. Obrigada.'
                },
            ]
        },
    ]
}

# Inicializar session state
if 'page' not in st.session_state:
    st.session_state.page = 'capa'
if 'marcia_step' not in st.session_state:
    st.session_state.marcia_step = 0
if 'marcia_score' not in st.session_state:
    st.session_state.marcia_score = 0
if 'marcia_history' not in st.session_state:
    st.session_state.marcia_history = []

# ==========================================
# FUNÇÕES DE NAVEGAÇÃO
# ==========================================

def go_to_page(page_name):
    st.session_state.page = page_name
    st.rerun()

def reset_marcia():
    st.session_state.marcia_step = 0
    st.session_state.marcia_score = 0
    st.session_state.marcia_history = []

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
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 QUERO IDENTIFICAR CLIENTES DE VERDADE", 
                     type="primary", 
                     use_container_width=True):
            go_to_page('scenarios')
    
    st.markdown('''
    <div class="footer-info">
        ⚡ Gratuito • 5 minutos • Resultado imediato
    </div>
    ''', unsafe_allow_html=True)

# ==========================================
# TELA 2: SELEÇÃO DE CENÁRIOS
# ==========================================

def show_scenarios():
    st.markdown('<div class="big-title">Escolha um Cenário</div>', unsafe_allow_html=True)
    
    st.markdown("### 3 Situações Reais do Dia a Dia")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🟢 CENÁRIO 1: MÁRCIA**
        
        Cliente com orçamento definido.
        Já pesquisou e quer começar logo.
        
        *Dificuldade: Fácil*
        """)
        if st.button("Começar", key="start_marcia", type="primary", use_container_width=True):
            reset_marcia()
            go_to_page('marcia')
    
    with col2:
        st.markdown("""
        **🟡 CENÁRIO 2: PAULA**
        
        Interessada mas sem verba pronta.
        "Vou ver se consigo juntar..."
        
        *Dificuldade: Média*
        """)
        st.button("Em breve", disabled=True, key="c2", use_container_width=True)
    
    with col3:
        st.markdown("""
        **🔴 CENÁRIO 3: CARLA**
        
        Só pesquisando preços.
        "Talvez ano que vem..."
        
        *Dificuldade: Difícil*
        """)
        st.button("Em breve", disabled=True, key="c3", use_container_width=True)
    
    st.markdown("---")
    
    if st.button("⬅️ Voltar para o Início"):
        go_to_page('capa')

# ==========================================
# TELA 3: SIMULADOR MÁRCIA
# ==========================================

def show_marcia():
    scenario = MARCIA_SCENARIO
    current_step = st.session_state.marcia_step
    
    # Cabeçalho
    st.markdown(f'<div class="big-title">📱 Cenário: {scenario["nome"]}</div>', unsafe_allow_html=True)
    st.markdown(f'**Perfil:** {scenario["perfil"]}')
    
    # Contexto (só no início)
    if current_step == 0:
        st.info(scenario['contexto'])
        st.markdown("---")
    
    # Mostrar pontuação e progresso
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="score-display">📊 Pontos: {st.session_state.marcia_score}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="score-display">🎯 Pergunta: {current_step + 1}/{len(scenario["steps"])}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Verificar se acabou
    if current_step >= len(scenario['steps']):
        show_marcia_result()
        return
    
    # Pegar step atual
    step_data = scenario['steps'][current_step]
    
    # Mostrar fala da cliente
    st.markdown(f'''
    <div class="cliente-bubble">
        <strong>💬 {scenario["nome"]} diz:</strong><br>
        "{step_data["cliente_fala"]}"
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("### Como você responde?")
    
    # Mostrar opções
    for idx, opcao in enumerate(step_data['opcoes']):
        letra = chr(65 + idx)  # A, B, C, D
        if st.button(f"{letra}) {opcao['texto']}", key=f"opt_{current_step}_{idx}", use_container_width=True):
            # Registrar escolha
            st.session_state.marcia_history.append({
                'step': current_step,
                'escolha': opcao['texto'],
                'pontos': opcao['pontos'],
                'feedback': opcao['feedback'],
                'resposta': opcao['resposta_cliente']
            })
            st.session_state.marcia_score += opcao['pontos']
            st.session_state.marcia_step += 1
            st.rerun()
    
    st.markdown("---")
    
    # Botão voltar
    if st.button("⬅️ Voltar para Cenários"):
        reset_marcia()
        go_to_page('scenarios')

# ==========================================
# TELA 4: RESULTADO MÁRCIA
# ==========================================

def show_marcia_result():
    st.markdown('<div class="big-title">🎯 Resultado Final</div>', unsafe_allow_html=True)
    
    score = st.session_state.marcia_score
    max_score = 9  # 3 perguntas x 3 pontos cada
    
    # Classificação
    if score >= 7:
        classificacao = "🟢 EXCELENTE QUALIFICADOR!"
        cor = "success"
        mensagem = "Você domina a arte de qualificar clientes! Sabe fazer as perguntas certas e não desperdiça tempo nem dá descontos desnecessários."
    elif score >= 3:
        classificacao = "🟡 BOM, MAS PODE MELHORAR"
        cor = "warning"
        mensagem = "Você tem noção básica de qualificação, mas ainda comete erros que podem custar clientes bons ou atrair os ruins."
    else:
        classificacao = "🔴 PRECISA TREINAR MAIS"
        cor = "danger"
        mensagem = "Você está perdendo clientes bons e atraindo os ruins. Precisa melhorar urgentemente suas perguntas de qualificação."
    
    st.markdown(f'<div class="score-display" style="font-size: 32px;">{classificacao}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="score-display">Pontuação: {score}/{max_score} pontos</div>', unsafe_allow_html=True)
    
    if cor == "success":
        st.success(mensagem)
    elif cor == "warning":
        st.warning(mensagem)
    else:
        st.error(mensagem)
    
    st.markdown("---")
    st.markdown("### 📝 Revisão das suas escolhas:")
    
    # Mostrar histórico
    for idx, item in enumerate(st.session_state.marcia_history):
        with st.expander(f"Pergunta {idx + 1} ({item['pontos']:+d} pontos)"):
            st.markdown(f"**Você escolheu:** {item['escolha']}")
            
            feedback_class = f"feedback-{MARCIA_SCENARIO['steps'][item['step']]['opcoes'][0]['tipo']}"
            for opcao in MARCIA_SCENARIO['steps'][item['step']]['opcoes']:
                if opcao['texto'] == item['escolha']:
                    feedback_class = f"feedback-{opcao['tipo']}"
                    break
            
            st.markdown(f'<div class="{feedback_class}">{item["feedback"]}</div>', unsafe_allow_html=True)
            st.markdown(f"**Cliente respondeu:** \"{item['resposta']}\"")
    
    st.markdown("---")
    
    # CTAs
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Tentar Novamente", use_container_width=True, type="primary"):
            reset_marcia()
            go_to_page('marcia')
    
    with col2:
        if st.button("🏠 Voltar ao Início", use_container_width=True):
            reset_marcia()
            go_to_page('capa')
    
    st.markdown("---")
    
    # CTA de Vendas
    show_cta_vendas()

# ==========================================
# CTA DE VENDAS
# ==========================================

def show_cta_vendas():
    st.markdown('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 30px; border-radius: 15px; color: white; margin: 30px 0;">
        <h2 style="text-align: center; margin-top: 0;">🎁 Quer dominar TODAS as 4 etapas?</h2>
        <p style="text-align: center; font-size: 18px;">
            Você treinou apenas <strong>BUDGET</strong> (Quem tem dinheiro?)<br><br>
            Mas ainda faltam 3 etapas críticas:
        </p>
        <ul style="font-size: 16px; line-height: 1.8;">
            <li><strong>AUTHORITY:</strong> Quem decide realmente?</li>
            <li><strong>NEED:</strong> Qual a necessidade real?</li>
            <li><strong>TIMELINE:</strong> Qual a urgência?</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Ferramenta FAROL Completa:")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ✅ 4 Simuladores Interativos (todas as etapas)  
        ✅ Scripts prontos para cada objeção  
        ✅ Mapa mental de qualificação  
        ✅ Guia de respostas para cada sinal  
        
        *Menos que o tempo perdido com 1 cliente errado.*
        """)
    
    with col2:
        st.markdown('<div style="text-align: center; font-size: 32px; font-weight: bold; color: #27ae60; margin-top: 20px;">R$ 27,00</div>', unsafe_allow_html=True)
    
    whatsapp_number = "556232170183"
    whatsapp_message = "Oi Jéssica! Quero a Ferramenta FAROL Completa (R$ 27,00)"
    whatsapp_link = f"https://wa.me/{whatsapp_number}?text={whatsapp_message.replace(' ', '%20')}"
    
    st.markdown(f'''
    <div style="text-align: center; margin: 30px 0;">
        <a href="{whatsapp_link}" target="_blank" style="
            background: #25D366;
            color: white;
            padding: 15px 40px;
            text-decoration: none;
            border-radius: 50px;
            font-size: 20px;
            font-weight: bold;
            display: inline-block;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
        ">
            💬 QUERO A FERRAMENTA COMPLETA - R$ 27,00
        </a>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center; color: #7f8c8d; font-size: 14px;">Pagamento via PIX • Acesso imediato após confirmação</p>', unsafe_allow_html=True)

# ==========================================
# ROTEAMENTO DE PÁGINAS
# ==========================================

if st.session_state.page == 'capa':
    show_capa()
elif st.session_state.page == 'scenarios':
    show_scenarios()
elif st.session_state.page == 'marcia':
    show_marcia()
