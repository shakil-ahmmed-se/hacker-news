from django.http import HttpResponse

def Home(req):
    return HttpResponse({
        "<h2>Welcome to HackerNews API -- <br/></h2>" 
        "<h4>To get the top stories, visit /api/top-stories/ <br/></h4>"
        "<h5>and to get a specific story, visit /api/stories/<id>/</h5>"
    })