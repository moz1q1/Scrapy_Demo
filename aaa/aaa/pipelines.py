# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AaaPipeline(object):
    def process_item(self, item, spider):
        for jpg_url in zip(item['src']):
            print("process_item.jpg_url:" + str(jpg_url))
        return item
