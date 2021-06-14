from django.core import exceptions
from django.utils import html
from .models import ContactForm
from django.shortcuts import render, redirect


from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt








# Create your views here.


@csrf_exempt
def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		subject = 'Hello From Fade'
		context = {'message':message, 'name':name,'email':email }
		html_message =render_to_string('backend/email-template.html', context)
		plain_message = strip_tags(html_message)
		from_email = settings.FROM_HOST
		send =  mail.send_mail(subject, plain_message, from_email, ['arebine@gmail.com',], html_message=html_message, fail_silently=True)
		if send:
			messages.success(request, 'Email sent sucessfully')
		else:
			messages.error(request, 'Mail not sent')
	return render(request, 'backend/contact.html', {'messages':message},)


def order_form(request):
	return render(request, 'backend/order.html')
		
def index(request):
    return render(request, 'backend/index.html')

def product(request):
    return render(request, 'backend/product-details.html')


def contact(request):
    return render(request, 'backend/contact.html')

def about(request):
	return render(request, 'backend/about.html' )

def event(request):
    return render(request, 'backend/event.html')

