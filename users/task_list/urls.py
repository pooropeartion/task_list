from django.urls import path

from .views import UserRegistrationView, UserLoginView, Tasks, Tasks_get_update_delete, Create_Tasks, login, registartion, task_data, list_data

urlpatterns = [
    path('register/api/posts', UserRegistrationView.as_view(), name='register'),
    path('login/api/posts/', UserLoginView.as_view()),
    path('login/', login, name='login'),
    path('registartion/', registartion, name='registartion'),
    path('task_data/', task_data, name='task_data'),
    path('list_data', list_data, name='list_data'),
    path('api/Tasks', Tasks.as_view(), name='post'),
    path('api/Task', Create_Tasks.as_view(), name='post'),
    path('get/api/Tasks/<int:id>', Tasks_get_update_delete.as_view(), name='post'),
    path('put/api/Tasks/<int:id>', Tasks_get_update_delete.as_view(), name='post'),
    path('delete/api/Tasks/<int:id>', Tasks_get_update_delete.as_view(), name='post'),

]