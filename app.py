HEAD
# app.py com rotas atualizadas


from flask import Flask, render_template, request, redirect, url_for, session, send_file
import random, os
from datetime import datetime
from scraping import get_latest_headline
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
app.secret_key = 'super_secret_key'

USERNAME = "fcnews2000"
PASSWORD = "Biel3265980"

def gerar_perspectivas(manchete):
    capetinha = f"Notícia chocante: {manchete}! Preparem-se para o caos! 😈"
    anjinho = f"Informação importante: {manchete}. Vamos espalhar solidariedade e esperança. 😇"
    return capetinha, anjinho

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]
        if user == USERNAME and pwd == PASSWORD:
            session["user"] = user
            return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    
    manchete, capetinha, anjinho = "", "", ""
    if request.method == "POST":
        manchete = get_latest_headline()
        capetinha, anjinho = gerar_perspectivas(manchete)
    return render_template("index.html", manchete=manchete, capetinha=capetinha, anjinho=anjinho)

@app.route("/export", methods=["POST"])
def export():
    manchete = request.form["manchete"]
    capetinha = request.form["capetinha"]
    anjinho = request.form["anjinho"]

    image = Image.new("RGB", (800, 800), color=(30, 30, 30))
    draw = ImageDraw.Draw(image)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font = ImageFont.truetype(font_path, 24)

    draw.text((20, 30), "🪙 FC News", fill="white", font=font)
    draw.text((20, 80), "📰 Manchete:", fill="white", font=font)
    draw.text((20, 120), manchete, fill="white", font=font)
    draw.text((20, 180), "😈 Capetinha:", fill="red", font=font)
    draw.text((20, 220), capetinha, fill="red", font=font)
    draw.text((20, 280), "😇 Anjinho:", fill="lightblue", font=font)
    draw.text((20, 320), anjinho, fill="lightblue", font=font)

    path = os.path.join("static", "fcnews_export.png")
    image.save(path)
    return send_file(path, as_attachment=True)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
 bfbba275a9f813f90eed30fc43624e3c9496eab8
