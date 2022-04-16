from django.urls import path

from . import views

urlpatterns = [
    path("<companyid>/<userid>", views.InterviewAnalysis.as_view()),
]