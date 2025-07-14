agenda = {
    "adriano@email":{
        "nome": "Adriano",
        "fone": "5198763456"
    },

    "amadeu@email": {
        "nome": "Amadeu",
        "fone": "5192672366"
    },

    "carla@email": {
        "nome": "Carla",
        "fone": "4737737643"
    }
}

def get_agenda():
    """Retorno o dicionário completo da agenda."""
    return agenda

def get_listagem():
    """
    Retorna uma lista de tuplas com os dados dos contatos.
    (Função opcional, não usada no fluxo principal do Flask, mas corrigida)
    """

    listagem = []
    for email, registro in agenda.items():
        listagem.append(
            (email, registro["nome"], registro["fone"])
        )
    return listagem

def cadastrar(contato):
    """
    Cadastrar um novo contato na agenda.
    Recebe um dicionário de contato e usa o email como chave principal.
    """
    emial = contato["email"]
    agenda[email] = contato

def remover(emial):
    """Remover um contato da agenda usando o email como chave."""
    if email in agenda:
        del agenda[email]