from django.http import HttpResponse
from django.shortcuts import render_to_response
from reportlab.pdfgen import canvas

def index (request):
    return render_to_response('index.html')

def gerar_pdf(request):
    c = canvas.Canvas("sample.pdf")
    c.drawString(150, 200, "caneta canetinha nao")
    c.save()
    with open('sample.pdf') as pdf:
	response = HttpResponse(pdf.read(), content_type='application/pdf')
	response['Content-Disposition']= 'filename=sample.pdf'
	return response
