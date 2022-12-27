app = Flask(__name__)

# criar a primeira pag do site no ar
# route -> hashtagteste.com/contatos - Caminho da página
# função -> o que vc quer exibir naquela página

@nomedosite.rout("/") # dentro do parenteses colocar o link da pag para ser exibida.
def homeopage():
    return "Primeiro site"




# colocar o sie no ar
app.run()



