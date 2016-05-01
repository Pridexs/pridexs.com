import requests
from ipware.ip import get_real_ip

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader

from .forms import EmailForm

from django.conf import settings

def index(request):
    latest_question_list = []
    template = loader.get_template('mainwebsite/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def contact(request):

    context = {
        'email_sent': False,
        'error': False,
        'captcha_success': True,

    }

    if request.method == 'POST':
        if 'submit_message' in request.POST:
            form = EmailForm(request.POST)
            if form.is_valid():
                # Check if nocaptcha is successful
                data = request.POST
                captcha_rs = data.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                params = {
                    'secret': settings.NOCAPTCHA_SECRET_KEY,
                    'response': captcha_rs,
                    'remoteip': get_real_ip(request)
                }
                verify_rs = requests.get(url, params=params, verify=True)
                verify_rs = verify_rs.json()

                senderName = form.cleaned_data['c_name']
                subject = form.cleaned_data['c_subject']
                message = form.cleaned_data['c_message']
                sender = form.cleaned_data['c_email']
                if verify_rs.get("success") == True:
                    recipients = ['contact@pridexs.com']
                    send_mail(subject, message, sender, recipients)
                    context['email_sent'] = True
                else:
                    context['senderName'] = senderName
                    context['subject'] = subject
                    context['message'] = message
                    context['sender'] = sender

                    context['captcha_success'] = False
            else:
                context['error'] = True

    template = loader.get_template('mainwebsite/contact.html')
    return HttpResponse(template.render(context, request))

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
