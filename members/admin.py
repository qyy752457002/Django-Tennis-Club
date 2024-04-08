from django.contrib import admin
from .models import Member

# Very important ! ! !

# 我们可以通过在 admin.py 文件中指定它们来控制要显示的字段，
# 方法是在 list_display 属性中创建一个 MemberAdmin() 类，
# 并指定 list_display 元组，如下所示

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
    prepopulated_fields = {"slug": ("firstname", "lastname")}

admin.site.register(Member, MemberAdmin)
