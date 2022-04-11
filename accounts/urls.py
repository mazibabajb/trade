from django.urls import path
from .views import main_view, signup_view
from .views import my_recommendations_view
urlpatterns = [
    path('', main_view, name = 'main-view'),
    path('<str:ref_code>/', main_view, name = 'main-view'),
    path('signup_view', signup_view, name = 'signup_view'),
    path('profiles',my_recommendations_view,name = 'profiles'),
]
