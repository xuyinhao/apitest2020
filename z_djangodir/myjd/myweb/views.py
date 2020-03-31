from django.shortcuts import render
from django.http.response import HttpResponse
from myweb.my.mymth import r_code

# Create your views here.
import json
def myindex(request):
    if request.method == 'GET':
        r={}
        username=request.GET.get('username')
        password=request.GET.get('password')
        mobile = request.GET.get('mobile')
        # r = r_code(3000,moblie)
        r['username']=username
        r['mobile']=mobile
        r = json.dumps(r)
        return HttpResponse(r,content_type='application/json;charset=utf-8')
    # else:
    #     return  render(request,'index.html')

def myindex2(request):
    r={}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        mobile = request.POST.get('mobile')
        r['username']=username
        r=json.dumps(r)
        return HttpResponse(r,content_type='application/json;charset=utf-8')
    else:
        return  render(request,'index.html')

def test01(request):
    if request.method == 'POST':
        startdevid = int(request.POST.get('startdevid'))
        num = int(request.POST.get('num'))
        r=[]
        for i in range(int(startdevid),int(startdevid)+int(num)):
            r.append(i)
        rdata={"data": {"start":startdevid,"nums":num ,"totaldev": ','.join(str(i) for i in r) }, "totalnum":int(len(r))}
        # return HttpResponse(r, content_type='application/text;charset=utf-8')
        return HttpResponse(json.dumps(rdata,indent=2,ensure_ascii=False,sort_keys=False),content_type='application/json;charset=utf-8')
    else:
        return render(request, 'main.html')
    pass

def test02(request):

    if request.method == "GET" :

        getdevid = request.GET.get("devid")
        if  getdevid is None:
            return  render(request, "main2.html")
        else:
            getdevid = request.GET.get("devid")
            arr = getdevid.split(',')
            for i in arr:
                print(i)
            print(getdevid)
            rdata = {"data":{"getdevid":getdevid}}
            return HttpResponse(json.dumps(rdata,indent=2,ensure_ascii=False,sort_keys=False),content_type='application/json;charset=utf-8')
    else:
        return  render(request,"main2.html")

    pass