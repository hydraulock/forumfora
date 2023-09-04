from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('inscription', register_view, name='register'),
    path('connexion', login_view, name='login'),
    path('detail/<slug:slug>/<int:id>', detail,name='detail'),
    path('info/<slug:slug>/<int:id>', detail_job,name='detail-job'),
    path('logout/', logout, name='logout'),
    path('jobs/', jobs, name='jobs'),
    path('divers/vêtements/', products_clothes, name='products_clothes'),
    path('immobilier/construction/plans', products_plans, name='products_plans'),
    path('mon-compte/', annonces, name='annonces'),
    path('mon-compte/mes-annonces', annonces, name='annonces'),
    path('mon-compte/profil',profile,name='profile'),
    path('creation/',category, name='category'),
    path('creation/category',category, name='category'),
    path('creation/immobilier/location', location, name='location'),
    path('creation/immobilier/vente', vente, name='vente'),
    path('creation/immobilier/plan', plan, name='plan'),
    path('creation/véhicules/voiture', voiture, name='voiture'),
    path('creation/services/chantier', chantier, name ='chantier'),
    path('creation/emplois/marketing-vente/', marketing_vente, name='marketing-vente'),
    path('creation/divers/vêtements', clothes, name='clothes'),

]