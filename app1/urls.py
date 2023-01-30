from django.urls import path
from . import views
app_name='app1'
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('showusers',views.showusers,name='showusers'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logout',views.logout,name='logout'),
    path('uploadimage',views.uploadimage,name='uploadimage'),
    path('showimage',views.showimage,name='showimage'),

]