from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'POST':
        session_Id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phoneNumber = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        if text == '':
            response = "CON What would you want to check \n"
            # response .= "1. My Account \n"
            response = "1. My Phone Number \n"

        elif text == "1":
            response = "END My Phone number is 07034366179"

        print(response)