import os
from graphviz import Digraph

# ==========================
# GARANTE QUE O PYTHON ENXERGUE O GRAPHVIZ
graphviz_bin = r"C:\Program Files\Graphviz\bin"  # Ajuste para seu caminho
if graphviz_bin not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + graphviz_bin

# ==========================
# FUNÇÃO PARA CRIAR MAPAS MENTAIS GRANDES EM SVG
# ==========================
def criar_mapa_mental_avancado(titulo, estrutura, arquivo_saida="mapa_mental"):
    """
    Cria um mapa mental detalhado e grande em SVG, suportando múltiplos níveis de ramificação.
    """
    dot = Digraph(comment=titulo, format="svg")
    dot.attr(rankdir='TB', size='40', nodesep='1.5', ranksep='2.5')
    dot.attr('node', shape='box', style='filled,rounded', fontname="Helvetica", fontsize='16')

    # Nó central
    dot.node('root', titulo, color="#FFD700", style='filled,bold', fontsize='22')

    # Paleta de cores para ramos principais e sub-ramos
    cores_ramos = [
        "#87CEFA", "#FFB6C1", "#98FB98", "#FFA500", "#9370DB", "#FF6347",
        "#40E0D0", "#FFDAB9", "#E6E6FA", "#FAFAD2", "#D8BFD8", "#F08080"
    ]

    def adicionar_nos(parent, estrutura_dict, nivel=0):
        for i, (chave, valor) in enumerate(estrutura_dict.items()):
            node_id = f"{parent}_{nivel}_{i}"
            cor = cores_ramos[nivel % len(cores_ramos)]
            dot.node(node_id, chave, color=cor, style='filled,rounded', fontsize='18')
            dot.edge(parent, node_id)

            if isinstance(valor, dict):
                adicionar_nos(node_id, valor, nivel + 1)
            elif isinstance(valor, list):
                for j, item in enumerate(valor):
                    sub_id = f"{node_id}_{j}"
                    sub_cor = "#FFFFFF" if nivel == 0 else "#F0F8FF"
                    dot.node(sub_id, item, color=sub_cor, style='filled,rounded', fontsize='16')
                    dot.edge(node_id, sub_id)

    adicionar_nos('root', estrutura)
    dot.render(arquivo_saida, view=True)
    print(f"✅ Mapa mental grande salvo como '{arquivo_saida}.svg'")


# ==========================
# EXEMPLO DE MAPA MENTAL GRANDE
# ==========================
estrutura_grande = {
    "Fatores de atuação": {
        "Geográficos": ["Fronteira Oeste", "Cidades médias", "Rodovias estratégicas"],
        "Sociais": ["Violência local", "Alvos financeiros", "Comunidade colaborativa"],
        "Policiais": ["Reação PMPR", "Interceptações PF", "Operações Gaeco"]
    },
    "Facções e Grupos": {
        "PCC": ["Articulação nacional", "Logística armada"],
        "CV": ["Apoio regional", "Roubo de cargas"],
        "Quadrilhas móveis": ["Ataques simultâneos", "Roubos coordenados"],
        "Grupos de apoio": ["Alimentação", "Transporte", "Inteligência local"]
    },
    "Linha do Tempo": ["2012 – 52 ataques", "2021 – Interceptações", 
                       "2022 – Ataque Guarapuava", "2025 – Operação policial"],
    "Conclusões": ["Paraná = alvo estratégico", "Corredor logístico", "Centro de reação"]
}

titulo_grande = "Novo Cangaço Paraná - Mapa Avançado"
arquivo_grande = "Mapa_Mental_Grande"

criar_mapa_mental_avancado(titulo_grande, estrutura_grande, arquivo_grande)
# ==========================