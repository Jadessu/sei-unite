from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.about, name='about'),
    # ----------------------------------PROJECT IDEAS-----------------------------------------------------
    path('ideas/', views.ideas, name = 'ideas'),

    # ---------------------------------PROJECTS---------------------------------------------------------
    path('projects/', views.projects_index, name='projects_index'),
    path('projects/<int:project_id>/', views.projects_detail, name='projects_detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),

    # -----------------------------------ALUMNUS PROJECTS-----------------------------------------------
    path('myprojects/', views.myprojects_index, name='myprojects_index'),

    # ------------------------------------ALUMNI------------------------------------------------------
    path('alumnus/', views.alumnus_index, name='alumnus_index'),
    path('alumnus/<int:alumnus_id>/', views.alumnus_detail, name='alumnus_detail'),
    path('alumnus/create/', views.AlumnusCreate.as_view(), name='alumnus_create'),
    path('alumnus/<int:pk>/update/', views.AlumnusUpdate.as_view(), name='alumnus_update'),
    path('alumnus/<int:pk>/delete/', views.AlumnusDelete.as_view(), name='alumnus_delete'),
    # ------------------------------------USERS------------------------------------------------------------
    path('accounts/signup/', views.signup, name='signup'),
    # -----------------------------------PHOTO--------------------------------------------------------------
    path('alumnus/<int:alumnus_id>/add_photo/', views.add_photo, name='add_photo'),
    
]
