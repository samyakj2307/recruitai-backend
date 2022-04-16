from django.urls import path

from . import views

urlpatterns = [
    path("<companyid>/<userid>", views.ResumeAnalysis.as_view()),
]