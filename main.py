from flask import Flask

# ======================
# INICIALIZAÇÃO DO FLASK
# ======================

# Instanciando o Flask
app = Flask(__name__)

# Definindo o caminho (link) da Home Page
@app.route('/')
def home():
    return 'Hello World! Primeiro site no ar....'

@app.route('/contato')
def contato():
    return 'Qualquer dúvida, sugestão ou reclamação, enviar um e-mail para contato@contato.com.br'

# Indicando que a página só será executada se o arquivo for o main.py
if __name__ == "__main__":
    app.run(debug=True) # Inicia o site no modo Debug, permitindo que a cada atualização do código basta apenas atualizar a página.