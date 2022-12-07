from django.shortcuts import render
from django.http import HttpResponse
from .models import OwnStory, StoryTitle
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from PyPDF2 import PdfReader
from gtts import gTTS

# Define a view function that responds to the browser's HTTP request by sending a string
# using HttpResponse() to send back a string of HTML, like using Express ---> res.send()


class OwnStoryUpdate(UpdateView):
  model = OwnStory
  fields = ['title','story', 'published_date']
  
  
class OwnStoryDelete(DeleteView):
  model = OwnStory
  success_url = '/ownstory/'

  
class OwnStoryCreate(CreateView):
  model = OwnStory
  fields = '__all__' 
  #or for specific data ----> fields = ['name', 'breed', 'description', 'age']
  success_url = '/ownstory/'
  
 
def ownstory_detail(request, ownstory_id):
  my_Story = OwnStory.objects.get(id = ownstory_id)
  return render (request, 'detail.html', {'ownstory': my_Story})
    


def ownstory_index(request):
  my_List = OwnStory.objects.all()
  # print (list(my_List))
  # return HttpResponse(my_List)
  return render(request, 'ownstory/ownstory_index.html', {'myList': my_List})

 
 
def home(request):
    # we must import HttpResponse appove, like the others
  return HttpResponse('<h1>Story Night!!</h1>')

def about(request):
#   return HttpResponse("<h1>Stories with audio! isn't that COOL!!!</h1>")
    return render(request,'about.html')
  
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