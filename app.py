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

    if imc < 18.5:
        mensagem = f"está abaixo do peso."
    
    elif imc < 24.9:
        mensagem = f"está com o peso normal."

    elif imc < 29.9:
        mensagem = f"está com sobrepeso."

    else:
        mensagem = f"está obeso."

    return render_template('calc_imc.html', mensagem = mensagem)