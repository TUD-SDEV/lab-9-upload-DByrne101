from django.urls import path
from .views import SignUpView, ProfileEditView, ProfilePageView

urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/<int:pk>/', ProfilePageView(), name='show_profile')
]