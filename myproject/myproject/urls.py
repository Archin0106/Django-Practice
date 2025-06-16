from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),  # Ensure there's a trailing slash
    path('stud/', views.stud), 
    path('emp/', views.emp),  
 

]