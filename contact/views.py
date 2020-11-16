from django.shortcuts import render
from allauth.account import app_settings as allauth_settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.debug import sensitive_post_parameters
from allauth.account.utils import complete_signup
# Create your views here.
from contact.models import Ville,Contact,Formation

from contact.serializers import VilleSerializer
from contact.serializers import ContactSerializer
from contact.serializers import FormationSerializer,RegisterSerializer
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.models import TokenModel
# Create your views here.

class FormationList(ListCreateAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer
    permission_classes = [AllowAny]


class FormationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer

class VilleList(ListCreateAPIView):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer
    permission_classes = [AllowAny]


class VilleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer


class ContactList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]


class ContactDetail(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
         
class ContactRegisterView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
    token_model = TokenModel
    throttle_scope = 'dj_rest_auth'
   

  
    def dispatch(self, *args, **kwargs):
        return super(ContactRegisterView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {"detail": ("Verification e-mail sent.")}
        

        

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self,serializer):
        user = serializer.save()
        if allauth_settings.EMAIL_VERIFICATION != \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            if getattr(settings, 'REST_USE_JWT', False):
                self.access_token, self.refresh_token = jwt_encode(user)
            else:
                create_token(self.token_model, user, serializer)
        
            

        complete_signup(self.request._request, user,
                        allauth_settings.EMAIL_VERIFICATION,
                        None)
        return user


        

        
    
          

        
