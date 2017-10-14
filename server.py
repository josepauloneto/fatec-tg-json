import os
from flask import Flask
from flask import render_template
from controllers import noticias_controllers

print __name__
app = Flask(__name__)

@app.route("/")
def lista_noticias():
    lista_arquivos = noticias_controllers.get_lista_noticias()
    return render_template("lista_noticias.html",noticias = lista_arquivos)

@app.route("/<int:id_noticia>")
def mostra_noticia(id_noticia):
    noticia = noticias_controllers.get_noticia(id_noticia)
    return render_template("noticia.html", noticia = noticia)