import os
from graphviz import Digraph

# Adicionar Graphviz ao PATH do sistema
os.environ['PATH'] += os.pathsep + 'C:/Program Files/Graphviz/bin'

dot = Digraph(comment='Mapa Mental', format='png')
dot.node('A', 'Tópico Central')
dot.render('mapa_mental', view=True)