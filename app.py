import flask as fk
import agenda

# Inicializador da aplicação Flask
app = fk.Flask(__name__)

@app.get("/")
def get_home():
   # Busca a lista de contatos do módulo 'agenda' e a exibe no template 'index.html'.
    return fk.render_template("index.html", agenda=lista_de_contatos)

@app.post("/cadastrar")
def post_cadastrar():
    # receber dados do form
    val_email = fk.request.form["email"]
    val_nome = fk.request.form["nome"]
    val_fone = fk.request.form["fone"]

    novo_contato = {
        "nome": val_nome,
        "email": val_email,
        "fone": val_fone
    }

    agenda.cadastrar(novo_contato)

    # pede à view que cadastre o resultado
    return fk.redirect("/")

@app.post("/remover")
def post_remover():
    email_remover = fk.request.form["nome"]
    agenda.remover(email_remover)
    return fk.redirect("/")

if __name__ == "__main__":
    app.run(debug=True)