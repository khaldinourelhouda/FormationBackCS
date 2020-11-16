from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Ville
from .models import Contact
from .models import Formation

from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields =('id','titre')

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Ville
        fields =('id','titre')
        

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=('id','nom','prenom','ville','telephone','email','formation','societe','fonction','presence','message')


class RegisterSerializer(serializers.Serializer):
    nom = serializers.CharField(required=True, write_only=True)
    prenom = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    telephone = serializers.CharField(required=True, write_only=True)
    ville = serializers.CharField(required=True, write_only=True)
    societe = serializers.CharField(required=True, write_only=True)
    fonction = serializers.CharField(required=True, write_only=True)
    formation = serializers.CharField(required=True, write_only=True)
    presence = serializers.CharField(required=True, write_only=True)
    message = serializers.CharField(required=True, write_only=True)

    
    

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address."))
        return email

   

    def get_cleaned_data(self):
        return {
            'nom': self.validated_data.get('first_name', ''),
            'prenom': self.validated_data.get('last_name', ''),
            'telephone': self.validated_data.get('company', ''),
            'ville': self.validated_data.get('ville', ''),
            'societe': self.validated_data.get('societe', ''),
            'email': self.validated_data.get('email', ''),
            'presence': self.validated_data.get('presence', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user
    