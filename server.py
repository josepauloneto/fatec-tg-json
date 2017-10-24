import os
from flask import Flask
from flask import render_template
import cx_Oracle
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

@app.route("/database/lista_noticias")
def lista_noticias_banco():
    conn = cx_Oracle.connect('oe/oe@localhost/orcl')
    cursor = conn.cursor()
    noticias = cursor.execute("""SELECT id_noticia, titulo FROM noticia""")
    #cursor.close()
    #conn.close()
    return render_template("lista_noticias_banco.html", noticias = noticias)

@app.route("/database/<int:id_noticia>")
def mostra_noticia_banco(id_noticia):
    conn = cx_Oracle.connect('oe/oe@localhost/orcl')
    cursor = conn.cursor()
    cursor.execute("""SELECT titulo, conteudo, autor FROM noticia where id_noticia = :id_not""", id_not=id_noticia)
    for noticia in cursor:
        noticia_expecifica = noticia
    return render_template("noticia_banco.html", noticia = noticia_expecifica)
    

if __name__ == "__main__":
    app.run()
