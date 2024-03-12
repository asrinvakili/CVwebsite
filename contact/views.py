from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from contact.forms import contact_form, NewsLetterForm


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = 'Unknown'
            instance.save()
            messages.success(request, "Thank you for contacting us.")
        else:
            messages.error(request, "Please correct the errors.")
    else:
        form = contact_form()

    return render(request, 'contact.html', {'form': form})


def news_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Email Submitted Successfully')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'There was an error, Please try again')

