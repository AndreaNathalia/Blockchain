from flask import Flask, render_template, request
from web3 import Web3

#link infura
web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/84618d68559b4f7d92345053f2ddf286'))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods =['GET', 'POST'])
def main():
    if request.method=='POST':
        frm = str(request.form['account'])
        to = '0xdbf0fed49a2c92ab32cb039752a75c09ab827c71'
        pk = str(request.form['pk'])
        amount = request.form['amount']

        webAddFrm = web3.toChecksumAddress(frm)
        webAddTo = web3.toChecksumAddress(to)

        nonce = web3.eth.getTransactionCount(webAddFrm)

        trns = {
            'nonce': nonce,
            'to' : webAddTo,
            'value': web3.toWei(str(amount),'ether'),
            'gas': 21000,
            'gasPrice': web3.toWei(40,'gwei')

        }

        signTrns = web3.eth.account.sign_transaction(trns,pk)
        transaction = web3.eth.sendRawTransaction(signTrns.rawTransaction)

        return render_template('ico.html')
    else:
        return render_template('index.html')


# def home():
#     return '<h1>Bienvenido a mi ICO :)</h1><br><p>Favor enviar la cantidad de ETH deseada a la siguiente dirección:</p><h4>0x1CE8c44d9F45A7b89d3aF5E4648e320416f731A0</h4><br><br><p>Puedes agregar el Token automaticamente a metamask haciendo click en el botón:</p><button>Agregar Token</button>'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8910)