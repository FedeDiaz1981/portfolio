from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    correo = forms.EmailField(label='Correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')
