# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ScrapyTuts2Pipeline:

    def __init__(self):
        self.create_db()
        self.create_table()

    def create_db(self):
        self.my_db = sqlite3.connect("my_database.db")
        self.my_cursor = self.my_db.cursor()

    def create_table(self):
        self.my_cursor.execute("DROP TABLE IF EXISTS my_table")
        self.my_cursor.execute(''' create table my_table (
            title text,
            author text,
            tag text)
            ''')

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.my_cursor.execute(''' insert into my_table values(?, ?, ?) ''',
        (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        )
        )

        self.my_db.commit()