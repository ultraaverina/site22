from datetime import datetime

from django.db.models import Q

from main1.models import User11, Subscription, Student, Visit


def autoriz(login, password):
    users = User11.objects.filter(login=login, password=password)
    return users

def sort_id(sort):
    if sort == 'sub':
        users = Visit.objects.filter().order_by('subscription_id')
    elif sort == 'contractDate':
        users =Visit.objects.filter(dateExecution__gte=datetime.datetime.now().date()).order_by('schedule_id')
    elif sort == 'circulation':
        users = Visit.objects.filter(dateExecution__gte=datetime.datetime.now().date()).order_by('student_id')
    else:
        users = Visit.objects.filter(dateExecution__gte=datetime.datetime.now().date()).order_by('id')
    return users


def searchDate(word):
    searchs = Subscription.objects.filter(Q(contractDate=word)| Q(dateExecution=word))
    return searchs

def get_students():
    st = Student.objects.all()
    return st