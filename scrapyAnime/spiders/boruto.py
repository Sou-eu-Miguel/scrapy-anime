# -*- coding: utf-8 -*-
import scrapy


class BorutoSpider(scrapy.Spider):

    name = 'boruto'
    start_urls = ['http://boruto.com.br/']

    def parse(self, response):
        divs_gerais = response.xpath('//*[@id="conteudo"]')
        div_central = divs_gerais.xpath('//*[@id="centro_area"]')
        episodios = div_central.xpath('.//table[contains(@style,"margin-bottom:15px;")]')
        for episodio in episodios:
            yield self.getDadosEpisodio(episodio.xpath('.//*[@id="HOTWordsTxt"]/div[2]/div/div'))


    def getDadosEpisodio(self,episodio):
        if episodio:
            dadosEpisodio = {
                'episodio':{
                    'img': episodio.xpath('.//div[1]/img[2]/@src').extract_first(),
                    'nome': episodio.xpath('.//div[2]/div/text()').extract_first(),
                    'capitulo': episodio.xpath('.//div[2]//span//b/text()').extract_first(),
                }
            }
            return dadosEpisodio
