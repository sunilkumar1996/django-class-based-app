"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentView.as_view(), name='student'),
    path('teacher/', views.TeacherView.as_view(), name='teacher'),
    path('contractor/', views.ContractorView.as_view(), name='contractor'),
    path('studentedit/<int:id>/', views.EditStudentView.as_view(), name='studentedit'),
    path('studentdelete/<int:id>/', views.DeleteStudentView.as_view(), name='studentdelete'),
    path('teacheredit/<int:id>/', views.EditTeacherView.as_view(), name='teacheredit'),
    path('teacherdelete/<int:id>/', views.DeleteTeacherView.as_view(), name='teacherdelete'),
    path('contractoredit/<int:id>/', views.EditContractorView.as_view(), name='contractoredit'),
    path('contractordelete/<int:id>/', views.DeleteContractorView.as_view(), name='contractordelete'),
]
