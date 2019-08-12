from django.shortcuts import render,redirect
import hashlib
import base64
import json
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def index(request):
    content={}
    return render(request,'student/index.html',content)
def hash(request):
    if request.method=="GET":
        return render(request,'student/hash.html')
    elif request.method=="POST":
        mingwen=request.POST["jiami"]
        print(mingwen)
        mad=hashlib.md5()
        mad.update(f"{mingwen}".encode("utf-8"))
        jiemidongxi=mad.hexdigest()
        context={
            "jiami":jiemidongxi
        }
        return render(request,"student/hash.html",context=context)


def base_64(request):
    if request.method=="GET":
        return render(request,'student/base64.html')
    elif request.method=="POST":
        mingwen=request.POST["zhuan"]
        print(mingwen)
        bytes_content=mingwen.encode(encoding='utf-8')
        jiema=base64.b64encode(bytes_content)

        context={
            'zhuan':jiema
        }
        return render(request,"student/base64.html",context=context)


def base_642(request):
    if request.method=="GET":
        return render(request,'student/base64.html')
    elif request.method=="POST":
        mingwen=request.POST["jiema"]
        print(mingwen)
        content=mingwen
        content1=base64.b64decode(content)
        content2=content1.decode()
        context={
            'jiema':content2
        }
        return render(request,"student/base64.html",context=context)


def tizhong(request):
    if request.method=='GET':
        return render(request, 'student/tizhong.html')
    elif request.method=='POST':
        a = float(request.POST.get('shengao'))
        b = float(request.POST.get('tizhong'))
        huanmi = a/100
        bmi = b/(huanmi*huanmi)
        content = {
            'bmi':bmi
        }
        if bmi < 18.5:
            content['bme'] = '太轻'
        elif 18.5 <= bmi < 23.9:
            content['bme'] = '标准身材'
        elif 24 <= bmi < 27:
            content['bme'] = '过重'
        elif 28 <= bmi < 32:
            content['bme'] = '超重'
        elif bmi>32:
            content['bme'] = '蔡徐坤了'
        return render(request, 'student/tizhong.html', content)
def yasuo(request):
    if request.method=='GET':
        context={}
        return render(request,'student/yasuo.html',context)
    elif request.method=='POST':
        context={}
        input=request.POST.get('input')
        content=input.split()
        context_list="".join(content)
        context['output']=context_list
        return render(request,'student/yasuo.html',context=context)


# 运用到 vue里面  base64编码
def vue_encode(request):
    mingwen=request.GET.get('encode','')
    print(mingwen)
    bytes_content = mingwen.encode(encoding='utf-8')
    jiema = base64.b64encode(bytes_content)
    zhuan=jiema.decode()
    print(zhuan)
    context = {
        'jiami': zhuan
    }
    context_json=json.dumps(context)
    return HttpResponse(context_json)

def vue_decode(request):
    mingwen=request.GET.get('decode','')
    print(mingwen)
    content = mingwen
    content1 = base64.b64decode(content)
    content2 = content1.decode()
    # print
    context = {
        'jiemi': content2
    }
    context_json = json.dumps(context)
    return HttpResponse(context_json)
# 运用到vue里面的 json 压缩
def vue_json(request):
    input=request.GET.get('encode','')
    print(json)
    context={}
    content=input.split()
    context_list="".join(content)
    context['yasuo']=context_list
    return HttpResponse(context)

#运用到vue里面的 bmi
def vue_bmi(request):
    height = int(request.GET.get('height'))
    weight = int(request.GET.get('weight'))
    height_m = height * 0.01 * height * 0.01
    result = weight / height_m
    result = round(result, 1)
    context = json.dumps({'msg': result})
    return HttpResponse(context)