from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),  # Include the URLs from the employees app
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh view
]