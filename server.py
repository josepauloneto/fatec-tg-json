from flask import Flask
from flask import render_template
import os

print __name__
app = Flask(__name__)

@app.route("/")
def lista_noticias():
    
    lista_arquivos = [id_noticia.replace(".json", "") for id_noticia in os.listdir("./arquivos/")]
    return render_template("lista_noticias.html",nomes = lista_arquivos)
