from django import forms
from .models import (
    Register_Model,
)
#Esta classe, formará o formulário a partir do model
class Register_Form(forms.ModelForm):
    class Meta: #(atributos extras à classe)
        model = Register_Model
        fields = '__all__'