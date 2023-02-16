from django.shortcuts import render
import include
# Create your views here.
task = ["foo", "bar", "baz"]
def index(request):
    return render(request, "task/index.html", {
        "task":task
    })