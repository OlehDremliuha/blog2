from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.getIndex, name="main"),
    path('login/', views.getLogin, name="login"),
    path('logup/', views.getLogup, name="logup"),
    path('logout/', views.getLogout, name="logout"),
    path('createPost/', views.createPost, name="createpost"),
    path('post/<int:pk>/', views.postView, name="article"),
    path('addComment/', views.addComment, name="addComment"),
    path('profile/<int:id>', views.getProfile, name="profile"),
    path('profile/<int:id>/edit/', views.editProfile, name="edit"),
    path('post/delete/<int:id>', views.deletePost, name="deletePost"),
    path('profile/<int:id>/edit/avatar', views.changeAvatar, name="changeAvatar"),
    path('profile/<int:id>/edit/bio', views.changeBio, name="changeBio"),


    # Reset password path
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]