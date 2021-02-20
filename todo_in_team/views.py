from django.shortcuts import render


def index(request):
    """ Index page view """
    page_heading = "Django-ToDo-Team-APP"
    context = {
        'page_heading': page_heading
        }
    template = "todo_in_team/index.html"
    return render(request, template, context)
