# -*- coding: utf-8 -*-
import scrapy

from ..src.models.anime import Anime
from ..src.models.episodio import Episodio


class BorutoSpider(scrapy.Spider):

    name = 'boruto'
    start_urls = ['http://boruto.com.br/']
    dominio = 'http://boruto.com.br'
    page = -1

    def parse(self, response):

        boruto = Anime(nome=self.name, url=response.url)

        divs_gerais = response.xpath('//*[@id="conteudo"]')
        div_central = divs_gerais.xpath('//*[@id="centro_area"]')
        tbs_episodio = div_central.xpath('.//table[1]')
        paginacao = div_central.xpath('.//p[contains(@class,"main_pagination")]//a/@href')

        for tb in tbs_episodio:

            episodio = self.getDadosEpisodio(tb.xpath('.//div[contains(@class,"boxr")]'))
            if episodio.dados['nome']:
                boruto.dados['episodios'].append(episodio)

                yield episodio.dados

        yield self.proximaPagina(paginacao)

    def getDadosEpisodio(self, episodio_web):

        return Episodio(

            img=episodio_web.xpath('.//div[1]/img[2]/@src').extract_first(),
            nome=episodio_web.xpath('.//div[2]/div/text()').extract_first(),
            capitulo=episodio_web.xpath('.//div[2]//span//b/text()').extract_first(),

        )

    def proximaPagina(self, paginacao):
        self.page += 1
        if self.page < len(paginacao):

            proxima_pagina = paginacao[self.page].extract()

            return scrapy.Request(
                url='{}{}'.format(self.dominio, proxima_pagina),
                callback=self.parse
            )
