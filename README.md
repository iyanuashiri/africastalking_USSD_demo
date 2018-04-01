# How to Build a USSD App Using Python and Django


## Introduction

This tutorial will guide you on how to build your first USSD app. 

### Tools used

* Python 3
* Django 1.11 - The Web framework for perfectionist with deadlines
* Virtualenv
* Ngrok
* Africastalking API



First of all, we need to create a Virtual environment using a tool known as virtualenv. 
It is highly recommended and best practice to create a virtual environment before you begin 
any Python project. Virtualenv isolates your Python set-up on a per-project basis. This means 
that changes made to one Python project won’t affect another Python project. 

## Setting up virtualenv

### On a Windows, Linux or OS X

```commandline
mkdir africastalking_demo
cd africastalking_demo
```



The next step is to make our virtual environment. This will be called environment. Make sure the
 names you choose for your virtualenv is in lower case with no special characters and spaces. 

```commandline
python3 -m venv environment
```

## Working with Virtual environment

### Windows

Enter the africastalking_demo directory 

```commandline
cd  africastalking_demo
```

Activate the virtual environment

```commandline
environment\Scripts\activate
```

### Linux and OS X

Enter the africastalking_demo directory

```commandline
cd africastalking_demo
```

Activate the virtual environment

```commandline
source environment/bin/activate
```

You will know that you have virtualenv started when you see that the prompt in your console is 
prefixed with (environment)

Then enter into the environment directory

```commandline
cd environment
```

To install pip Use 

```commandline
sudo easy_install pip 
```

In the environment directory with the virtual environment already activated, you can now install 
django

```commandline
pip install django~=1.11
```

After the installation of django, you will need to create a django project

```commandline
django-admin startproject africastalking_project . 
``` 
Take note of the dot after africastalking_project


At this juncture, you can open the africastalking_project in your Text editor

You should see the following files:

* ```manage.py```
* ```settings.py```
* ```urls.py```


This shows that the project was successfully created.

In the ```settings.py```  file, add the following 

```djangotemplate
STATIC_ROOT = os.path.join(BASE_DIR, ‘static’)
```


## Creating an application

In the command line

```commandline
python manage.py startapp demo      
```  
```demo``` is the name of our application. This name is different from the project name

In the ```settings.py``` file, you should see something like this;


```djangotemplate
INSTALLED_APPS = [
this is not empty
]
```


Add ```‘demo’``` to the list of apps found in INSTALLED_APPS

```djangotemplate
INSTALLED_APPS = [
‘demo’
]
```

In your Text editor, you should see the demo folder. It has the following files

* ```admin.py```
* ```apps.py```
* ```models.py```
* ```tests.py```
* ```views.py```

Type out the code below into views.py

```python
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.



@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON What would you want to check \n"
            # response .= "1. My Account \n"
            response += "1. My Phone Number"

        elif text == "1":
            response = "END My Phone number is {0}".format(phone_number)

        return HttpResponse(response)
```


Let me explain the code above.

You need to define the function that will receive the call from your service code. 

We are calling this function ```index```. As in all views functions, the index function will have 
a ```request``` argument.

The first line of code in our function is ```if request.method == ‘POST’```. This line tells 
python that if a POST is sent to the server, it should do the lines of code that follow. 

Normally, you receive a ```POST``` from the frontend, when a form is filled by a user. 
But in the case of the USSD API, the ```POST``` information is sent directly to the 
server whenever a user dials the service code.

The next four lines are variables and we pass the information sent from the USSD API after a user 
must have dialed the service code. 

The ```response``` variable is created with an empty string. The ```if...elif``` statements 
followed is what Africastalking recommends and that is how the response screen will appear to 
the user. 

The  line ```if text == " ":```  means that the user has not sent any request after dialing 
the USSD code. The ```response = 'CON What would you want to check``` line contains a response 
variable with a string that begins with *CON*. This is the first message that appears on 
a User's screen immediately after dialing a USSD code.

According to Africastalking, the first response variable in either a ```if``` statement 
or an ```elif``` statement must begin with CON. Hence for every ```if...elif``` statement,
the first ```response``` variable will have a string that begins with CON. The 
```response += "1. My Phone Number" ``` line is the first option that a user can reply with. 
In this case, we have just one option which is *1*. We can have as many options as possible.

The ```elif text == "1":``` line means that if a user replies with *1*, do the following. The line
```response ="END My phone number is {0}".format(phoneNumber)``` is the message that appears on a
User screen since the User replied with *1*. The *END* in the string means that's the last message
that should after which the connection will the terminated. We have to return a response in our function
which is why we have the ```return HttpResponse(response)``` line. The built-in Django function
```HttpResponse``` allows a view function to return a response. This function is imported in
```from django.http import HttpResponse```. There is one last import that we have to do which is
```from django.views.decorators.csrf import csrf_exempt```. We have to decorate our view function
otherwise an error will be returned by Django. According to Django, every POST request must have 
```{% csrf_token %}``` on the form.But since our POST request is not from a form we have to
explicitly inform Django to exempt this particular views function. This is why our function is 
decorated with ```@csrf_exempt``` . 


## Create an Africastalking account

Navigate to [Africastalking](http://africastalking.com) site and create an account. Login to your newly created account.

Create an app and you should see something like the image below.

![First image](/Articles/africa.png)

Click on **Go to Sandbox app**. The next page is similar to the image below.

![Second image](africa2.png)

Click on **Create channel** This will take you to a page where you will create your own USSD service
code. You will also be required to provide a callback url, but for the sake of this tutorial, we will
make use of Ngrok. Ngrok is basically a software that provides a public url for accessing our
local host. It listens from the same port that your local server is running on. 


## Install and Use Ngrok

Download ngrok zip file, unzip the file and move it to ```/usr/local/bin``` PATH. 

Run ngrok in the terminal using the following command.

```commandline
ngrok http 8000
```
The default port for Django is ```8000```, which is what we have used. 

Running ngrok takes you to a page where you can copy the generated public url. This url changes 
every time we run run ngrok.
 

## Starting and Setting up the USSD App


Go to our Django project and locate the settings.py file. Paste the url inside the square brackets
```djangotemplate
ALLOWED_HOSTS = [ ]
``` 

Run the Django server using the following command after you must have activated the virtual 
environment where the africastalking_demo project is located.

```commandline
python manage.py runserver
```

Also Go ahead to Africastalking, the **Create a channel** page and fill in your ngrok public url.

Click on **Launch simulator** to test your new USSD app. 

Congratulations you just created your first USSD app.


You can follow me on **Twitter**: @IyanuAshiri. You can also star this project on **GitHub**.