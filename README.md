🧠 MindMap Studio | HUD & Gerador de Mapas Mentais
Um aplicativo web interativo moderno desenvolvido em Python, Streamlit e Graphviz que permite criar, estruturar e visualizar mapas mentais complexos em tempo real a partir de texto indentado.

✨ Funcionalidades
HUD Interativa (Streamlit): Interface web local responsiva com painel lateral de controle e pré-visualização instantânea.

Parser de Texto Inteligente: Converte automaticamente blocos de texto indentados (via Tab ou espaços) em uma árvore hierárquica estruturada.

Múltiplos Layouts e Formatos: Suporte a diferentes orientações de fluxo (Vertical, Horizontal, etc.) e formatos de nós personalizados (Retângulos arredondados, elipses, etc.).

Exportação Rápida: Opção para baixar o código estruturado em Graphviz (.dot) diretamente pela interface.

Design Dark Minimalista: Estética moderna em tons escuros e acentos refinados (#0d1117).

🛠️ Pré-requisitos e Dependências
Certifique-se de ter o Python instalado no seu computador. Além disso, o projeto depende do executável do Graphviz instalado no sistema operacional.

Instale o Graphviz no Windows (caso ainda não tenha):

PowerShell
winget install Graphviz.Graphviz
(Certifique-se de que o caminho dos binários esteja no PATH do sistema, geralmente em C:\Program Files\Graphviz\bin).

Instale as bibliotecas Python necessárias:

Bash
pip install streamlit graphviz
📂 Estrutura do Projeto
Plaintext
mapa-mental-streamlit/
│
├── mapa_mental.py        # Script principal da aplicação (HUD + Lógica do Parser)
└── README.md             # Documentação do projeto
🚀 Como Executar o Projeto
Abra o terminal na pasta onde o arquivo mapa_mental.py está salvo.

Inicie a aplicação executando o comando do Streamlit:

Bash
streamlit run mapa_mental.py
O painel abrirá automaticamente no seu navegador padrão (geralmente em http://localhost:8501).