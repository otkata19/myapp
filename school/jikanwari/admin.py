from django.contrib import admin
from .models import SampleDB # models.pyで指定したクラス名

# Register your models here.
admin.site.register(SampleDB) # models.pyで指定したクラス名
