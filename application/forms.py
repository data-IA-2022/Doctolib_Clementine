from django import forms
from application.models import FormulaireSante, FormulaireStress
from authentification.models import Utilisateur

class FormulaireSanteForm(forms.ModelForm):
    class Meta:
        model = FormulaireSante
        fields = "__all__"
        widgets = {
            'heure_debut_palpitations': forms.TimeInput(attrs={'type': 'time'}),
            'heure_debut_douleurs_thoraciques': forms.TimeInput(attrs={'type': 'time'}),
            'heure_debut_malaises': forms.TimeInput(attrs={'type': 'time'}),
            'date_remplissage': forms.DateInput(attrs={'type': 'date'}),
            # Ajoutez ici d'autres champs TimeField si nécessaire
        }
        
class FormulaireStressForm(forms.ModelForm):
    class Meta:
        model = FormulaireStress
        fields = "__all__"

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'first_name', 'last_name', 'role']  # Ajoutez ou retirez les champs selon votre modèle

    def init(self, args, **kwargs):
        super(UtilisateurForm, self).init(args, **kwargs)

        # Personnalisez les widgets si nécessaire
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Prénom'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Nom'})

#Gérez le choix du rôle, si votre modèle le permet
        self.fields['role'].widget = forms.Select(choices=Utilisateur.ROLE_CHOICES)
