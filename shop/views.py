import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
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
