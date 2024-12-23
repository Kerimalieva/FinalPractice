"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from webapp.views import PasswordResetView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/password_reset/', PasswordResetView.as_view(), name='password_reset'),

    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/posts/create/', PostCreateView.as_view(), name='post-create'),
    path('api/posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('api/posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
