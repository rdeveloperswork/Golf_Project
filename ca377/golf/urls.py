from django.urls import path
from . import views

urlpatterns = [
    # Every path here has a golf/ in front of it
    # The name is the name of the URL and we can use it in templates
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("golferlist/", views.golferlist, name="golferlist"),
    path("golferdetails/<int:gid>/", views.golferdetails, name="golferdetails"),
    path("courselist/", views.courselist, name="courselist"),
    path("coursedetails/<int:cid>/", views.coursedetails, name="coursedetails"),
    path("addgolfer/", views.addgolfer, name="addgolfer"),
    path("addgolfcourse/", views.addgolfcourse, name="addgolfcourse"),
]
