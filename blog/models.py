from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class Blog(models.Model):
    title = models.CharField("タイトル", max_length=100)
    content = models.TextField("内容")
    postdate = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT,verbose_name ="カテゴリ")

    def __str__(self):
        return self.title