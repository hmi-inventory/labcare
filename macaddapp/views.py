from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_protect
import secrets
from .models import *
from json import dumps

#rest api
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@csrf_protect
def home(request):
	# data = list(ftp.objects.values_list('	',flat=True).distinct())
	data1 = list(register.objects.values_list('name',flat=True))
	if request.method == 'POST':
		try:
			mac = request.POST['mac']
			username = request.POST['username']
			cname = request.POST['cname']
			security_key = secrets.token_hex(8)
			f = ftp(mac=mac, username=username,companyname=cname, security_key=security_key)
			f.save()
			return JsonResponse({"result":"success"},safe=False)
		except Exception as e:
			print(e)
			return JsonResponse({"result":"failed"},safe=False)
	else:
		return render(request,'ftp.html',{"data1":data1})


cname=""
@csrf_protect
def mac_list(request):
	data=""
	if request.method == "POST":
		cname = request.POST['cname']
		companynames = list(ftp.objects.values_list('companyname',flat=True).distinct())
		if cname in companynames:
			data = list(ftp.objects.filter(companyname = cname).values_list('mac',flat=True))
			return JsonResponse({"data":data},safe=False)
	return JsonResponse({"data":data},safe=False)

@csrf_protect
def registration(request):
	data = list(register.objects.values_list('name',flat=True))
	data1 = list(register.objects.values_list('email',flat=True))
	if request.method == "POST":
		try:
			name=request.POST['name']
			email=request.POST['email']
			username=request.POST['username']
			password=request.POST['password']
			phone=request.POST['phone']
			if phone=="":
				phone=0
			address=request.POST['address']
			r = register(name=name,email=email,username=username,password=password,phone=phone,address=address)
			r.save()
			return JsonResponse({"result":"success"},safe=False)
		except Exception as e:
			print(e)
			return JsonResponse({"result":"failed"},safe=False)
	return render(request,"register.html",context={"data":dumps(data),"data1":dumps(data1)})

@csrf_protect
def records(request):
	data = ftp.objects.all()
	return render(request,'records.html',{"data":data})

@csrf_protect
def delete_record(request,mobid):
	obj = ftp.objects.get(id=mobid)
	obj.delete()
	return redirect('ftp_records')

@csrf_protect
def recordsapi(request):
	data = ftp.objects.all()
	records=[]
	for d in data:
		data_id=d.id
		mac=d.mac
		data_security_key=d.security_key
		sdata={
			"id": data_id,
			"mac": mac,
			"security_key": data_security_key
		}
		records.append(sdata)
	return JsonResponse(records,safe=False)


#get Company Name using rest api
@api_view(['GET'])
def getCompanyName(request):
	if request.method == 'GET':
		queryset = False
		companyname = request.query_params.get("company_name")
		queryset = ftp.objects.filter(companyname=companyname).exists()
		print(queryset)
		return Response({"exists":queryset}, status=status.HTTP_201_CREATED)