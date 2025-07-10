import flask as fk
import agenda

app = fk.Flask(__name__)

@app.get("/")
def get_home():
   # listagem_agenda = agenda.get_listagem()
    return fk.render_template("index.html", agenda=agenda.get_agenda)

@app.post("/cadastrar")
def post_cadastrar():
    # receber dados do form
    val_email = fk.request.form["email"]
    val_nome = fk.request.form["nome"]
    val_fone = fk.request.form["fone"]

    # pede à model que cadastre
    agenda.cadastrar(val_email, {
        "nome": val_nome
        "fone": val_fone
    })
    # pede à view que cadastre o resultado
    return fk.redirect("/")

@app.route("/remover/<nome>")
def remover(email):
    agenda.remover(email)
    return fk.redirect("/")

@app.route("/remover")
def post_remover():
    nome = fk.request.form["nome"]
    agenda.remover(nome)
    return fk.redirect("/")