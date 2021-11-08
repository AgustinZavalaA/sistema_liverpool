from django.shortcuts import render
from .models import Product, User

# Create your views here.
def index(request):
    return render(request, "store/index.html")


def login(request):
    return render(request, "store/login.html")


def manager(request):
    products = Product.objects.all()
    return render(request, "store/manager.html", {"products": products})


def employee(request):
    products = Product.objects.all()
    return render(request, "store/employee.html", {"products": products})


def purchase(request, id):
    item = Product.objects.get(id=id)
    return render(request, "store/product.html", {"item": item})


def add(request):
    return render(request, "store/add_product.html")


def add_product(request):
    # print(request.POST)
    p = Product(
        name=request.POST.get("name"),
        store_id=int(request.POST.get("sucursal")),
        description=request.POST.get("description"),
        quantity=int(request.POST.get("quantity")),
        price=float(request.POST.get("price")),
    )
    p.save()
    return manager(request)


def sell_product(request, id):
    print(request.POST.get("substract"))
    item = Product.objects.get(id=id)
    item.quantity -= int(request.POST.get("substract"))
    item.save()
    return manager(request)


def delete(request, id):
    item = Product.objects.get(id=id)
    return render(request, "store/delete_product.html", {"item": item})


def del_product(request, id):
    item = Product.objects.get(id=id)
    item.delete()
    return manager(request)


def update(request, id):
    item = Product.objects.get(id=id)
    return render(request, "store/update_product.html", {"item": item})


def upd_product(request, id):
    item = Product.objects.get(id=id)
    item.name = request.POST.get("name")
    item.store_id = request.POST.get("sucursal")
    item.description = request.POST.get("description")
    item.price = request.POST.get("price")
    item.quantity = request.POST.get("quantity")
    item.save()
    return manager(request)


def verify(request):
    users = User.objects.filter(name=request.POST.get("name"))
    if len(users) == 0:
        return login(request)
    else:
        for u in users:
            if u.password == request.POST.get("password"):
                if u.manager:
                    return manager(request)
                elif u.client:
                    return store(request)
                else:
                    return employee(request)
    return login(request)


def register(request):
    return render(request, "store/register.html")


def add_user(request):
    if request.POST.get("password") != request.POST.get("password_repeat"):
        return register(request)
    else:
        man = False
        clie = False
        if request.POST.get("tipo") == 1:
            man = True
        if request.POST.get("tipo") == 3:
            clie = True
        u = User(
            name=f"{request.POST.get('first_name')} {request.POST.get('last_name')}",
            store_id=1,
            manager=man,
            client=clie,
            password=request.POST.get("password"),
            salary=0,
        )
        u.save()
    return login(request)


def store(request):
    products = Product.objects.all()
    return render(request, "store/client.html", {"products": products})
