from django.conf import settings
from django.conf.urls import url
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('Student_account', StudentAccountView.as_view(), name='Student_account'),
    path('Manager_account', ManagerAccountView.as_view(), name='Manager_account'),

    path('login', LoginView.as_view(), name='login'),
    path('add_user', views.add_user, name='add_user'),
    path('add_student', views.add_student, name='add_student'),
    path('students_list', Students_ListView.as_view(), name='students_list'),
    path('students_list/<int:pk>', StudentDetailView.as_view(), name='student_detail'),
    path('students_list/<int:pk>/update', StudentUpdateView.as_view(), name='student_update'),
    path('students_list/<int:pk>/delete', StudentDeletView.as_view(), name='student_delete'),
    path('timetable_list', Timetable_ListView.as_view(), name='timetable_list'),
    path('teachers_list', Teachers_ListView.as_view(), name='teachers_list'),
    path('visits_list', Visits_ListView.as_view(), name='visits_list'),
    path('subscription_list', Subscription_ListView.as_view(), name='subscription_list'),
    path('student_account', StudentAcc_ListView.as_view(), name='student_account'),
    path('subscription', SubscriptionStudent_ListView.as_view(), name='subscription'),
    path('logout', views.logout, name='logout'),
    path('student_timetable', TimetableStudent_ListView.as_view(), name='student_timetable'),
    path('add_timetable', views.add_timetable, name='add_timetable'),
    path('add_subscription', views.add_subscription, name='add_subscription'),




]
