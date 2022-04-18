from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from . import user

def Login(request):
	if request.method == 'POST':
		userid = request.POST.get('userid')
		password = request.POST.get('password')
		checkout = request.POST.get('checkout') # 継続ログイン
		if user.existUser(userid):
			if user.challenge(userid, password):
				context = {
					'message': '<div class="alert alert-success" role="alert">ログインに成功しました。ようこそ ' + str(user.loadUserjson(userid)['fullname']) + ' さん！</div>',
				}
				template = 'index.html'
				if checkout == 'on':
					age = 60 * 60 * 24 * 7 # 7 days
				else:
					age = 60 * 60 * 3 # 3 hours
				response = render(request, template, context)
				response.set_cookie('userid', userid, max_age = age)
				response.set_cookie('password', password, max_age = age)
				return response
			else:
				template = 'login.html'
				context = {
					'message': '<div class="alert alert-danger" role="alert">password is not correct</div>',
				}
				response = render(request, template, context)
				return response
		else:
			template = 'login.html'
			context = {
				'message': '<div class="alert alert-danger" role="alert">user is not found</div>',
			}
			response = render(request, template, context)
			return response
	# GET
	else:
		return render(request, 'login.html')

def Logout(request):
	redirect_url = reverse('index')
	parameters = urlencode({'ll': 1})
	url = f'{redirect_url}?{parameters}'
	response = redirect(url)
	response.delete_cookie('userid')
	response.delete_cookie('password')
	return response

def index(request):
	logout = request.GET.get('ll')
	msg = ''
	if logout:
		msg = '<div class="alert alert-success" role="alert">ログアウトに成功しました。</div>'
	context = {
		'Logout': '/logout',
		'Login': '/login',
		'message': msg,
	}
	return render(request, 'index.html', context)