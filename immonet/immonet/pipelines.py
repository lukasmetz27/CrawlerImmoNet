# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import mysql.connector

class ImmonetPipeline:
    def process_item(self, item, spider):

        return item


class ImmonetPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            passwd = "Wunderbar2701?!",
            database = "immonet"
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS immo_tb""")
        
        self.curr.execute("""create table immo_tb(
                typ text,
                ort text,
                price text,
                sqm text,
                rooms text,
                website text
                )""")



    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into immo_tb values (%s, %s, %s, %s, %s, %s)""", (
            item["typ"][:],
            item["ort"][:],
            item["price"][:],
            item["sqm"][:],
            item["rooms"][:],
            item["website"][:]
        ))
        self.conn.commit()