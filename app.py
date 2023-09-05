from flask import Flask,render_template

app = Flask("Meu app")

posts =[
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste"
    },
    {
        "titulo": "Segundo post",
        "texto": "teste2.0"
    }
]

# Comenario
@app.route('/')
def exibir_entradas():
    """Rota principal da aplicação"""
    entradas = posts #Mock das postagens
    return render_template('exibir_entradas.html',entradas = entradas)