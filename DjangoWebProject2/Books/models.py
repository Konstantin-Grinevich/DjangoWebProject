from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=120, verbose_name='Название')
    author = models.ForeignKey('Author', blank=True, null=True, verbose_name = 'Автор', on_delete = models.CASCADE)
    status=(('r1', 'Роман'), ('p','Поэма'), ('s','Стихотворение'), ('r2','Рассказ'))
    status = models.CharField(max_length=2,choices=status,blank=True,default='r1',verbose_name='Жaнр')
    sheets = models.IntegerField(verbose_name="Кол-во страниц")
    price = models.IntegerField(verbose_name="Цена")
    publisher = models.ForeignKey('Publisher', blank=True, null=True, verbose_name = 'Издатель', on_delete = models.CASCADE)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=120,verbose_name='Имя')
    second_name=models.CharField(max_length=120,verbose_name='Фамилия')
    contry = models.CharField(max_length=120, verbose_name='Гражданство')

    def __unicode__(self):
        return self.first_name+' '+self.second_name

    def __str__(self):
        return self.first_name+' '+self.second_name

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=120,verbose_name='Название издательства')
    city = models.CharField(max_length=60, verbose_name='Город')
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name