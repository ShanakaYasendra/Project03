from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
import datetime


from .models import Category,RegularPizza,SicilianPizza,Salads,Sub,DinnerPlatter,Topping,User_order,Pasta,Orders,Items,Order_counter


counter = Order_counter.objects.first()
print(counter.counter)
if counter==None:
    set_counter=Order_counter(counter=1)
    set_counter.save()
try:    
        shoping_cart= Items.objects.get(OrderNo=counter.counter).count()
except Exception as e:
        shoping_cart=0

def index(request):
    print(counter)
    if not request.user.is_authenticated:
        return render(request,'login.html',{'message':None})
  
    context= {
        "Category": Category.objects.all(),
        "user": request.user,
        "Order_no": counter,
        "cart_count": Items.objects.filter(username= request.user,OrderNo=counter.counter).count()
    }
    return render(request,'index.html',context)
    
def login_view(request):
    print(request)
    try:
        username=request.POST["username"]
        print(username)
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        print(user)


  
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request,"login.html",{"message":"Invalid credentials"}) 
    except KeyError:
        print('error')
        return render(request,"login.html",{"message":"Invalid credentials"}) 

def logout_view(request):
    logout(request)
    return render(request, "login.html",{"message":"Log out" })

def register_view(request):
    print('register view')
    if request.method == "POST":
        try:
     
            first_name=request.POST["firstname"]
            last_name=request.POST["lastname"]
            username=request.POST["username"]
            email=request.POST["email"]
            password=request.POST["password"]
            password2=request.POST["confirmpassword"]
        
            if not password==password2:
                return render(request,"register.html",{"message":"Passwords don't match."})
            user=User.objects.create_user(username,email,password)
            user.first_name=first_name
            user.last_name=last_name
        
            user.save()

            return render(request,"login.html",{"message":"Registered. You can log in now."}) 
        except Exception as e:
            print('error')
            return render(request,"register.html",{"message":"username Taken"})
    return render(request,"register.html") 

def menu(request,category):
   
    menu,columns=findTable(category)

    context = {
        "user": request.user,
        
        "Category": Category.objects.all(),
        "Active_category":category,
        "Menu": menu,
        "Columns":columns,
        "Topping_price": 0.00,
        "Topping": Topping.objects.all(),
        "Order_number":counter.counter,
        "cart_count": Items.objects.filter(username= request.user,OrderNo=counter.counter).count()
    }
    return render(request,"menu.html",context) 

def orderextra(request, category, name,price,topping):
    
        
        
        menu,columns=findTable(category)
        try:
            item= Items(OrderNo=counter.counter,Item=name, Topping=topping, username=request.user,Price=price)
            item.save()
            
        except Exception as e:
            print ('error is')
            print(e)

        shoping_item= Items.objects.filter(username= request.user,OrderNo=counter.counter)
        #print(item)
        
        context = {
            "user": request.user,
            "Category": Category.objects.all(),
            "Active_category":category,
            "Menu": menu,
            "Columns":columns,
            "Topping_price": 0.00,
            "Topping": Topping.objects.all(),
            "Order_number":counter,
            "cart_count": shoping_item.count()
            }
        return render(request,"menu.html",context) 
            
        
        


           


            


def add(request, category, name,price):
    menu,columns=findTable(category)
    #User = get_object_or_404(User_order, username=request.user)

    item= Items(OrderNo=counter.counter,Item=name,username=request.user,Price=price)
    item.save()

    shoping_item= Items.objects.filter(username= request.user,OrderNo=counter.counter)
    print(item)
    

    
    context = {
         "user": request.user,
         "Category": Category.objects.all(),
         "Active_category":category,
         "Menu": menu,
         "Columns":columns,
         "Topping_price": 0.00,
         "Topping": Topping.objects.all(),
         "Order_number":counter,
         "cart_count": shoping_item.count()
    }
    return render(request,"menu.html",context) 

def load_cart(request):

 
    try:
        user= request.user
        shoping_item= Items.objects.filter(username= user,OrderNo=counter.counter)
        shoping_tottal= Items.objects.filter(username= user,OrderNo=counter.counter).aggregate(Sum('Price')).values()
        shoping_tottal=(float([x for x in shoping_tottal][0]))
    except Exception as e:
        shoping_item =None
        shoping_tottal=None
        print(e)
    context={
        "user": request.user,
        "Category": Category.objects.all(),
        "shoping_item": shoping_item,
        "shoping_total": shoping_tottal,
        "cart_count": Items.objects.filter(username= user,OrderNo=counter.counter).count()
    }

    return render(request,"shopping_cart.html",context) 

def delete_item(request, rowId):
    try:
        print(rowId)
        user= request.user,
        deleteItem= Items.objects.filter(id=rowId)
        print(deleteItem)
        deleteItem.delete()
  
        shoping_item= Items.objects.filter(username= user,OrderNo=counter.counter)
        shoping_tottal= Items.objects.filter(username= user,OrderNo=counter.counter).aggregate(Sum('Price')).values()
        shoping_tottal=(float([x for x in shoping_tottal][0]))
    except Exception as e:
        shoping_item =None
        shoping_tottal=None
        print(e)
    context={
        "user": request.user,
        "Category": Category.objects.all(),
        "shoping_item": shoping_item,
        "shoping_total": shoping_tottal,
        "cart_count": shoping_item.count()
    }
    return render(request,"shopping_cart.html",context)

