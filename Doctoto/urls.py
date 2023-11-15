"""
URL configuration for Doctoto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentification.views import connexion, creationpatient, deconnexion
from application.views import (accueil, edaia, associationMedecinPatient, 
                               comptes, formulaireSante, historiqueFormulairesPatients, 
                               formulaireStress, liste_patients, create_patient, update_patient, delete_patient) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connexion', connexion, name='connexion'),
    path('creationpatient', creationpatient, name='creationpatient'),
    path('', accueil, name='accueil'),
    path('edaia', edaia, name='edaia'),
    path('associationMedecinPatient', associationMedecinPatient, name='associationMedecinPatient'),
    path('comptes', comptes, name='comptes'),
    path('deconnexion', deconnexion, name='deconnexion'),
    path('formulaireSante', formulaireSante, name='formulaireSante'),
    path('historique', historiqueFormulairesPatients, name='historique'),
    path('formulaireStress', formulaireStress, name='formulaireStress'),
    path('liste_patients', liste_patients, name='liste_patients'),
    path('create_patient', create_patient, name='create_patient'),
    path('update_patient/<int:patient_id>/', update_patient, name='update_patient'),
    path('delete_patient/<int:patient_id>/', delete_patient, name='delete_patient'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)