from django.urls import path
from users.views import SignUpCreateAPIView, VerifyCodeAPIView

app_name = 'users'

urlpatterns = [
    path('register/', SignUpCreateAPIView.as_view(), name='register'),
    path('verify/', VerifyCodeAPIView.as_view(), name='verify'),
]
