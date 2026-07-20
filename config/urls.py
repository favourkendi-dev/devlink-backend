from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import MyTokenObtainPairView

urlpatterns = [
    # built in Django admin panel
    path('admin/', admin.site.urls),

    # Any URL starting with api auth and gets handled by accounts urls.py this is where our register endpoint lives 
    
    path('api/auth/', include('accounts.urls')),

    # Login endpoint takes username and password, returns an access token and a refresh token
    # Uses our custom view so the token also includes the username
    
    path('api/auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Takes a valid refresh token returns a new access token  once the old access token has expired
    
    path('api/auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Any URL starting with api or posts and gets handled by postsurls.py

    path('api/posts/', include('posts.urls')),
]