from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupView, LoginView, EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
