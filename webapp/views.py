from django.shortcuts import render

# Create your views here.
#create index view which displays the index.html template
def index(request):
    #render some html
    return render(request, 'index.html')
    
