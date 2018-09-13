from django.db import models
from datetime import datetime
# Create your models here.
class StudentInfo(models.Model):

    name = models.CharField(max_length=30,verbose_name='学生姓名')
    age = models.IntegerField(default=18,verbose_name='学生年龄')
    gender = models.CharField(max_length=10,choices=(('girl','女'),('boy','男')),verbose_name='学生性别')
    height = models.DecimalField(verbose_name='学生身高',decimal_places=2,max_digits=5,null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name