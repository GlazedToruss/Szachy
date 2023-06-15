from django.urls import path
from . import views


# URLconf
urlpatterns = [
    path("siemano/", views.hello),
    path("siemano/Maciek", views.hello_Maciek)
]