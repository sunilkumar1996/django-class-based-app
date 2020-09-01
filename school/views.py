from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentForm, TeacherForm, ContractorForm
from .models import Student, Teacher, Contractor
from django.views import View
from django.contrib import messages


# Class based View and Only Student View
class StudentView(View):
    def get(self, request):
        form = StudentForm()
        students = Student.objects.all()
        return render(request, 'school/student.html', {'form': form, 'students': students})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['name']
            student_age = form.cleaned_data['age']
            student_fees = form.cleaned_data['fees']
            student_data = Student(name=student_name, age=student_age, fees=student_fees)
            student_data.save()
            messages.success(request, 'Student Created SuccessFully !')
            return HttpResponseRedirect('/student/')

# Student Update View 
class EditStudentView(View):
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, 'school/studentedit.html', {'form': form})

    def post(self, request, id):
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Data Updated !')
            return HttpResponseRedirect('/student/')

# Class based Student delete View
class DeleteStudentView(View):
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        student.delete()
        messages.success(request, 'Student Delete Successfully !!')
        return HttpResponseRedirect('/student/')

# Class based View. This Teacher View 
class TeacherView(View):
    def get(self, request):
        form = TeacherForm()
        teachers = Teacher.objects.all()   
        return render(request, 'school/teacher.html', {'form': form, 'teachers': teachers})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher_name = form.cleaned_data['name']
            teacher_age = form.cleaned_data['age']
            teacher_date = form.cleaned_data['date']
            teacher_salary = form.cleaned_data['salary']
            teacher_data = Teacher(name=teacher_name, age=teacher_age, date=teacher_date, salary=teacher_salary)
            teacher_data.save()
            messages.success(request, 'Teacher Created SuccessFully !')
            return HttpResponseRedirect('/teacher/')


# Teacher class based Edit and Update view
class EditTeacherView(View):
    def get(self, request, id):
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(instance=teacher)
        return render(request, 'school/teacheredit.html', {'form': form})

    def post(self, request, id):
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher Updated Successfully !')
            return HttpResponseRedirect('/teacher/') 


# Teacher Class based Delete record in database 
class DeleteTeacherView(View):
    def get(self, request, id):
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
        messages.success(request, 'Deleted Successfully !!')
        return HttpResponseRedirect('/teacher/')


# Class based View. This is Contractor View 
class ContractorView(View):
    def get(self, request):
        form = ContractorForm()
        contractor = Contractor.objects.all()
        return render(request, 'school/contractor.html', {'form': form, 'contractors': contractor})

    def post(self, request):
        form = ContractorForm(request.POST)
        if form.is_valid():
            c_name = form.cleaned_data['name']
            c_age = form.cleaned_data['age']
            c_date = form.cleaned_data['date']
            c_payment = form.cleaned_data['payment']
            c_data = Contractor(name=c_name, age=c_age, date=c_date, payment=c_payment)
            c_data.save()
            messages.success(request, 'Contractor Created SuccessFully !')
            return HttpResponseRedirect('/contractor/')


# Contractor Edit and update class based view
class EditContractorView(View):
    def get(self, request, id):
        contractor = Contractor.objects.get(pk=id)
        form = ContractorForm(instance=contractor)
        return render(request, 'school/contractoredit.html', {'form': form})

    def post(self, request, id):
        contractor = Contractor.objects.get(pk=id)
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully !!')
            return HttpResponseRedirect('/contractor/')

# Contractor delete class based view
class DeleteContractorView(View):
    def get(self, request, id):
        data = Contractor.objects.get(pk=id)
        data.delete()
        messages.success(request, 'Deleted Successfully !!')
        return HttpResponseRedirect('/contractor/')
