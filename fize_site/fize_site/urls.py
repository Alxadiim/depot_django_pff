"""
URL configuration for fize_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from auth_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path("navigation/", views.navigation, name="navigation"),
    path('connexion/acceuil/', views.index, name='index'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('eleves/<int:admin_id>/', views.student_list, name='student_list'),
    path('connexion/responsable_metier/<int:responsable_id>/', views.responsable_metier, name='responsable_metier'),
    path('connexion/detail_eleve/<int:student_id>/', views.student_detail, name='student_detail'),
    path('connexion/detail_prof/<int:teacher_id>/', views.detail_prof, name='detail_prof'),
    path('filter_students_view/', views.filter_students_view, name='filter_students_view'),
    path('filter_teacher/', views.filter_teacher, name='filter_teacher'),
    path('connexion/teacher_list/<int:admin_id>/', views.teacher_list, name='teacher_list'),
    path('Responsable_filiere/<int:admin_id>/', views.responsableFiliere_list, name='responsableFiliere_list'),
    path('student_add/<int:admin_id>/', views.add_student, name='add_student'),
    path('liste filieres/<int:admin_id>/', views.liste_filieres, name='liste_filieres'),
    path('ajouter_prof/<int:admin_id>/', views.add_teacher, name='add_teacher'),
    path('connexion/Affecter_professeur/<int:responsable_id>/', views.affecter_professeur, name='affecter_professeur'),
    path('ajouter_filiere/<int:admin_id>/', views.ajouter_filiere, name='ajouter_filiere'),
    path('ajouter_responsable/<int:admin_id>/', views.ajouter_responsable, name='ajouter_responsable'),
    path('teacher/update/<int:teacher_id>/', views.update_teacher, name='update_teacher'),
    path('student/update/<int:student_id>/', views.update_student, name='update_student'),
    path('modifier_responsable/<int:admin_id>/', views.update_responsable, name='update_responsable'),
    path('suprof/<int:id>/', views.delete_teacher_by_id, name='delete_teacher_by_id'),
    path('connexion/supeleve/<int:student_id>/', views.delete_student_by_id, name='delete_student_by_id'),
    path('connexion/pointage/<int:teacher_id>/', views.pointage, name='pointage'),
    path('success_page/', views.success_page, name='success_page'),
    # path('pointages/<int:teacher_id>/', views.liste_pointages, name='liste_pointages'),
    path('create_planning/', views.create_planning, name='create_planning'),
    path('connexion/parametre_filiere/<int:responsable_id>/', views.parametre_filiere, name='parametre_filiere'),    
    path('connexion/espaceeleve/<int:student_id>/', views.espaceeleve, name='espaceeleve'),
    path('connexion/espaceprof/<int:teacher_id>/', views.espaceprof, name='espaceprof'),
    path('connexion/espaceadmin/<int:admin_id>/', views.espaceadmin, name='espaceadmin'),
    path('connexion/responsableclasse/<int:responsable_id>', views.responsableclasse, name='responsableclasse'),
    path('responsableclasse/', views.espaceresponsableclasse, name='espaceresponsableclasse'),
    path('connexion/responsable_filiere/<int:responsable_id>', views.responsable_filiere, name='responsable_filiere'),
    path('connexion/notes_filiere/<int:responsable_id>/', views.notes_filiere, name='notes_filiere'),
    path('connexion/moyenne_par_classe/<int:responsable_id>/', views.moyenne_par_classe, name='moyenne_par_classe'),
    # path('classe_detail/<int:classe_id>/', views.classe_detail, name='classe_detail'),
    path('ajouter_classe/', views.ajouter_classe, name='ajouter_classe'),
    path('liste_classes/', views.liste_classes, name='liste_classes'),
    path('connexion/liste_etudiant/<int:teacher_id>/', views.prof_etudiant_list, name='prof_etudiant_list'),
    path('connexion/ajouter_note/<int:teacher_id>/', views.ajouter_notes, name='ajouter_notes'),
    path('connexion/afficher_notes/<int:teacher_id>/', views.afficher_notes, name='afficher_notes'),
    path('connexion/note/<int:student_id>/', views.note_eleve, name='note_eleve'),
    path('modifier_notes/<int:note_id>/', views.modifier_notes, name='modifier_notes'),
    path('connexion/note/<int:teacher_id>/', views.filtrer_notes, name='filtrer_notes'),
    path('ajouter_salle/<int:admin_id>/', views.ajouter_salle, name='ajouter_salle'),
    path('liste_salle/', views.liste_salles, name='liste_salles'),
    path('connexion/ajouter_classe/<int:administrateur_id>/', views.ajouter_classe, name='ajouter_classe'),
    path('classes/modifier/<int:id>/', views.modifier_classe, name='modifier_classe'),
    path('classes/supprimer/<int:id>/', views.supprimer_classe, name='supprimer_classe'),
    path('salles/', views.liste_salles, name='liste_salles'),
    path('salles/ajouter/', views.ajouter_salle, name='ajouter_salle'),
    path('connexion/salles/modifier/<int:id>/', views.modifier_salle, name='modifier_salle'),
    path('connexion/salles/supprimer/<int:id>/', views.supprimer_salle, name='supprimer_salle'),
    path('planning/', views.planning_list, name='planning_list'),
    path('connexion/planning/delete/<int:pk>/', views.delete_planning, name='delete_planning'),
    path('connexion/planning/edit/<int:pk>/', views.edit_planning, name='edit_planning'),
    # path('comptable/', views.comptable_list, name='comptable_list'),
    path('connexion/espacecomptable/<int:comptable_id>/', views.espacecomptable, name='espacecomptable'),
    # path('comptable_detail/<int:id>/', views.comptable_detail, name='comptable_detail'),
    # path('comptable/<int:id>/edit/', views.comptable_edit, name='comptable_edit'),
    # path('comptable/<int:id>/delete/', views.comptable_delete, name='comptable_delete'),
    # path('paiements/', views.view_teacher_payments, name='view_teacher_payments'),
    # path('manage_payments/', views.manage_payments, name='manage_payments'),
    # path('payment_list/', views.payment_list, name='payment_list'),
    # path('affecter_prof/<int:teacher_id>/', views.affecter_prof, name='affecter_prof'),
    path('teacher_class/<int:responsable_id>/', views.teacher_class, name='teacher_class'),   
    path('connexion/affecter_eleve/<int:admin_id>/', views.Affecter_eleve, name='Affecter_eleve'),
    path('liste_classe/', views.liste_classe, name='liste_classe'),
    path('class_info/', views.class_info, name='class_info'),
    path('connexion/remplir-cahier/<int:teacher_id>/', views.remplir_cahier, name='remplir_cahier'),
    path('connexion/liste_cahiers/<int:teacher_id>/',views.liste_cahiers, name='liste_cahiers'),
    path('connexion/liste_cahier/<int:responsable_id>/',views.listes_cahiers, name='listes_cahiers'),
    path('planning_eleve/', views.planning_eleve, name='planning_eleve'),
    # path('env_planning/', views.env_planning, name='env_planning'),
    path('filter_planning/', views.filter_planning, name='filter_planning'),
    path('ajouter_matiere/<int:responsable_id>/', views.ajouter_matiere, name='ajouter_matiere'),
    path('connexion/ajouter_ressource/<int:teacher_id>/', views.ajouter_ressource, name='ajouter_ressource'),
    path('connexion/modifier_matiere/<int:matiere_id>/', views.modifier_matiere, name='modifier_matiere'),
    path('connexion/supprimer_matiere/<int:matiere_id>/', views.supprimer_matiere, name='supprimer_matiere'),
    path('liste_matieres/<int:responsable_id>/', views.liste_matieres, name='liste_matieres'),
    path('upload/', views.upload_and_resize_image, name='upload_image'),
    path('success/', views.success_page, name='success_page'), 
    path('connexion/classe/<int:classe_id>/', views.details_classe, name='details_classe'),
    path('envoyer-email/', views.envoyer_email, name='envoyer_email'),
    path('connexion/classes/<int:classe_id>/', views.classes, name='classes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)