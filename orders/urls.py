from django.urls import path

from . import views

urlpatterns = [

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("add/<str:category>/<str:name>/<str:price>",views.add, name="add"),
    path("orderpizza/<str:category>/<str:name>/<str:price>/<str:topping>",views.orderextra,name="orderpizza"),
    path("", views.index, name="index"),
    path("deleteItem/<str:rowId>", views.delete_item, name= "deleteItem"),
    path("order", views.Place_Order,name="order"),
    path("shoppingCart" , views.load_cart, name="shoppingCart"),
    path("orders_manager",views.order_management,name="orders_manager"),
    path("my_orders",views.my_orders,name="my_orders"),
    path("view_order/<str:orderNo>",views.view_order,name="view_order"),
    path("Reorder",views.Re_Order, name="Reorder"),
    path("cancel_order",views.cancel_order, name="cancel_order"),
  
    path("complete_order/<str:user>/<str:order_number>", views.complete_order,name="complete_order"),
   

      path("menu/<str:category>", views.menu, name="menu")
]
