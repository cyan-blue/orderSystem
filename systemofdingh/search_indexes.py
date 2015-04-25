
#coding:utf-8
__author__ = 'yann'


from models import Product
from haystack import indexes

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
        text = indexes.CharField(document=True, use_template=True)
        def get_model(self):
            return Product
        def index_queryset(self):
            """Used when the entire index for model is updated."""
            return self.get_model().objects.all()
            #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录
