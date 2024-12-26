from django.shortcuts import render, redirect
from .form import InfoForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .utils.zoom_utils import createMeeting

from .models import Thread, Post


# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def index(request):
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = InfoForm()
    context = { 'form': form }
    return render(request, 'first/index.html', context)

#Define home page after login/sing in
def home(request):
    return render(request, 'first/home.html')


def white(request):
    return render(request, 'first/white.html')

#Define forum
class ThreadListView(ListView):
    model = Thread

class ThreadDetailView(DetailView):
    model = Thread

class CreateThreadView(CreateView):
    model = Thread
    fields = ['title']
    success_url = reverse_lazy('thread_list')
    
class CreatePostView(CreateView):
    model = Post
    fields = ['content']
    
    def form_valid(self, form):
        form.instance.thread_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('thread_detail', kwargs={'pk': self.kwargs['pk']})


#Define zoom meeting
def create_zoom_meeting(request):
    if request.method == "POST":
        result = createMeeting()
        if "error" in result:
            return JsonResponse({"error": result["error"]}, status=400)
        return JsonResponse({
            "message": "Meeting created successfully",
            "join_url": result["join_url"],
            "password": result["password"],
        })
    return JsonResponse({"error":"Invalid request method"}, status=405)

#NEW ONE IS HERE
def attend(request):
    return render(request, 'first/attend.html')

from django.http import JsonResponse

def create_post(request):
    if request.method == "POST":
        # Simulate meeting creation logic or implement the actual functionality
        return JsonResponse({
            "join_url": "https://zoom.us/j/123456789",
            "password": "example_password",
        })
    return JsonResponse({"error": "Invalid request"}, status=400)
