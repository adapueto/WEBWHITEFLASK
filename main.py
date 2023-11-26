from flask import Flask
import random
import requests

app = Flask(__name__)
facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

def get_fox_image_url():    
    img = 'https://randomfox.ca/floof'
    res = requests.get(img)
    data = res.json()
    return data['image']

@app.route("/")
def index():
    return f'<h1>DATOS DE DEPENDENCIAS TECNOLOGICAS</h1><a href="/random_fact">¡Ver un hecho al azar!</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p><a href="/zorro">Imagenes de zorros</a>'

@app.route("/zorro")
def fox_image():
    return f'<p>{get_fox_image_url()}</p>'

app.run(debug=True)