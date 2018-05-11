from django.shortcuts import render, HttpResponse, redirect

def index(request):
    products = products_list()
    context = {
        "items": products
    }
    return render(request, "amadon_app/index.html", context)

def buy(request):
    # total items
    if not "count" in request.session:
        request.session["count"] = 0
    # total spent
    if not "total" in request.session:
        request.session["total"] = 0
    # current item
    product_id = request.POST["product_id"]
    product_quantity = int(request.POST["quantity"])
    # products info
    products = products_list()
    # find price for item in list
    for prod in products:
        if prod["id"] == product_id:
            request.session["subtotal"] = product_quantity * prod["price"]
            request.session["total"] += round(request.session["subtotal"],2)
    # update total items
    request.session["count"] += product_quantity

    return redirect("/amadon_app/checkout")

def checkout(request):

    return render(request, "amadon_app/checkout.html")

def products_list():
    products = [{"id":"1","name":"Dojo T-Shirt","price":19.99 }, 
                {"id":"2","name":"Dojo Sweater","price":29.99 },
                {"id":"3","name":"Dojo Cup","price":4.99 },
                {"id":"4","name":"Algorithm Book","price":49.99 }              
            ]
    return products