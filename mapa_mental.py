from graphviz import Digraph

def criar_mapa_mental(titulo, estrutura, arquivo_saida="mapa_mental"):
    """
    Função genérica para criar um mapa mental a partir de um dicionário.
    
    Parâmetros:
    - titulo: título central do mapa mental (string)
    - estrutura: dicionário representando ramos e sub-tópicos
    - arquivo_saida: nome do arquivo PNG gerado
    """
    dot = Digraph(comment=titulo, format="png")
    dot.attr(rankdir='TB', size='10', nodesep='0.5', ranksep='0.75')
    dot.attr('node', shape='box', style='filled', fontname="Helvetica")

    # Nó central
    dot.node('root', titulo, color="lightgrey")

    # Função recursiva para adicionar nós
    def adicionar_nos(parent, estrutura_dict):
        for i, (chave, valor) in enumerate(estrutura_dict.items()):
            node_id = f"{parent}_{i}"
            dot.node(node_id, chave, color="lightblue")
            dot.edge(parent, node_id)

            if isinstance(valor, dict):
                adicionar_nos(node_id, valor)
            elif isinstance(valor, list):
                for j, item in enumerate(valor):
                    sub_id = f"{node_id}_{j}"
                    dot.node(sub_id, item, color="white")
                    dot.edge(node_id, sub_id)

    adicionar_nos('root', estrutura)
    dot.render(arquivo_saida, view=True)
    print(f"Mapa mental salvo como '{arquivo_saida}.png'")


# ==========================
# MAPA MENTAL 1 – Estrutura e Fatores
# ==========================
estrutura1 = {
    "Fatores": ["Fronteira Oeste", "Cidades médias", "Reação policial"],
    "Facções": ["PCC", "CV", "Quadrilhas móveis", "Grupos regionais de apoio/logística"]
}
titulo1 = "Novo Cangaço - Paraná (Fatores e Facções)"
arquivo1 = "Mapa_Mental1_Fatores_Faccoes"

criar_mapa_mental(titulo1, estrutura1, arquivo1)


# ==========================
# MAPA MENTAL 2 – Linha do Tempo e Conclusão
# ==========================
estrutura2 = {
    "Linha do Tempo": ["2012 – 52 ataques", "2021 – Interceptação", "2022 – Guarapuava", "2025 – Operação"],
    "Conclusão": ["Alvo estratégico", "Corredor logístico", "Centro de reação"]
}
titulo2 = "Novo Cangaço - Paraná (Linha do Tempo e Conclusão)"
arquivo2 = "Mapa_Mental2_LinhaTempo_Conclusao"

criar_mapa_mental(titulo2, estrutura2, arquivo2)
