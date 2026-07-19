from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Built in Django admin panel
    path('admin/', admin.site.urls),

    # Any URL starting with api/auth/ gets handled by accounts/urls.py This is where our register/ endpoint lives (api/auth/register/)
    
    path('api/auth/', include('accounts.urls')),

    # Login endpoint takes username and  password returns an access token and a refresh token from SimpleJWT
    
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Takes a valid refresh token returns a new access token  once the old access token has expired
    
    path('api/auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]