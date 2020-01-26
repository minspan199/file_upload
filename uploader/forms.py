from django import forms


class ApplicantForm(forms.Form):
    name = forms.CharField(label="name", max_length=50)
    email = forms.EmailField(label="email")
    file_1 = forms.FileField()  # for creating file input
    OPTIONS = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                       choices=OPTIONS)


class ApplicantFiles(forms.Form):
    file_1 = forms.FileField()  # for creating file input