def cancel_order(request):
    user= request.user
    try:
        delete_or= Items.objects.filter(username=user, OrderNo=counter.counter)
        delete_or.delete()
        shoping_item =None
        shoping_tottal=None
    except Exception as e: 
       
        print(e)
    context={
        "user": request.user,
        "Category": Category.objects.all(),
        "shoping_item": shoping_item,
        "shoping_total": shoping_tottal,
        "cart_count": 0
    }
    return render(request,"shopping_cart.html",context)

def Place_Order(request):
    user= request.user
    counter = Order_counter.objects.first()
    item= User_order(username=request.user,order_number=counter.counter)
    item.save()
    shoping_tottal= Items.objects.filter(username= user).aggregate(Sum('Price')).values()
    shoping_tottal=(float([x for x in shoping_tottal][0]))
    order= Orders(username=request.user,OrderNo=counter.counter,OrderdateTime=datetime.datetime.now(), OrderTotal=shoping_tottal)
    order.save()
    counter=Order_counter.objects.first()
    #new_order_number=User_order(user=request.user,order_number=counter.counter)
    #new_order_number.save()
    counter.counter=counter.counter+1
    counter.save()
    message='Thank You For Ordering'
    context={
        "user": request.user,
        "Category": Category.objects.all(),
        "message": message,
        "Order_No" : counter.counter,
        "shoping_total": 0,
        "cart_count": Items.objects.filter(username= user,OrderNo=counter.counter).count()
      
    }
    return render(request,"shopping_cart.html",context)
   
def order_management(request):
    pendingOrder= User_order.objects.filter(status='initiated')

    context={
        "item":pendingOrder
    }

    return render(request,"order_management.html",context)

def complete_order(request,user, order_number):
    user=User.objects.get(username=user)
    complete=User_order.objects.get(username=user,order_number=order_number)
    complete.status='completed'
    complete.save()

    pendingOrder= User_order.objects.filter(status='initiated')

    context={
        "item":pendingOrder
    }

    return render(request,"order_management.html",context)

def my_orders(request):
    user= request.user
    order=User_order.objects.filter(username=user)
    print(order)
    context={
        "Category": Category.objects.all(),
        "orders": order,
        "cart_count": Items.objects.filter(username= user,OrderNo=counter.counter).count()
    }
    return render(request,"my_orders.html",context)

def view_order(request ,orderNo):
    user= request.user
    order_details= Items.objects.filter(OrderNo=orderNo)
    shoping_item= Items.objects.filter(username= user,OrderNo=orderNo)
    shoping_total= Items.objects.filter(username= user,OrderNo=orderNo).aggregate(Sum('Price')).values()
    shoping_total=(float([x for x in shoping_total][0]))
    print('hi')
    print(shoping_item)
    context={
        "Category": Category.objects.all(),     
        "cart_count": Items.objects.filter(username= user,OrderNo=counter.counter).count(),
        "shoping_item":shoping_item ,
        "shoping_total":shoping_total
    }
    return render(request, "orderDetails.html",context)


def Re_Order(request):
    user= request.user
    counter = Order_counter.objects.first()
    item= User_order(username=request.user,order_number=counter.counter)
    item.save()
    shoping_tottal= Items.objects.filter(username= user).aggregate(Sum('Price')).values()
    shoping_tottal=(float([x for x in shoping_tottal][0]))
    order= Orders(username=request.user,OrderNo=counter.counter,OrderdateTime=datetime.datetime.now(), OrderTotal=shoping_tottal)
    order.save()
    counter=Order_counter.objects.first()
    #new_order_number=User_order(user=request.user,order_number=counter.counter)
    #new_order_number.save()
    counter.counter=counter.counter+1
    counter.save()
    message='Thank You For Ordering'
    context={
        "user": request.user,
        "Category": Category.objects.all(),
        #"shoping_item": shoping_item,
        "shoping_total": 0,
        "message": message,
        "Order_No" : counter.counter,
        "cart_count": Items.objects.filter(username= user,OrderNo=counter.counter).count()
      
    }
    return render(request,"shopping_cart.html",context)
  

def findTable(category):
    if category == "Regular Pizza":
        menu=RegularPizza.objects.all()
        topping = Topping.objects.all()
        columns=3
    elif category == "Sicilian Pizza":
        menu=SicilianPizza.objects.all()
        topping = Topping.objects.all()
        columns=3
    elif category == "Toppings":
        menu=Topping.objects.all()
        columns=1
    elif category == "Subs":
        menu=Sub.objects.all()
        columns=3
    elif category == "Pasta":
        menu=Pasta.objects.all()
        columns=2
    elif category == "Salads":
        menu=Salads.objects.all()
        columns=2
    elif category == "Dinner Platters":
        menu=DinnerPlatter.objects.all()
        columns=3

    return menu,columns
