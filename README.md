<p align="center">
  <img src="http://i.imgur.com/wYi2CkD.png" width="700" height="200"/>
</p>

# Scrapy-Anime
Web scrapy de animes(alguns que tive curiosidade)[EM ANDAMENTO...]

## Estrutura do diretório
```sh
.
├── scrapyAnime
│   ├── spiders
│       ├── boruto.py
│    
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
└── scrapy.cfg
```


## Tecnologias
- Python
- Scrapy

## Rodando localmente

Você primeiramente deve adicionar um ambiente virtual
```sh
$ virtualenv venv
$ source /venv/bin/activate
```

Instalar as dependências do projeto
```sh
(venv)$ pip install -r requirements.txt
```

E por fim, rodar o projeto localmente
```
(venv)$ scrapy crawl <Nome-Spider>
```
