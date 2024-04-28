from django.urls import path
from .views import CreateShortUrlView, RedirectView

urlpatterns = [
    path('create/', CreateShortUrlView.as_view(), name='create_short_url'),
    path('<str:short_key>/', RedirectView.as_view(), name='redirect'),
]
