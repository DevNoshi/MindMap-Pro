import os
import streamlit as st
from graphviz import Digraph

# ==========================
# CONFIGURAÇÃO DO PATH DO GRAPHVIZ
# ==========================
graphviz_path = r"C:\Program Files\Graphviz\bin"  # Ajuste o caminho se necessário
if graphviz_path not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + graphviz_path

# ==========================
# CONFIGURAÇÃO DA PÁGINA (HUD)
# ==========================
st.set_page_config(
    page_title="MindMap Studio | HUD",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS Dark Minimalista para a HUD
st.markdown("""
    <style>
        .stApp { background-color: #0d1117; color: #c9d1d9; }
        .stTextArea textarea { background-color: #161b22; color: #58a6ff; font-family: monospace; }
        .stButton>button { background-color: #238636; color: white; border-radius: 6px; border: none; font-weight: bold; }
        .stButton>button:hover { background-color: #2ea043; }
    </style>
""", unsafe_allow_html=True)

# ==========================
# PARSER DE TEXTO INDENTADO
# ==========================
def converter_texto_para_dict(texto):
    """Converte texto indentado de forma segura em dicionário encadeado."""
    linhas = [l for l in texto.split('\n') if l.strip()]
    if not linhas:
        return {}

    raiz = {}
    # Armazena tuplas de (indentacao, dicionario_ou_lista)
    pilha = [( -1, raiz )]

    for linha in linhas:
        # Calcula a indentação baseada em espaços iniciais (considerando 4 espaços ou tabulações)
        espacos = len(linha) - len(linha.lstrip(' '))
        conteudo = linha.strip().lstrip('-*').strip()
        if not conteudo:
            continue

        # Remove da pilha elementos com indentação maior ou igual
        while len(pilha) > 1 and pilha[-1][0] >= espacos:
            pilha.pop()

        pai = pilha[-1][1]

        # Se o elemento pai for um dicionário, adiciona a chave
        if isinstance(pai, dict):
            # Se já existir, vira um dicionário aninhado, senão prepara um novo dict
            novo_nivel = {}
            pai[conteudo] = novo_nivel
            pilha.append((espacos, novo_nivel))

    return raiz

# ==========================
# GERADOR DE GRAPHVIZ
# ==========================
def gerar_graphviz(titulo, estrutura, direcao='TB', formato_no='box'):
    dot = Digraph(comment=titulo, format="svg")
    dot.attr(rankdir=direcao, bgcolor='#0d1117', nodesep='0.6', ranksep='1.0')
    dot.attr('node', shape=formato_no, style='filled,rounded', fontname="Helvetica", fontsize='12', fontcolor='#f0f6fc')
    dot.attr('edge', color='#30363d', penwidth='1.5')

    dot.node('root', titulo, color="#58a6ff", fillcolor='#1f6beb', style='filled,bold', fontsize='16', fontcolor='#ffffff')

    cores = ["#1f6beb", "#238636", "#8957e5", "#d29922", "#db6d28", "#3fb950"]

    def adicionar_nos(parent, estr, nivel=0):
        if not isinstance(estr, dict):
            return
        for i, (chave, valor) in enumerate(estr.items()):
            node_id = f"{parent}_{nivel}_{i}"
            cor = cores[nivel % len(cores)]
            
            dot.node(node_id, chave, color=cor, fillcolor='#161b22', style='filled,rounded')
            dot.edge(parent, node_id, color=cor)

            if isinstance(valor, dict) and valor:
                adicionar_nos(node_id, valor, nivel + 1)

    adicionar_nos('root', estrutura)
    return dot

# ==========================
# INTERFACE HUD (STREAMLIT)
# ==========================
st.title("🧠 Dashboard de Criador de Mapas Mentais")
st.caption("Insira seu texto estruturado para renderizar o mapa dinamicamente.")

# Sidebar - Controles da HUD
with st.sidebar:
    st.header("⚙️ Opções do Mapa")
    titulo_mapa = st.text_input("Título Central", value="Novo Cangaço Paraná")
    
    direcao = st.selectbox(
        "Orientação do Layout",
        options=["TB", "LR", "BT", "RL"],
        format_func=lambda x: {"TB": "Vertical (Cima -> Baixo)", "LR": "Horizontal (Esquerda -> Direita)", "BT": "Baixo -> Cima", "RL": "Direita -> Esquerda"}[x]
    )
    
    formato_no = st.selectbox(
        "Formato dos Nós",
        options=["box", "ellipse", "hexagon", "plaintext"],
        format_func=lambda x: {"box": "Retângulo Arredondado", "ellipse": "Elipse", "hexagon": "Hexágono", "plaintext": "Texto Puro"}[x]
    )

# Área Principal - Layout em Colunas
col_input, col_preview = st.columns([1, 1.5])

# Exemplo padrão de texto indentado
texto_padrao = """Fatores de Atuação
    Geográficos
        Fronteira Oeste
        Cidades Médias
    Sociais
        Violência Local
        Alvos Financeiros
Facções e Grupos
    PCC
        Articulação Nacional
    CV
        Apoio Regional
Linha do Tempo
    2012 - 52 Ataques
    2022 - Ataque Guarapuava"""

with col_input:
    st.subheader("📝 Estrutura do Texto")
    texto_inserido = st.text_area("Digite usando Tab ou 4 espaços para sub-níveis:", value=texto_padrao, height=450)

with col_preview:
    st.subheader("🖼️ Visualização do Mapa")
    
    if texto_inserido.strip():
        try:
            estrutura_dict = converter_texto_para_dict(texto_inserido)
            grafico = gerar_graphviz(titulo_mapa, estrutura_dict, direcao, formato_no)
            
            # Renderiza diretamente na tela da HUD
            st.graphviz_chart(grafico, use_container_width=True)
            
            # Botão para baixar o código DOT
            st.download_button(
                label="📥 Baixar Código Graphviz (.dot)",
                data=grafico.source,
                file_name="mapa_mental.dot",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Erro ao processar a estrutura: {e}")