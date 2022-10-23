from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    login_view,
    logout_template_view,
    logout_view,
    accounts_view,
    password_change_view,
    reset_password_view,
    home_view,
    about_view,
    create_register,
    read_register,
    detail_register,
    update_register,
    delete_register,
    
    
)

urlpatterns = [
    path('', login_view, name='login'),#login
    path('logout_template/', logout_template_view,name='logout_template'),
    path('logout', logout_view, name='logout'),#logout
    path('accounts/', accounts_view, name='accounts'), #cadastro
    path('password_change/', password_change_view, name='password-change'),
    path('reset_password/', reset_password_view, name='reset-password'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('create/', create_register, name='create-register'),
    path('read/', read_register, name='read-register'),
    path('detail/<id>/', detail_register, name='update-register'),
    path('update/<id>/', update_register, name='update-register'),
    path('delete/<id>/', delete_register,name="delete-register"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 