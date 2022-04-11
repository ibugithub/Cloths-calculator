from django.shortcuts import render
from django.http import JsonResponse
from .models import ClothInfo, ShopEvent
from .forms import ShopEventForm

# Create your views here.

def clothMeasure(request):
    return render(request, 'core/clothMeasure.html')


def prevAmount(request):
    print("now it will be reserved in the memory")
    data = {}
    gozLen = request.GET['gozLenV']
    giraLen = request.GET['giraLenV']
    rate = request.GET['rateV']
    if gozLen == '':
        gozLen = 0
    if giraLen == '':
        giraLen = 0
    if rate == '':
        data['warning'] = 'rate'
    else:
        clothInfo = ClothInfo(GozLength=gozLen, GiraLength=giraLen, Rate=rate)
        clothInfo.save()
    return JsonResponse(data)

def totalInfo(request):
    clothInfos = ClothInfo.objects.all()
    sum = 0
    for clothInfo in clothInfos:
        totalPrize = (clothInfo.GozLength + (clothInfo.GiraLength / 16)) * clothInfo.Rate
        sum += totalPrize
    data = {'totalPrize': sum}
    ClothInfo.objects.all().delete()
    return JsonResponse(data)

def ShopEventView(request):
    context = {}
    form = ShopEventForm()
    context["form"] = form
    return render(request, "core/ShopEvents.html", context)