from django.urls import path
from . import api

app_name = 'service'

urlpatterns = [
    path('register-database-connection/', api.RegisterDatabaseConnection.as_view(), name='register-database-connection'),
]
