from django.contrib import admin
from .models import RegularPizza,SicilianPizza,Salads,Sub,Orders,User_order,Topping,DinnerPlatter,Pasta,Category,Items,Order_counter,Deal

# Register your models here.
admin.site.register(Category)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatter)
admin.site.register(Orders)
admin.site.register(User_order)
admin.site.register(Items)
admin.site.register(Order_counter)
admin.site.register(Deal)
