from timeit import default_timer
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
    # print("path:", request.path)
    # print("method:", request.method)
    # print("headers:", request.headers)
    # return HttpResponse('<h1>Hello products!</h1>')
    products = [
        ("milk", 109),
        ("bread", 120),
        ("eggs", 130),
        ("coffee", 200)
    ]

    context = {
        'time_running': default_timer(),
        "products": products,
    }
    return render(request,
                  template_name='products/index.html',
                  context=context)
