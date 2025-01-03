from django.urls import path
from . import views 
urlpatterns = [
    path('home/', views.Home, name="home"),
    path('Service/', views.Service, name="Service"),
    path('Ecom/',views.Ecom, name="Ecom"),
    path('App/',views.App, name="Application"),
    path('Ecom/',views.Ecom, name="Ecommerce"),
    path('webd/',views.webd, name="Development"),
    path('Hosting/',views.Host, name="Hosting"),
    path('Digital/',views.Digital, name="Digital Marketing"),
    path('Develop/',views.Develop, name="Maintenance"),
    path('SEO/',views.SEO, name="SEO"),
    path('Domain/',views.Hosting, name="Domain"),
    path('Learn/',views.Learning, name="Learning"),
    path('program/',views.Program, name="Program"),
    path('blog1/', views.Blog1, name='blog1'), 
    path('blog2/', views.Blog2, name='blog2'), 
    path('blog3/', views.Blog3, name='blog3'), 
    path('blog4/', views.Blog4, name='blog4'), 

    path('Test/',views.Test, name="Testimonial"),
    path('blog/',views.Blog, name="Blog"),
    path('About/',views.About, name="Abouts"),
    path('Login1/', views.Login, name="Login"),
    path('Ragister/',views.Ragister, name="Ragister"),
    path('Logout3/',views.Logout, name="logout"),
    path('NotResponse/',views.Password, name="notmatch"),
    path('Incorrect/',views.Incorrect, name="wrong"),
    path('contact/', views.contact_view, name='contactus'),
    path('SendMessage/', views.Send, name='success'),
    path('already/', views.already, name='log'),
    path('project/', views.Project, name='project'),



]