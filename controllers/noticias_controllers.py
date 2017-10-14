import os
import json


def get_lista_noticias():
    lista_noticias = []
    lista_arquivos = os.listdir("arquivos/")
    for nome_arquivo in lista_arquivos:
        with open("arquivos/"+nome_arquivo) as arquivo:
            lista_noticias.append(json.loads(arquivo.read()))
            arquivo.close()
    return lista_noticias

def get_noticia(id_noticia):
    with open("arquivos/"+str(id_noticia)+".json") as arquivo:
        noticia_json = json.load(arquivo)
        arquivo.close
    if noticia_json:
        return noticia_json
    else:
        raise ValueError('alguma coisa ruim aconteceu no parser do json')
