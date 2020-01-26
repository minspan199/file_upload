from ..models import FileManagement


def handle_uploaded_file(f):
    with open('uploader/static/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def create_new_applicant_model(request):
    name = request.POST.get('name', '')
    gender = request.POST.get('gender', '')
    email = request.POST.get('email', '')
    file_1 = request.FILES['file_1']
    applicant = FileManagement(email=email, gender=gender, name=name, file_1=file_1)
    existed_applicant = FileManagement.objects.filter(email=email, gender=gender, name=name).first()
    print(existed_applicant)
    if existed_applicant:
        applicant.pk = existed_applicant.pk
        applicant.save(force_update=True)
    else:
        applicant.save(force_insert=True)


def get_all_applicant():

    existed_applicant = FileManagement.objects.all()
    print(existed_applicant)
    return existed_applicant

