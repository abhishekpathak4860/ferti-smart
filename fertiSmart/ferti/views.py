from django.shortcuts import render

from .models import Fertilizer
# Create your views here.


def home(request):
    return render(request, 'pages/Home.html')


def soilAnalysis(request):
    return render(request, 'pages/soil_form.html')


def cropYield(request):
    return render(request, 'pages/cropyield.html')


def sustainability(request):
    return render(request, 'pages/sustainable.html')


def fertilizer(request):
  if request.method=="POST":#soil data posted by user
    soil_nitrogen=float(request.POST["nitrogen"])
    soil_phosphorous=float(request.POST["phosphorous"])
    soil_potassium=float(request.POST["potassium"])
    soil_depth=float(request.POST["depth"])
    soil_bulk=float(request.POST["bulk"])
    crop=request.POST["crop"]
    N=P=K=0
    match crop:#nutirent requirement of crops
        case "wheat":
            N=99.6
            P=40.2
            K=6.9
        case "paddy":
            N=81.7
            P=24.3
            K=13.1
        case "cotton":
            N=89.55
            P=39.3
            K=12.9
        case "jute":
            N=38
            P=11.5
            K=5
        case "sugarcane":
            N=124.8
            P=44
            K=38.3
        case "millet":
            N=21.9
            P=5.5
            K=.8
        case"pulses":
            N=120
            P=60
            K=80
        case _:
            N=98.9
            P=6.3
            K=20.0
    #amount of nutirents present in soil 
    newN=soil_nitrogen*soil_depth*soil_bulk/10
    #recommented nutrient=crop nutirent - new nutrient
    RN="{:.3f}".format(N-newN)
    #amount of nutirents present in soil 
    newP=soil_phosphorous*soil_depth*soil_bulk/10
      #recommented nutrient=crop nutirent - new nutrient
    RP="{:.3f}".format(P-newP)
     #amount of nutirents present in soil 
    newK=soil_potassium*soil_depth*soil_bulk/10
      #recommented nutrient=crop nutirent - new nutrient
    RK="{:.3f}".format(K-newK)
    #if rop nutrient in soil is less then crop nutrient then  need to recommend fertlizer 
    if newN<N:
        nitro=Fertilizer.objects.filter(nitrogen__gt=10)
    #else no need
    else:
        nitro=None
        RN=None
    if newP<P:
        phos=Fertilizer.objects.filter(phosphorus__gt=5)
    else:
        phos=None
    if newK<K:
         pot=Fertilizer.objects.filter(potassium__gt=10)
    else:
        pot=None
    
    return render(request,"pages/fertilizer.html",{
        "nitro":nitro,
        "RN":RN,
        "phos":phos,
        "RP":RP,
        "pot":pot,
        "RK":RK,
        "crop":crop
    })
def about(request):
    return render(request, 'pages/about.html')
