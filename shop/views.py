import json
import random

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from shop.forms import PostForm
from shop.models import Post, Product


@csrf_exempt
def json_response_view(request: WSGIRequest):
    if request.method == 'GET':
        return JsonResponse({"first": 'content', 'second': 'test'})
    elif request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        
        Post.objects.create(title=data["title"], content=data["content"])
        return JsonResponse({"status": "ok, I got you."})
    else:
        return JsonResponse({"status": 'no, I don\'t know it.'})


def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, 'shop/post_create.html', context)


# Create your views here.
def hello(request):
    context = {
        "first_var": "Hello Man",
        "second_var": 87.8787,
        # 新增一筆用來比對的字串在 list 裡
        "third_list": ["歡迎", "你好", "我是 RS", "來比對我阿"]
    }
    
    # 表示會載入 templates/shop/index.html
    return render(request, 'shop/index.html', context)


def shop_view(request):
    context = {
        'products': list(Product.objects.all())
    }
    return render(request, 'shop/shop.html', context)


def insert_view(request):
    for i in range(5):
        product = Product()
        product.name = f"測試{str(random.randint(0, 5))}"
        product.price = random.randint(1, 500)
        product.save()
    
    return HttpResponse("批次新增資料完成")


def lookup_view(request):
    products = Product.objects.all()
    result = []
    for product in products:
        result.append({"product name": product.name, "price": float(product.price)})

    return HttpResponse(result)


def modify_view(request):
    product = Product.objects.get(id=1)
    product.name = "我是後來才修改的產品"
    product.save()
    return HttpResponse('修改完成，請到 SQL shell下指令\nsql> select * from shop_product where id=1')


def delete_view(request):
    product = Product.objects.get(id=1)
    product.delete()
    return HttpResponse('刪除 id=1 的資料成功，請到 SQL shell 下指令\nsql> select * from product')
