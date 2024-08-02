from django.shortcuts import render, redirect
from .models import Poll, Comment
from .forms import PollForm, CommentForm

# Create your views here.
def index(request):
    polls = Poll.objects.all()

    context = {
        'polls' : polls,
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save()
            return redirect('/index/')
    else:
        form = PollForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'form.html', context)

def detail(request, id):

    poll = Poll.objects.get(id=id)
    form = CommentForm()

    context = {
        'poll' : poll,
        'form' : form,

    }

    return render(request, 'detail.html', context)

def comment_create(request, poll_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.poll_id = poll_id
            comment.save()

            return redirect('/detail/', id=poll_id)

    else:
        return redirect('/index/')
