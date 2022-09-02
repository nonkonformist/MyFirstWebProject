from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_home, name='events_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.EventDetailView.as_view(), name='events-detail'),
    path('<int:pk>/update', views.EventUpdateView.as_view(), name="event-update"),
    path('<int:pk>/delete', views.EventDeleteView.as_view(), name="event-delete")
]