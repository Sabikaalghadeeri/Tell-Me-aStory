from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import OwnStory, StoryTitle
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from PyPDF2 import PdfReader
from gtts import gTTS

# Define a view function that responds to the browser's HTTP request by sending a string
# using HttpResponse() to send back a string of HTML, like using Express ---> res.send()


class OwnStoryUpdate(LoginRequiredMixin, UpdateView):
  model = OwnStory
  fields = ['title','story', 'published_date']
   
class OwnStoryDelete(LoginRequiredMixin, DeleteView):
  model = OwnStory
  success_url = '/ownstory/'

class OwnStoryCreate(LoginRequiredMixin, CreateView):
  model = OwnStory
  fields = '__all__'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  #or for specific data ----> fields = ['name', 'breed', 'description', 'age']
  success_url = '/ownstory/'
  
@login_required
def ownstory_detail(request, ownstory_id):
  my_Story = OwnStory.objects.get(id = ownstory_id)
  return render (request, 'detail.html', {'ownstory': my_Story})
    

@login_required
def ownstory_index(request):
  my_List = OwnStory.objects.filter(user=request.user)
  # print (list(my_List))
  # return HttpResponse(my_List)
  return render(request, 'ownstory/ownstory_index.html', {'myList': my_List})

 
 
def home(request):
    # we must import HttpResponse appove, like the others
  return HttpResponse('<h1>Story Night!!</h1>')

def about(request):
#   return HttpResponse("<h1>Stories with audio! isn't that COOL!!!</h1>")
    return render(request,'about.html')

@login_required 
def favorite_index(request):
  return render(request, 'favorite/index.html', { 'favorite': favorite })

def allstories(request):
  all_stories = StoryTitle.objects.all()
  return render(request,'allstories.html', {'allstories': all_stories})
  
class StoryTitleList(ListView):
  model = StoryTitle

class StoryTitleDetail(DetailView):
  model = StoryTitle

class StoryTitleCreate(CreateView):
  model = StoryTitle
  fields = '__all__'

class StoryTitleDelete(DeleteView):
  model = StoryTitle
  success_url = '/StoryTitles/'
  
@login_required
def listen(request, story_title):
    reader = PdfReader(f'{story_title}.pdf')
    number_of_pages = len(reader.pages)
    page = reader.pages[5]
    # print(list(reader.pages[5]))
    text = page.extract_text()
    # print(str(text))

    book = ""

    for p in reader.pages:
      page = p.extract_text()
      # print(str(page))
      book += str(page)

    print(book)

    tts = gTTS(book)
    tts.save(f'main_app/static/{story_title}.mp3')
    story_title = f'{story_title}.mp3'
    
    return render(request, 'listen_story.html', {'story_title': story_title, 'book': book} )
  
  
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/about')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)