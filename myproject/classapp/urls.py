from django.urls import path
from . import views
from .views import ThreadListView, ThreadDetailView, CreateThreadView, CreatePostView

#Define the list of urls patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('white/', views.white, name='white'),
    path('threads/', ThreadListView.as_view(), name='thread_list'),     	                # URL for listing all threads
    path('<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),                    # URL for viewing a specific thread
    path('create/', CreateThreadView.as_view(), name='create_thread'),                      # URL for creating a new thread
    path('<int:pk>/post/', CreatePostView.as_view(), name='create_post'),                   # URL for creating a post in a thread
    path('create-zoom-meeting/', views.create_zoom_meeting, name='create_zoom_meeting'),    # URL for creating a class
    path('post/', views.create_post, name='create_post'),                                   # URL for attend page
    path('attend/', views.attend, name='attend'),
]
