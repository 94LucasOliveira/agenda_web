agenda = {
    "adriano@email":{
        "nome": "Adriano",
        "fone": "5198763456"
    },

    "amadeu@email": {
        "nome": "Amadeu",
        "fone": "5192672366"
    }

    "carla@email": {
        "nome": "Carla",
        "fone": "4737737643"
    }
}

def get_agenda():
    return agenda

def get_listagem():

    listagem = list()
    for email, registro in agenda.items:
        listagem.append(
            (email, registro["nome"], registro["fone"])
        )
    return listagem

def cadastrar(email, registro):
    agenda[email] = registro

def remover(um_item):
    del agenda[um_item]