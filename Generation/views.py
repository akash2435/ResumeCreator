from django.shortcuts import render

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa
# Create your views here.

def home(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'createResume.html')

def steptwo(request):
    return render(request, 'create_next2.html')

def testing(request):
    return render(request, 'testing.html') 
    template_path = 'testing.html'

    response = HttpResponse(content_type='application/pdf')
    context = {'testing' : "testing"}

    response['Content-Disposition'] = 'filename="testing.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response