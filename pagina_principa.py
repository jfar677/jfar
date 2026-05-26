from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "animes.json"

def load_animes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_animes(animes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(animes, f, ensure_ascii=False, indent=2)

@app.route("/")
def dashboard():
    animes = load_animes()
    status_counts = {
        "assistido": len([a for a in animes if a["status"] == "Assistido"]),
        "assistindo": len([a for a in animes if a["status"] == "Assistindo"]),
        "planejando": len([a for a in animes if a["status"] == "Planejando"])
    }
    filtro = request.args.get("filtro", "")
    if filtro:
        animes = [a for a in animes if a["status"] == filtro]
    return render_template("dashboard.html", animes=animes, status_counts=status_counts, filtro_ativo=filtro)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        animes = load_animes()
        novo_anime = {
            "id": str(len(animes) + 1),
            "nome": request.form.get("nome", "").strip(),
            "tipo": request.form.get("tipo", "").strip(),
            "status": request.form.get("status", "Planejando"),
            "notas": request.form.get("notas", "").strip(),
            "data": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        if novo_anime["nome"]:
            animes.append(novo_anime)
            save_animes(animes)
        return redirect(url_for("dashboard"))
    return render_template("adicionar.html", anime=None)

@app.route("/editar/<int:anime_id>", methods=["GET", "POST"])
def editar(anime_id):
    animes = load_animes()
    anime = next((a for a in animes if a["id"] == str(anime_id)), None)
    if not anime:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        anime["nome"] = request.form.get("nome", "").strip()
        anime["tipo"] = request.form.get("tipo", "").strip()
        anime["status"] = request.form.get("status", "Planejando")
        anime["notas"] = request.form.get("notas", "").strip()
        anime["data"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        save_animes(animes)
        return redirect(url_for("dashboard"))
    return render_template("adicionar.html", anime=anime)

@app.route("/deletar/<int:anime_id>")
def deletar(anime_id):
    animes = load_animes()
    animes = [a for a in animes if a["id"] != str(anime_id)]
    save_animes(animes)
    return redirect(url_for("dashboard"))

@app.route("/filtro-detalhado")
def filtro_detalhado():
    animes = load_animes()
    tipo = request.args.get("tipo", "").lower()
    data = request.args.get("data", "")
    nome = request.args.get("nome", "").lower()
    status = request.args.get("status", "")
    
    if tipo:
        animes = [a for a in animes if tipo in a["tipo"].lower()]
    if data:
        animes = [a for a in animes if data in a["data"]]
    if nome:
        animes = [a for a in animes if nome in a["nome"].lower()]
    if status:
        animes = [a for a in animes if a["status"] == status]
    
    todos_os_animes = load_animes()
    tipos_unicos = sorted(set(a["tipo"] for a in todos_os_animes if a["tipo"]))
    
    return render_template("filtro_detalhado.html", animes=animes, tipos=tipos_unicos)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
