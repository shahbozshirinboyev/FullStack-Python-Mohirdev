from django import forms
from users.models import CustomUser

class UserCreateForm(forms.Form):
  username = forms.CharField(max_length=150)
  email = forms.EmailField()
  first_name = forms.CharField(max_length=150)
  last_name = forms.CharField(max_length=150)
  password = forms.CharField(max_length=128)
  # avatar = forms.ImageField()

  def save(self):
    username = self.cleaned_data['username']
    first_name = self.cleaned_data['first_name']
    last_name = self.cleaned_data['last_name']
    email = self.cleaned_data['email']
    password = self.cleaned_data['password']
    user = CustomUser.objects.create(
      username=username,
      first_name=first_name,
      last_name=last_name,
      email=email,
      )
    user.set_password(password)
    user.save()
    return user

class UserLoginForm(forms.Form):
  username = forms.CharField(max_length=150)
  password = forms.CharField(max_length=128)

class UserUpdateForm(forms.ModelForm):
  class Meta:
    model = CustomUser
    fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
