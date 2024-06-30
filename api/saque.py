from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_cedulas(saque):
    cedulas = {
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0
    }

    cedulas_disponiveis = [100, 50, 20, 10, 5, 2]

    for cedula in cedulas_disponiveis:
        if saque >= cedula:
            qtd_cedulas = saque // cedula
            cedulas[cedula] = qtd_cedulas
            saque %= cedula

    return cedulas

@app.route('/api/saque', methods=['POST'])
def saque():
    try:
        data = request.get_json()
        saque = int(data['valor'])

        if saque <= 0:
            return jsonify({'error': 'Valor inválido para saque! Insira um valor positivo.'}), 400

        cedulas = calcular_cedulas(saque)
        return jsonify({'cedulas': cedulas}), 200

    except ValueError:
        return jsonify({'error': 'Valor inválido. Tente um valor inteiro.'}), 400
    except KeyError:
        return jsonify({'error': 'Dados inválidos. Certifique-se de enviar um JSON com o campo "valor".'}), 400

if __name__ == '__main__':
    app.run(debug=True)
