from django.urls import path
from .views import CreateUserView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
path('notes/', views.NoteListCreate.as_view(), name='note-list'),
path('notes/<int:pk>/', views.NoteDelete.as_view(), name='delete-note'),

#     path('user/register/', CreateUserView.as_view(), name='register'),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
