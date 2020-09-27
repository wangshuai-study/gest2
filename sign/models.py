import cursor as cursor
import pymysql as pymysql
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# ORM 一般指对象关系映射
# 字段地址 D:\Python\Python37\Lib\site-packages\django\db\models\fields
# 发布会管理表
class Event(models.Model):
    name = models.CharField(max_length=100) #发布会标题
    limit = models.IntegerField() #限制人数
    status = models.BooleanField() #状态
    address = models.CharField(max_length=100) # 地址
    start_time = models.DateTimeField() #发布会时间
    create_time = models.DateTimeField(auto_now=True) #创建时间（自动获取当前时间）

    def __str__(self):
        return self.name
        # return self.address

# 嘉宾   on_delete 删除时会把相关联的数据全部删除
class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE) #关联发布会id
    realname = models.CharField(max_length=64) # 姓名
    phone = models.CharField(max_length=16) # 手机号
    email = models.EmailField() #邮箱
    sign = models.BooleanField() # 签到状态
    create_time = models.DateTimeField(auto_now=True) #创建时间（自动获取当前时间）
    class Meta:
        unique_together = ("phone","event")

'''
创建和管理数据库表的文件,用编程语言来操作数据库,而不是sql语句
编程语言--- ORM---> 数据驱动（pymysql） ----数据库
#创建和管理数据库的文件
sql = "select * from XXX "
pymysql.run(sql)
'''

'''
mvt
models.py  连接数据库
views
templates 页面
'''

'''
发布会签到系统
发布会管理表:  ----->  创建发布会：id,名称,时间,地点,人数,status(状态),创建时间
嘉宾： ----> （媒体,米粉,厂商）user id,姓名,手机号,邮箱,发布会,签到,创建时间
'''
# 写sql语句
# sql = "SELECT 'id','password' FROM 'users' WHERE 'email'= 'webmaster@python.org'"
# cursor.execute(sql)

# user1 = User.objects.get('email'= 'webmaster@python.org')
# user1.id
# user1.password