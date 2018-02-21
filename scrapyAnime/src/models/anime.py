# -*- coding: utf-8 -*-
import json
from ..util.encoder import CustomEncoder


class Anime:

    def __init__(self, nome='', descricao='', img='', url=''):
        self.dados = {
            'nome': nome,
            'episodios': [],
            'descricao': descricao,
            'img': img,
            'url': url
        }

    def __str__(self):
        return json.dumps(self.dados, cls=CustomEncoder)
