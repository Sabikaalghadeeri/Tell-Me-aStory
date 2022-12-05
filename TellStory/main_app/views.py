from django.shortcuts import render

from django.http import HttpResponse

# Define a view function that responds to the browser's HTTP request by sending a string

 # using HttpResponse() to send back a string of HTML, like using Express ---> res.send()
 
def home(request):
    # we must import HttpResponse appove, like the others
  return HttpResponse('<h1>Story Night!!</h1>')

def about(request):
#   return HttpResponse("<h1>Stories with audio! isn't that COOL!!!</h1>")
    return render(request,'about.html')
  
def favorite_index(request):
  return render(request, 'favorite/index.html', { 'favorite': favorite })

def ownstory_index(request):
  return render(request, 'ownstory/index.html', { 'ownstory': ownstory })