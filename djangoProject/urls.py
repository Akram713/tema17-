
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from service.views import my_view, project_details_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='ThesisManagement/index.html'), name='index'),
    path('project-list/', my_view, name='projectList'),
    path('project-details/<int:project_id>/', project_details_view, name='projectDetails'),
path('about-us/', TemplateView.as_view(template_name='ThesisManagement/aboutUs.html'), name='aboutUs'),
]
