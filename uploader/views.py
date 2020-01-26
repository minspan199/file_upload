import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import FileManagement
from .forms import ApplicantForm, ApplicantFiles
from .functions.functions import handle_uploaded_file, create_new_applicant_model, get_all_applicant

#
# def index(request):
#     return render(request, 'uploader/index.html')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class IndexView(TemplateView):
    # template_name = os.path.join(BASE_DIR, 'templates/uploader/index.html')
    template_name = 'uploader/index.html'


def index(request):
    if request.method == 'POST':
        print(request.POST)

        if 'submit' in request.POST:
            form = ApplicantFiles(request.POST, request.FILES)
            print(request.POST.get('name', ''))
            if form.is_valid():
                # file is saved
                print(request.FILES)
                handle_uploaded_file(request.FILES['file_1'])
                create_new_applicant_model(request)
                return render(request, 'uploader/index.html', {'form': form})
            else:
                print('form is not valid')
    return render(request, 'uploader/index.html')


def database(request):
    existed_applicant = get_all_applicant()
    return render(request, 'uploader/datalist.html', {'applicants': existed_applicant})
