from userena.forms import SignupForm, AuthenticationForm, identification_field_factory, USERNAME_RE, EditProfileForm, ChangeEmailForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _
from userena.contrib.umessages.forms import ComposeForm
#custom forms with css and widgets
custom_attrs_dict = {"class":"required form-control"}
class CustomSignupForm(SignupForm):
    username = forms.RegexField(regex=USERNAME_RE,
                                max_length=30,
                                widget=forms.TextInput(attrs=custom_attrs_dict),
                                label=_("Username"),
                                error_messages={'invalid': _('Username must contain only letters, numbers, dots and underscores.')})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(custom_attrs_dict,
                                                               maxlength=254)),
                             label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=custom_attrs_dict,
                                                           render_value=False),
                                label=_("Create password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=custom_attrs_dict,
                                                           render_value=False),
                                label=_("Repeat password"))

class CustomSigninForm(AuthenticationForm):
    identification = identification_field_factory(_(u"Email or username"),
                                                  _(u"Either supply us with your email or username."))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs=custom_attrs_dict, render_value=False))

class CustomEditProfileForm(EditProfileForm):
    first_name = forms.CharField(label=_(u'First name'),
                                 max_length=30,
                                 widget=forms.TextInput(attrs=custom_attrs_dict),
                                 required=False)
    last_name = forms.CharField(label=_(u'Last name'),
                                max_length=30,
                                widget=forms.TextInput(attrs=custom_attrs_dict),
                                required=False)
    def __init__(self, *args, **kwargs):
        super(CustomEditProfileForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs.update({'class' : 'form-control'})


class CustomMessageForm(ComposeForm):
    def __init__(self, *args, **kwargs):
        super(CustomMessageForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs.update({'class' : 'form-control'})

class CustomPasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs.update({'class' : 'form-control'})

class CustomEmailChangeForm(ChangeEmailForm):
    def __init__(self, *args, **kwargs):
        super(CustomEmailChangeForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs.update({'class' : 'form-control'})

