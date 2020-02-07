# -*- coding: utf-8 -*-
import scrapy


class ImobSpider(scrapy.Spider):
    name = "imob"
    allowed_domains = ["www.imoveismartinelli.com.br"]
    start_urls = [
        "https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=L&id_tipo_imovel%5B%5D=33&finalidade=0&dormitorio=0&garagem=0&vmi=&vma="
    ]

    def parse(self, response):
        for home in response.css("div.item"):
            price = home.css("div.price").css("span::text")
            yield {"price": price.getall()}

        for link in response.css(".pagination").xpath("./ul/li/a")[-1:]:
            url = link.xpath("@href").get()
            yield response.follow(url)

