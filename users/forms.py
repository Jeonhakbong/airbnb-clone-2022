from click import pass_context
from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong."))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist."))

    """
    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist.")  # raise error.

    def clean_password(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return email
            else:
                raise forms.ValidationError("Password is wrong.")
        except models.User.DoesNotExist:
            pass
    """


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    # first_name = forms.CharField(max_length=80)
    # last_name = forms.CharField(max_length=80)
    # email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)  # commit=Flase : create, but don't save it.

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()

    """
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email")
        except models.User.DoesNotExist:
            return email

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        # password1 = self.cleaned_data.get("password1")

        user = models.User.objects.create_user(email, email, password)

        user.first_name = first_name
        user.last_name = last_name
    """
