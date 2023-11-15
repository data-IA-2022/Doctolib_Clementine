from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from authentification.models import Utilisateur, medecinPatient
from application.models import FormulaireSante
from application.forms import FormulaireSanteForm, FormulaireStressForm,  UtilisateurForm #InfoGeneraleForm, EtatDeSanteForm #
#from formtools.wizard.views import SessionWizardView
from django.core.mail import EmailMessage
import os
from django.http import HttpResponse
import datetime
from django.conf import settings
from django.core.mail import send_mail

@login_required
def accueil(request):
    prenom = request.user.username
    return render(request,"accueil.html",
                  context={"prenom": prenom})


@login_required
def comptes(request):
    regexMDP = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-]).{8,}$"
    message = ""
    if request.method == "POST":
        ancienMDP = request.POST["ancienMDP"]
        nouveauMDP1 = request.POST["nouveauMDP1"]
        nouveauMDP2 = request.POST["nouveauMDP2"]
        
        verification = authenticate(username = request.user.username,
                                    password = ancienMDP)
        if verification != None:
            if nouveauMDP1 == nouveauMDP2:
                utilisateur = Utilisateur.objects.get(username = request.user.username)
                #utilisateur = Utilisateur.objects.get(id=request.user.id)
                utilisateur.set_password(request.POST.get("nouveauMDP1"))
                utilisateur.save()
                return redirect("accueil")
            else:
                message = "⚠️ Les deux mot de passe ne concordent pas ⚠️"
        else:
            message = "L'ancien mot de passe n'est pas bon. T'es qui toi ? 😡"
    return render(request,
                  "comptes.html",
                  {"regexMDP" : regexMDP, "message" : message})

@login_required
def edaia(request):
    if request.user.role != "medecin":
        return redirect("https://media.tenor.com/2euSOQYdz8oAAAAj/this-was-technically-illegal-maclen-stanley.gif")
    else:
        return render(request, "edaia.html")

@login_required
def associationMedecinPatient(request):

    if request.user.role == 'patient':
        return redirect('connexion')

    medecins = [medecin.username for medecin in Utilisateur.objects.filter(role="medecin")]

    medecin_connecte = request.user
    patients_associes = medecinPatient.objects.filter(idMedecin=medecin_connecte).select_related('idPatient')
    listePatientsAssocies = [assoc.idPatient for assoc in patients_associes]

    tous_les_patients = Utilisateur.objects.filter(role="patient")
    listePatientsNonAssocies = [patient for patient in tous_les_patients if patient not in listePatientsAssocies]

    if request.method == "POST":
        medecin = request.POST["medecin"]
        patient = request.POST["patient"]
        medecinPatient(idMedecin=Utilisateur.objects.get(username=medecin), 
                       idPatient=Utilisateur.objects.get(username=patient)).save()
        
        # Envoyer un e-mail au médecin avec la notice en pièce jointe
        chemin_notice = os.path.join(settings.MEDIA_ROOT, 'notice.pdf')
        email_medecin = EmailMessage(
            'Association Patient-Médecin Effectuée',
            f'Une association avec un nouveau patient a été réalisée. Veuillez trouver ci-joint la notice de protection des données à faire signer par le patient.',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email]
        )
        email_medecin.attach_file(chemin_notice)
        email_medecin.send()        
        
        # Envoyer un e-mail à l'administrateur
        sujet = 'Nouvelle Association Médecin-Patient'
        message = f'Une nouvelle association a été réalisée entre le médecin {medecin} et le patient {patient}.'
        send_mail(
            sujet,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],  # Utiliser l'adresse e-mail de l'administrateur
            fail_silently=False,
        )        
               
        return redirect("associationMedecinPatient")
    association = medecinPatient.objects.all()
    return render(request, "associationMedecinPatient.html", {

        "medecins": medecins,
        "listePatientsNonAssocies": listePatientsNonAssocies,
        "tableAssociationMedecinPatient": association
    })


@login_required
def historiqueFormulairesPatients(request):
    # Rediriger si l'utilisateur n'est ni médecin, ni admin, ni patient
    if request.user.role not in ['medecin', 'admin', 'patient']:
        return redirect('accueil')

    # Si l'utilisateur est un médecin ou un admin, afficher les formulaires de tous les patients associés
    if request.user.role in ['medecin', 'admin']:
        patients_associes = medecinPatient.objects.filter(
            idMedecin=request.user).select_related('idPatient')
        patients_ids = [assoc.idPatient.id for assoc in patients_associes]
    else:  # Si l'utilisateur est un patient, afficher uniquement ses formulaires
        patients_ids = [request.user.id]

    champs_a_inclure = [
        field.name for field in FormulaireSante._meta.get_fields()]
    formulaires_des_patients_associes = FormulaireSante.objects.filter(
        patient__id__in=patients_ids
    ).values(*champs_a_inclure)

    # Modifier les données pour remplacer l'ID du patient par son username
    dataFormulaireSante_modifiee = []
    for formulaire in formulaires_des_patients_associes:
        formulaire_modifie = formulaire.copy()
        patient_id = formulaire_modifie.get('patient')
        if patient_id:
            formulaire_modifie['patient'] = Utilisateur.objects.get(
                id=patient_id).username
        dataFormulaireSante_modifiee.append(formulaire_modifie)

    return render(request, "listeformulairespatients.html", {
        "champsFormulaireSante": champs_a_inclure,
        "dataFormulaireSante": dataFormulaireSante_modifiee
    })


@login_required
def formulaireSante(request):
    if request.method == "POST":
       formulaire = FormulaireSanteForm(request.POST)
       if formulaire.is_valid():
           sauvagarde = formulaire.save() 
    else:
        formulaire = FormulaireSanteForm()
    return render(request,
                  "formulaireSante.html",
                  {"formulaire" : formulaire})
    
@login_required
def formulaireStress(request):
    if request.method == "POST":
       formulaire = FormulaireStressForm(request.POST)
       if formulaire.is_valid():
           sauvagarde = formulaire.save() 
    else:
        formulaire = FormulaireStressForm()
    return render(request,
                  "formulaireStress.html",
                  {"formulaire" : formulaire})

@login_required
def create_patient(request):
    if request.method == "POST":
        form = UtilisateurForm(request.POST)  # Assurez-vous que ce formulaire existe
        if form.is_valid():
            new_patient = form.save(commit=False)
            new_patient.role = 'patient'  # Assurez-vous que le modèle Utilisateur a un champ 'role'
            new_patient.save()
            return redirect('liste_patients')  # Redirige vers la liste des patients
    else:
        form = UtilisateurForm()
    return render(request, 'create_patient.html', {'form': form})  # Template pour créer un patient

@login_required
def liste_patients(request):
    if request.user.role == 'medecin':
        patients = medecinPatient.objects.filter(idMedecin=request.user).select_related('idPatient')
        return render(request, 'liste_patients.html', {'patients': patients})  # Template pour afficher la liste des patients
    else:
        return redirect('accueil')
    
@login_required
def update_patient(request, patient_id):
    patient = get_object_or_404(Utilisateur, pk=patient_id, role='patient')
    if request.method == "POST":
        form = UtilisateurForm(request.POST, instance=patient)  # Assurez-vous que ce formulaire existe
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
    else:
        form = UtilisateurForm(instance=patient)
    return render(request, 'update_patient.html', {'form': form, 'patient_id': patient_id})  # Template pour mettre à jour un patient

@login_required
def delete_patient(request, patient_id):
    if request.method == "POST":
        patient = get_object_or_404(Utilisateur, pk=patient_id, role='patient')
        patient.delete()
        return redirect('liste_patients')

