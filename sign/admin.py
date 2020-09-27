from django.contrib import admin
# 导入两张表
from sign.models import Event,Guest
# Register your models here.
# django自带admin后台
# 把models（db）里面的表映射到后台管理  register注册 admin.site.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','limit','status','address','start_time','create_time']
    search_fields = ['name'] #搜索栏
    list_filter = ['status'] #过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','event']
    search_fields = ['name']  # 搜索栏
    list_filter = ['sign']  # 过滤器
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)

