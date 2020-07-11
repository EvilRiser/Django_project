from django.shortcuts import render

from django.http import HttpResponse


posts = [
	{
		'author': 'CoreyMs',
		'title': 'Blog Post 1',
		'content': 'First Post content',
		'date_posted': 'July 11,2020'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second Post content',
		'date_posted': 'July 12,2020'
	}



]


# Create your views here.
def home(request):
	context = {
		'posts': posts

	}
	# return HttpResponse('<h1> Blog Home</h1>')
	return render(request,'blog/home.html',context)

def about(request):
	# return HttpResponse('<h1> Blog About</h1>')
	return render(request,'blog/about.html',{'title':'About'})
