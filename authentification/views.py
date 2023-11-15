from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from authentification.models import Utilisateur
from django.contrib.auth.decorators import login_required
import random 
import string
import os
import pandas as pd

def connexion(request):
    message = ""
    # A t'on reçu des datas d'un formulaire ? Si oui la condition est True
    if request.method == "POST": 
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        verification = authenticate(username = username,
                                    password = motDePasse)
        if verification != None:
            login(request, verification)
            return redirect("accueil")
        else:
            message = "username ou/et mot de passe incorrect"
    
    return render(request,
                      "connexion.html", {"message" : message})

def deconnexion(request):
    logout(request)
    return redirect("connexion")

@login_required
def creationpatient(request):
    ideeMDP = "".join([random.choice(string.printable) for _ in range(12)]).replace(" ", "")
     
    while True:
        nouveau_patient = "P" + str(int(list(Utilisateur.objects.filter(role="patient"))[-1].username[1:]) + 1)
        if not Utilisateur.objects.filter(username=nouveau_patient).exists():
            break
    
    if request.method == "POST":
        username = request.POST["username"]
        email_patient = request.POST.get("email", "")
        # Générer un mot de passe initial
        motDePasse_initial = "P" + str(int(list(Utilisateur.objects.filter(role="patient"))[-1].username[1:]) + 1) + "MDP"

        # Créer le compte utilisateur
        nouveauCompte = Utilisateur.objects.create_user(username=username, role="patient", password=motDePasse_initial, email=email_patient)

        # Préparer le lien pour la réinitialisation du mot de passe
        url_reinit = request.build_absolute_uri(reverse('comptes'))

        # Préparer et envoyer l'e-mail au patient
        email_patient_message = EmailMessage(
            'Bienvenue chez Nous!',
            f'Votre compte a été créé avec succès. Votre mot de passe initial est: {motDePasse_initial}. Veuillez le changer dès que possible en suivant ce lien: {url_reinit}',
            settings.DEFAULT_FROM_EMAIL,
            [email_patient]
        )
        email_patient_message.send()
        
        
        # Envoyer un e-mail au médecin avec la notice en pièce jointe
        chemin_notice = os.path.join(settings.MEDIA_ROOT, 'notice.pdf') 
        email_medecin = EmailMessage(
            'Nouveau Patient Créé',
            f'Un nouveau patient a été créé. Veuillez trouver ci-joint la notice de protection des données à faire signer par le patient.',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email]  # Envoi de l'e-mail au médecin
        )
        email_medecin.attach_file(chemin_notice)
        email_medecin.send()

        return redirect("accueil")

    return render(request, "creationpatient.html", {"ideeMDP": ideeMDP.replace(" ", ""), "nouveau_patient": nouveau_patient})

def alimentationPatients():
    listePatients = pd.read_csv("authentification/datas/listePatients.csv")
    for index, valeurs in listePatients.iterrows():
        #champDBB = Utilisateur._meta.get_fields()
        
        Utilisateur.objects.create_user(username = valeurs.username,
                                        password = valeurs.motDePasse,
                                        role="patient")
        
        
def alimentationMedecin():
    listeMedecins = pd.read_csv("authentification/datas/listeMedecins.csv")
    for index, valeurs in listeMedecins.iterrows():
        Utilisateur.objects.create_user(username = valeurs.username,
                                        password = valeurs.motDePasse,
                                        role="medecin")
        
if len(Utilisateur.objects.filter(role="patient")) == 0:
    alimentationPatients()
if len(Utilisateur.objects.filter(role="medecin")) == 0:
    alimentationMedecin() 

