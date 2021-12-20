from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.views.generic import View, FormView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from .baza import autoriz, sort_id
from .forms import UserForm, StudentForm, SearchForm, timetableForm, subscriptionForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login



class MainPage(View):
    def get(self, request):
        data = {'hello': 'Привет мир!!!'

                }
        return render(request, 'main/index.html', data)


class LoginView(View):
    def get(self, request):
        context = {}
        return render(request, 'main/login.html', context=context)

    def post(self, request):
        entered_login = request.POST.get("login")
        entered_passw = request.POST.get("password")
        users = autoriz(entered_login, entered_passw)

        if not users:
            context = {
                "message": users
            }
            return render(request, 'login.html', context=context)
        elif users[0].privilegies == 0:
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].privilegies

            return HttpResponseRedirect('Student_account')
        else:
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].privilegies
            return HttpResponseRedirect('Manager_account')


class StudentAccountView(View):
    def get(self, request):
        user = User11.objects.filter(id=request.session["id_user"])
        user1 = Student.objects.filter(user_id=user)
        context = {'user': user1}
        return render(request, 'Student/StudentAcc.html', context=context)


class ManagerAccountView(View):
    def get(self, request):
        context = {}
        return render(request, 'Manager/ManagerAcc.html', context=context)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "main/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "account"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def add_user(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Поля заполненны не верно!'
    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'Manager/add_user.html', context=context)



class Students_ListView(View):

    def get(self, request):
        search_query = request.GET.get("q")
        if search_query==None:
            user = Student.objects.all()
        else:
            user=Student.objects.filter(
                name__contains=search_query
            )
        context = {
            'user': user
        }
        return render(request, 'Manager/students_list.html', context=context)



class StudentDetailView(DetailView):
    model = Student
    template_name = 'Manager/Student_details_view.html'
    context_object_name = 'person'




class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'Manager/add_student.html'
    form_class = StudentForm
    success_url = '/students_list'


class StudentDeletView(DeleteView):
    model = Student
    template_name = 'Manager/student_delete.html'
    form_class = StudentForm
    context_object_name = 'person'
    success_url = '/students_list'


def add_student(request):
    error = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Поля заполненны не верно!'
    form = StudentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'Manager/add_student.html', context=context)

class Timetable_ListView(View):

    def get(self, request):
        search_query = request.GET.get("q")
        if search_query==None:
            ob = Schedule.objects.all()
        else:
            ob=Schedule.objects.filter(
                date__contains=search_query
            )
        context = {
            'ob': ob
        }
        return render(request, 'Manager/timetable_list.html', context=context)
class Teachers_ListView(View):

    def get(self, request):
        search_query = request.GET.get("q")
        if search_query==None:
            ob = Educator.objects.all()
        else:
            ob=Educator.objects.filter(
                name__contains=search_query
            )
        context = {
            'person': ob
        }
        return render(request, 'Manager/teachers_list.html', context=context)
class Visits_ListView(View):
    def get(self, request):
        ob = Visit.objects.all()
        context = {'ob': ob}
        return render(request, 'Manager/visits_list.html', context=context)

    def post(self, request):
        if 'sortButton' in request.POST:
            sort = request.POST.get("Sort")
            if sort == 'sub':
                users = Visit.objects.filter(presence=True)

            context = {'ob': users}
        else:
            error = 'Поля заполненны не верно!'
            context = {
                "error": error}

        return render(request, 'Manager/visits_list.html', context=context)



class Subscription_ListView(View):
    def get(self, request):
        search_query = request.GET.get("q")
        if search_query == None:
            sub = Subscription.objects.all()
        else:
            sub = Subscription.objects.filter(
                price__contains=search_query
            )
        context = {
            'sub': sub
        }
        return render(request, 'Manager/subscription_list.html', context=context)


class StudentAcc_ListView(View):

    def get(self, request):
        user = User11.objects.get(id=request.session["id_user"])
        user1=Student.objects.filter(user_id=user)


        context = {
            'user': user1
        }
        return render(request, 'Student/student_info.html', context=context)

def logout(request):
    try:
        del request.session['id_user']
    except KeyError:
        pass
    return render(request, 'main/index.html')

class SubscriptionStudent_ListView(View):

    def get(self, request):
        user = User11.objects.get(id=request.session["id_user"])
        user1=Student.objects.filter(user_id=user)
        ab = Subscription.objects.filter(student_id=user1[0])

        ac = len(Visit.objects.filter(student_id=user1[0]))


        context = {
            'ab': ab,
            'ac': ac,

        }
        return render(request, 'Student/subscription.html', context=context)

class TimetableStudent_ListView(View):

    def get(self, request):
        ab = Schedule.objects.all()


        context = {
            'ab': ab,


        }
        return render(request, 'Student/student_timetable.html', context=context)
def add_timetable(request):
    error = ''
    if request.method == 'POST':
        form = timetableForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Поля заполненны не верно!'
    form = timetableForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'Manager/add_timetable.html', context=context)


def add_subscription(request):
    error = ''
    if request.method == 'POST':
        form = subscriptionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Поля заполненны не верно!'
    form = subscriptionForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'Manager/add_subscription.html', context=context)