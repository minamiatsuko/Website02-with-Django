from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm

# Create your views here.
def home(request):
    context = {"name": 'Nan', 'from':'Django'}
    return render(request, "home.html", context)

def about(request):
     context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my about (/about)")
     return render(request, "about.html", context)

def skills(request):
     context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my about (/about)")
     return render(request, "skills.html", context)

def projects(request):
    context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my project (/project)")
    return render(request, "projects.html", context)

def anime(request):
    context = {"name": 'Nan', 'from':'Django'}
    # return HttpResponse("This is my project (/project)")
    return render(request, "anime.html", context)

# def contact(request):
#     context = {"name": 'Nan', 'from':'Django'}
#     # return HttpResponse("This is my contact (/contact)")
#     return render(request, "contact.html", context)


# コンタクトフォーム

class ContactFormView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context