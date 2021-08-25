from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    # ---------------------------------PROJECTS---------------------------------------------------------
    path('projects/', views.projects_index, name='projects_index'),
    path('projects/<int:project_id>/', views.projects_detail, name='projects_detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    # ------------------------------------ALUMNI------------------------------------------------------
    path('alumnus/create/', views.AlumnusCreate.as_view(), name='alumnus_create'),
    path('alumnus', views.AlumnusList.as_view(), name='alumnus_index'),
    path('alumnus/<int:pk>/', views.AlumnusDetail.as_view(), name='alumnus_detail')


]
