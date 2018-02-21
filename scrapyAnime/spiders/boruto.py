# -*- coding: utf-8 -*-
import scrapy

from ..src.models.anime import Anime
from ..src.models.episodio import Episodio


class BorutoSpider(scrapy.Spider):
    name = 'boruto'
    start_urls = ['http://boruto.com.br/']

    def parse(self, response):

        boruto = Anime(nome=self.name, url=response.url)

        divs_gerais = response.xpath('//*[@id="conteudo"]')
        div_central = divs_gerais.xpath('//*[@id="centro_area"]')
        tbs_episodio = div_central.xpath('.//table[contains(@style,"margin-bottom:15px;")]')

        for tb in tbs_episodio:
            episodio = self.getDadosEpisodio(tb.xpath('.//*[@id="HOTWordsTxt"]/div[2]/div/div'))
            if episodio:

                boruto.dados['episodios'].append(episodio)
                yield episodio.dados

        return

    def getDadosEpisodio(self, episodio_web):

        episodio = Episodio(

            img=episodio_web.xpath('.//div[1]/img[2]/@src').extract_first(),
            nome=episodio_web.xpath('.//div[2]/div/text()').extract_first(),
            capitulo=episodio_web.xpath('.//div[2]//span//b/text()').extract_first(),

        )

        return episodio
