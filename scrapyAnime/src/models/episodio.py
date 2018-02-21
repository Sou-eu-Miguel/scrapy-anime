# -*- coding: utf-8 -*-
import json
from ..util.encoder import CustomEncoder

class Episodio:

    def __init__(self, nome='', capitulo='0', img='', descricao=''):

        self.dados = {
            'nome': nome,
            'capitulo': capitulo,
            'descricao': descricao,
            'img': img,
        }

    def __str__(self):

        return json.dumps(self.dados, cls=CustomEncoder)
