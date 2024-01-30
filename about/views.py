from django.shortcuts import render


# Create your views here.
def about(request):
    contex = {
        'name': 'Asrin Vakili',
        'education': 'Master of Degree In Software Engineering',
        'bio1': 'My first name is Asrin, which is a Kurdish name, meaning tears, and my last name is Vakili, which is a common family name in my area. I am 32, married, but I have no children. I am a master\'s holder, majoring in computer engineering. I am University lecturer. I was born and grew up in a small city located in West of Iran called Saqqez.',
        'bio2': 'My favorite programming language is Python. I love working with graphic software such as Illustrator, Blender, Photoshop, and After Effects. I am just learning Django framework. I also do calligraphy and painting.',
        'bio3': 'I know many programming languages. Including Java, which I wrote my thesis with. Html and CSS to design the Front-End of website. I also teach Assembly at the university. When I was a student, I was programming with C++. '
    }
    return render(request, 'about-us.html',contex)
