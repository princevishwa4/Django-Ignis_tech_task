from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from events.models import Event

class RegisterForm(UserCreationForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		labels = {'first_name' : 'First Name', 'last_name' : 'Last Name', 'email' : 'Email'}
		widgets = {'username' : forms.TextInput(attrs={'class' : 'form-control'}), 
					'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
					'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
					'email' : forms.EmailInput(attrs={'class' : 'form-control'})}


class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={'autofocus' : True, 'class' : 'form-control'}))
	password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class' : 'form-control'}))


class EventForm(forms.ModelForm):
	organizer = forms.ModelChoiceField(queryset=User.objects.all(), initial='admin', widget=forms.Select(attrs={'class' : 'form-control'}))
	
	class Meta:
		model = Event
		fields = ['organizer', 'event_name', 'description', 'image', 'location', 'start_date', 'end_date', 'start_time', 'end_time']
		widgets = { 
					'event_name' : forms.TextInput(attrs={'class' : 'form-control'}),
					'description' : forms.Textarea(attrs={'class' : 'form-control'}),
					'location' : forms.TextInput(attrs={'class' : 'form-control'}),
					'start_date' : forms.DateTimeInput(attrs={'class' : 'form-control', 'type' : 'date'}),
					'end_date' : forms.DateTimeInput(attrs={'class' : 'form-control', 'type' : 'date'}),
					'start_time' : forms.DateTimeInput(attrs={'class' : 'form-control', 'type' : 'time'}),
					'end_time' : forms.DateTimeInput(attrs={'class' : 'form-control', 'type' : 'time'})
				}
		