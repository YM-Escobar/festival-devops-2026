from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "festival": "Pacific DevOps Music Fest",
        "fecha": "15 de diciembre de 2026",
        "artistas": [
            "Imagine Dragons",
            "Coldplay",
            "Foo Fighters"
        ]
    }

app.run(host="0.0.0.0", port=5000)

#Comentario 2