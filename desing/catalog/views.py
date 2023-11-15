from django.shortcuts import render
from django.views.generic CreateView
from django.views.generic import TemplateView


from .forms import RegisterUserForm

def index(request):
    return render(request, 'index.html')

class RegisterUserView(CreateView):
   model = AdvUser
   template_name = 'main/register_user.html'
   form_class = RegisterUserForm
   success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView):
   template_name = 'main/register_done.html'