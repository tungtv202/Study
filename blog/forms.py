from django import forms
from blog.models import Post


class PostForm(forms.Form):
    username = forms.CharField(label="Tai khoan")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="pass", widget=forms.PasswordInput)

    def clean_password(self):
        if 'password' in self.cleaned_data:
            password1 = self.cleaned_data['password']
            if password1 == password1:
                return password1
            raise forms.ValidationError("Mat khau khong hop le")

    def save(self):
        Post.objects.create(title="title2", body="body2")
