from django.urls import path
from . import views
urlpatterns = [
    path('usercreate/', views.usercreate, name='usercreate'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('', views.loginpage, name='loginpage'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_posts/', views.create_posts, name='create_posts'),
    path('profile/', views.profile, name='profile'),
    path('editpro/<int:pk>', views.editpro, name='editpro'),
    path('chg_pro/<int:pk>', views.chg_pro, name='chg_pro'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('save_edit/<int:pk>', views.save_edit, name='save_edit'),
    

    
    
]
