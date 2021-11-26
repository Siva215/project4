from django.shortcuts import render

# Create your views here.
def second_html(request):
    return render(request,'app4/h2.html')