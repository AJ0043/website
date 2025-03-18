from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from Mywebapp.models import Contact
from django.shortcuts import render
from django.http import JsonResponse
from .models import PythonTopic
import json
import io
import contextlib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404


# Create your views here.

def Home(request):
    return render(request,"Home.html")

def Pro(request):
    return render(request,"pro.html")

@login_required(login_url='Login')
def Ecom(request):
    return render(request,"Ecom.html")

@login_required(login_url='Login')
def App(request):
    return render(request,"App.html")

def Service(request):
    return render(request,"Service.html")

@login_required(login_url='Login')
def Ecom(request):
    return render(request,"Ecom.html")

@login_required(login_url='Login')
def webd(request):
    return render(request,"Webd.html")

@login_required(login_url='Login')
def Host(request):
    return render(request,"Host.html")

@login_required(login_url='Login')
def Digital(request):
    return render(request,"Digital.html")

@login_required(login_url='Login')
def Develop(request):
    return render(request,"Develop.html")

@login_required(login_url='Login')
def Test(request):
    return render(request,"Test.html")



@login_required(login_url='Login')
def SEO(request):
    return render(request,"SEO.html")



@login_required(login_url='Login')
def Hosting(request):
    return render(request,"Domain.html")




@login_required(login_url='Login')
def Learning(request):
    return render(request,"Learn.html")


@login_required(login_url='Login')
def Program(request):
    return render(request,"Program.html")


@login_required(login_url='Login')
def Project(request):
    return render(request,"Project.html")


def About(request):
    return render(request,"About.html")


def Blog(request):
    return render(request,"Blog.html")





def Blog1(request):
    return render(request,"blog1.html")


def Blog2(request):
    return render(request,"blog2.html")


def Blog3(request):
    return render(request,"blog3.html")



def Blog4(request):
    return render(request,"blog4.html")


@login_required(login_url='Login')
@csrf_exempt    
def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        business = request.POST['business']
        service = request.POST['service']
        message = request.POST['message']
        
        # Create a new contact instance and save it to the database
        contact = Contact(Name=name, Email=email, Phone=phone, Business=business, Service=service, Message=message)
        contact.save()

        return redirect('success')    
    return render(request, 'Contact.html')

def Ragister(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Email = request.POST.get('email')
        pass1 = request.POST.get('Password1')
        pass2 = request.POST.get('Password2')

        if not (name and Email and pass1 and pass2):
            return HttpResponse("All fields are required!")
        
        if pass1 != pass2:
            return redirect('notmatch')
        
        my_user = User.objects.create_user(name,Email,pass1)
        my_user.save()    
        return redirect("Login")
   
   
    return render(request, "Ragister.html")



@csrf_exempt
def Login(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('log')

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('wrong')

    return render(request, 'Login.html')



@csrf_exempt
def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("home")


def Password(request):
    return render(request,'pass.html')

def Incorrect(request):
    return render(request,'wrong.html')


def Send(request):
    return render(request,'Send Message.html')

def already(request):
    return render(request,'already.html')




######## Dashboard $$$$$$$##########
def Dash(request):
    return render(request,'DASH1.html')



def python_dashboard(request):
    topics = PythonTopic.objects.all()
    return render(request, 'dashboard.html', {'topics': topics})

def get_content(request, topic_id):
    topic = get_object_or_404(PythonTopic, id=topic_id)
    return JsonResponse({
        'title': topic.title,
        'subtitle': topic.subtitle,
        'content1': topic.content1,
        'content2': topic.content2,
        'content3': topic.content3,
        'content4': topic.content4,
    })








@csrf_exempt  # Disable CSRF protection (use only if necessary)
def run_code(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            code = data.get("code", "")

            if not code.strip():
                return JsonResponse({"output": "Error: No code provided."})

            # Redirect stdout and stderr to capture output/errors
            output_buffer = io.StringIO()
            error_buffer = io.StringIO()
            
            try:
                with contextlib.redirect_stdout(output_buffer), contextlib.redirect_stderr(error_buffer):
                    exec(code, {"__builtins__": {"print": print}}, {})  # Allow print()

                output = output_buffer.getvalue()
                error_output = error_buffer.getvalue()

                return JsonResponse({"output": output if output.strip() else error_output.strip()})

            except Exception as e:
                print(f"Execution Error: {str(e)}")  # Log error in Django console
                return JsonResponse({"output": f"Runtime Error: {str(e)}"})

        except json.JSONDecodeError:
            return JsonResponse({"output": "Error: Invalid JSON format."})

        except Exception as e:
            print(f"Server Error: {str(e)}")  # Log error in Django console
            return JsonResponse({"output": f"Error: {str(e)}"})

    return JsonResponse({"output": "Invalid request method. Use POST."})





############## Dashbord $########


def python_dashboard(request):
    topics = PythonTopic.objects.all()
    return render(request, 'dashboard.html', {'topics': topics})


def get_content(request, topic_id):
    topic = get_object_or_404(PythonTopic, id=topic_id)
    return JsonResponse({
        'title': topic.title,
        'subtitle': topic.subtitle,
        'content1': topic.content1,
        'content2': topic.content2,
        'content3': topic.content3,
        'content4': topic.content4,
    })
