from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Golfer, GolfCourse
from .forms import AddGolferForm, AddGolfCourseForm

# Create your views here.
def index(request):
  '''View function for home page.'''
  num_golfers = Golfer.objects.all().count()
  num_golfers2 = Golfer.objects.all()
  num_courses = GolfCourse.objects.all().count()
  ctx = {
    'num_golfers' : num_golfers,
    'num_golfers2' : num_golfers2,
    'num_courses' : num_courses }
  
  return render(request, 'golf/index.html', context=ctx)

def golferlist(request):
  '''View function for golfer list.'''
  golfers = Golfer.objects.all()
  num_golfers2 = Golfer.objects.all()
  ctx = {

    'num_golfers2' : num_golfers2,
    'golfers' : golfers

  }
  return render(request, 'golf/golferlist.html', context=ctx)

def courselist(request):
  '''View function for course list.'''
  courses = GolfCourse.objects.all()
  num_golfers2 = Golfer.objects.all()
  ctx = {
    'courses' : courses,
    'num_golfers2' : num_golfers2,
  }
  return render(request, 'golf/courselist.html', context=ctx)

def golferdetails(request, gid):
  '''View function for golfer details.'''
  golfer = Golfer.objects.get(id=gid)
  num_golfers2 = Golfer.objects.all()
  ctx = {
    'golfer' : golfer,
    'num_golfers2' : num_golfers2,
  }
  return render(request, 'golf/golferdetails.html', context=ctx)

def coursedetails(request, cid):
  '''View function for course details.'''
  course = GolfCourse.objects.get(id=cid)
  num_golfers2 = Golfer.objects.all()
  ctx = {
    'course' : course,
    'num_golfers2' : num_golfers2,
  }
  return render(request, 'golf/coursedetails.html', context=ctx)

@csrf_exempt
def addgolfer(request):
  '''View function for add golfer form.'''
  num_golfers2 = Golfer.objects.all()
  if request.method == 'POST':
    form = AddGolferForm(request.POST,request.FILES)

    if form.is_valid():
      golfer = Golfer(
        forename = form.cleaned_data['forename'],
        surname = form.cleaned_data['surname'],
        handicap = form.cleaned_data['handicap'],
        profile_pic = form.cleaned_data['profile_image'],
        )
      golfer.save()
      messages.success(request, "Added {}".format(golfer))
      return HttpResponseRedirect(reverse('golferlist'))
  else:
    form = AddGolferForm()

  context = {
    'form' : form,
    'num_golfers2' : num_golfers2,
    
  }

  return render(request, 'golf/addgolfer.html', context)

@csrf_exempt
def addgolfcourse(request):
  '''View function for add golf course form.'''
  if request.method == 'POST':
    form = AddGolfCourseForm(request.POST)

    if form.is_valid():
      course = GolfCourse(
        name = form.cleaned_data['name'],
        latitude = form.cleaned_data['latitude'],
        longitude = form.cleaned_data['longitude'])
      course.save()
      messages.success(request, "Added {}".format(course))
      return HttpResponseRedirect(reverse('courselist'))
  else:
    num_golfers2 = Golfer.objects.all()
    form = AddGolfCourseForm()

  context = {
    'form' : form,
    'num_golfers2' : num_golfers2,
  }

  return render(request, 'golf/addgolfcourse.html', context)
