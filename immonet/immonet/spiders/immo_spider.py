import scrapy
from ..items import ImmonetItem

class ImmoNetSpider(scrapy.Spider):
    name = "immo"
    allowed_domains = ["immonet.de"]
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/43.0.2357.130 Safari/537.36 "
    start_urls = [
        "https://www.immonet.de/immobiliensuche/sel.do?&sortby=0&suchart=1&objecttype=1&marketingtype=1&parentcat=1&city=109657&locationname=67454+Hassloch"
    ]


    def parse(self, response):

        items = ImmonetItem()

        orderss = response.css("div#result-list-stage")
        orders = orderss.css("div.place-over-understitial")

        for order in orders:

            """müssen noch abwägen wie viele optionen: geht mithilfe einer if schleife schauen die länge des Splits an"""

            try:
                typ = order.css("span.text-100::text").get()
                typ = "".join(filter(str.isdigit, typ))
            except:
                typ = "None"

            try:
                ort = order.css("span.text-100::text").get()
            except:
                ort = "None" 


            try:
                price = order.css("span.text-250::text").get()
            except:
                price = "None"

            try:
                sqm = order.css("p.text-250::text").get()
                sqm = "".join(filter(str.isdigit, sqm))
            except:
                sqm = "None"

            try:
                rooms = order.css("p.text-250::text").getall()[2]
                rooms = "".join(filter(str.isdigit, rooms))
            except:
                rooms = "None"

            items["typ"] = typ
            items["ort"] = ort
            items["price"] = price
            items["sqm"] = sqm
            items["rooms"] = rooms

            yield items
