from flask import Flask,render_template

app = Flask("Meu app")

posts =[
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste.10"
    },
    {
        "titulo": "Segundo post",
        "texto": "outro teste"
    }
]

# Comenario
@app.route('/')
def exibir_entradas():
    """Rota principal da aplicação"""
    entradas = posts #Mock das postagens
    return render_template('exibir_entradas.html',entradas = entradas)