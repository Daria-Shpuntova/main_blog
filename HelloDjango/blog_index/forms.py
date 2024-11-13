from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'email_text'}))
    subject = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={'class':'name_text'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class':'massage-bt'}), required=True)