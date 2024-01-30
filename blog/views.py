from django.shortcuts import render


# Create your views here.
contex = {
    'name': 'Asrin Vakili',
    'time': '1/30/2024',
    'view': '2.3M Views',
    'comment': '13 Comments'
}
def blog(request):
    return render(request, 'blog/blog.html', contex)


def single_blog(request):
    return render(request, 'blog/single-blog.html', contex)
