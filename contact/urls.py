from django.urls import path,re_path
from contact import views
from allauth.account.views import confirm_email
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('villes/', views.VilleList.as_view()),
     path('formations/', views.FormationList.as_view()),
    path('contacts/', views.ContactRegisterView.as_view()),
    path('contactslist/', views.ContactList.as_view()),
    re_path(r'registration/account-confirm-email/', VerifyEmailView.as_view(),name='account_email_verification_sent'),
    re_path(r'registration/account-confirm-email/(?P<key>[-:\w]+)/', VerifyEmailView.as_view(),name='account_confirm_email'),
    

]
