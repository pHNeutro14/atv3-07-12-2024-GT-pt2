from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/calc_imc', methods=["GET"])
def calc_imc():
    altura = float(request.args.get("altura"))
    peso = float(request.args.get("peso"))
    imc = round((peso/altura**2),2)
    mensagem = f"olá deus sou eu dnv {imc}"


    return render_template('calc_imc.html', mensagem = mensagem)