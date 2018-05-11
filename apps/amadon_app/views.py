from django.shortcuts import render, HttpResponse, redirect

def index(request):
    products = products_list()
    context = {
        "items": products
    }
    return render(request, "amadon_app/index.html", context)

def buy(request):
    print(request.POST["quantity"])
    print(request.POST["product_id"])
    product_id = request.POST["product_id"]
    products = products_list()
    for prod in products:
        if str(prod["id"]) == product_id:
            print("product price: ",prod["price"])
        print(prod["id"])
    return redirect("/amadon_app/checkout")

def checkout(request):

    return render(request, "amadon_app/checkout.html")

def products_list():
    products = [{"id":1,"name":"Dojo T-Shirt","price":"$19.99" }, 
                {"id":2,"name":"Dojo Sweater","price":"$29.99" },
                {"id":3,"name":"Dojo Cup","price":"$4.99" },
                {"id":4,"name":"Algorithm Book","price":"$49.99" }              
            ]
    return products