from django.test import TestCase
from .models import FormulaireSante, Utilisateur
from datetime import date

class FormulaireSanteModelTest(TestCase):

    def setUp(self):
        # Créez un utilisateur de test pour l'associer au formulaire
        self.user = Utilisateur.objects.create(username='testuser', password='12345')
        
        # Créez une instance du modèle FormulaireSante avec tous les champs
        self.formulaire = FormulaireSante.objects.create(
            patient=self.user,
            date_remplissage=date.today(),
            periodicite_jours=30,
            is_late=False,
            poids=70.0,
            tour_de_taille_cm=90.0,
            frequence_cardiaque_min=80,
            tension_arterielle_systolique_matin=120.0,
            tension_arterielle_systolique_soir=118.0,
            tension_arterielle_diastolique_matin=80.0,
            tension_arterielle_diastolique_soir=79.0,
            symptomes_cardiovasculaires="",
            nb_medicaments_jour=2,
            oublie_medicament_matin=False,
            oublie_medicament_soir=False,
            effets_secondaires=False,
            symptomes_particuliers=False,
            description_effets_symptomes="",
            consommation_alcool=False,
            grignotage_sucre=False,
            grignotage_sale=False,
            nb_repas_jour=3,
            quantite_eau_litres=1.5,
            quantite_alcool_litres=None,
            activite_physique=True,
            nature_activite_physique="Marche rapide",
            duree_activite_physique_min=None,
            dyspnee=False,
            oedeme=False,
            fievre=False,
            palpitation=False,
            douleur_thoracique=False,
            malaise=False,
            heure_debut_palpitations=None,
            duree_total_palpitations_min=None,
            heure_debut_douleurs_thoraciques=None,
            duree_total_douleurs_thoraciques_min=None,
            heure_debut_malaises=None,
            duree_total_malaises_min=None,
            natremie_mmol_per_l=142.0,
            potassium_mmol_per_l=4.2,
            creatinine_umol_per_l=85.0,
            clairance_creatinine_ml_per_min=95.0,
            nt_probnp_ng_per_l=150.0,
            fer_serique_mg_per_l=100.0,
            hemoglobine_g_per_100_ml=14.0,
            vitesse_sedimentation_mm=2.0,
            proteine_c_reactive_mg_per_l=1.0,
            troponine_ug_per_l=0.01,
            vitamine_d_ng_per_ml=30.0,
            acide_urique_mg_per_l=300.0,
            inr=1.0
        )

    def test_creation_formulaire(self):
        # Testez si le formulaire a été créé correctement
        self.assertTrue(isinstance(self.formulaire, FormulaireSante))

    def test_attributs_formulaire(self):
        # Testez les attributs du formulaire
        self.assertEqual(self.formulaire.patient, self.user)
        self.assertEqual(self.formulaire.date_remplissage, date.today())
        self.assertEqual(self.formulaire.periodicite_jours, 30)
        self.assertEqual(self.formulaire.is_late, False)
        self.assertEqual(self.formulaire.poids, 70.0)
        self.assertEqual(self.formulaire.tour_de_taille_cm, 90.0)
        self.assertEqual(self.formulaire.frequence_cardiaque_min, 80)
        self.assertEqual(self.formulaire.tension_arterielle_systolique_matin, 120.0)
        self.assertEqual(self.formulaire.tension_arterielle_systolique_soir, 118.0)
        self.assertEqual(self.formulaire.tension_arterielle_diastolique_matin, 80.0)
        self.assertEqual(self.formulaire.tension_arterielle_diastolique_soir, 79.0)
        self.assertEqual(self.formulaire.symptomes_cardiovasculaires, "")
        self.assertEqual(self.formulaire.nb_medicaments_jour, 2)
        self.assertEqual(self.formulaire.oublie_medicament_matin, False)
        self.assertEqual(self.formulaire.oublie_medicament_soir, False)
        self.assertEqual(self.formulaire.effets_secondaires, False)
        self.assertEqual(self.formulaire.symptomes_particuliers, False)
        self.assertEqual(self.formulaire.description_effets_symptomes, "")
        self.assertEqual(self.formulaire.consommation_alcool, False)
        self.assertEqual(self.formulaire.grignotage_sucre, False)
        self.assertEqual(self.formulaire.grignotage_sale, False)
        self.assertEqual(self.formulaire.nb_repas_jour, 3)
        self.assertEqual(self.formulaire.quantite_eau_litres, 1.5)
        self.assertIsNone(self.formulaire.quantite_alcool_litres)
        self.assertEqual(self.formulaire.activite_physique, True)
        self.assertEqual(self.formulaire.nature_activite_physique, "Marche rapide")
        self.assertIsNone(self.formulaire.duree_activite_physique_min)
        self.assertEqual(self.formulaire.dyspnee, False)
        self.assertEqual(self.formulaire.oedeme, False)
        self.assertEqual(self.formulaire.fievre, False)
        self.assertEqual(self.formulaire.palpitation, False)
        self.assertEqual(self.formulaire.douleur_thoracique, False)
        self.assertEqual(self.formulaire.malaise, False)
        self.assertIsNone(self.formulaire.heure_debut_palpitations)
        self.assertIsNone(self.formulaire.duree_total_palpitations_min)
        self.assertIsNone(self.formulaire.heure_debut_douleurs_thoraciques)
        self.assertIsNone(self.formulaire.duree_total_douleurs_thoraciques_min)
        self.assertIsNone(self.formulaire.heure_debut_malaises)
        self.assertIsNone(self.formulaire.duree_total_malaises_min)
        self.assertEqual(self.formulaire.natremie_mmol_per_l, 142.0)
        self.assertEqual(self.formulaire.potassium_mmol_per_l, 4.2)
        self.assertEqual(self.formulaire.creatinine_umol_per_l, 85.0)
        self.assertEqual(self.formulaire.clairance_creatinine_ml_per_min, 95.0)
        self.assertEqual(self.formulaire.nt_probnp_ng_per_l, 150.0)
        self.assertEqual(self.formulaire.fer_serique_mg_per_l, 100.0)
        self.assertEqual(self.formulaire.hemoglobine_g_per_100_ml, 14.0)
        self.assertEqual(self.formulaire.vitesse_sedimentation_mm, 2.0)
        self.assertEqual(self.formulaire.proteine_c_reactive_mg_per_l, 1.0)
        self.assertEqual(self.formulaire.troponine_ug_per_l, 0.01)
        self.assertEqual(self.formulaire.vitamine_d_ng_per_ml, 30.0)
        self.assertEqual(self.formulaire.acide_urique_mg_per_l, 300.0)
        self.assertEqual(self.formulaire.inr, 1.0)