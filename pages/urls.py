from django.urls import path
from pages.views import index, convocacoes, denuncia, documentos, faleconosco, filiese, sobrenos

urlpatterns = [
path('', index, name='index'),
path('convocacoes/', convocacoes, name='convocacoes'),
path('denuncia/', denuncia, name='denuncia'),
path('documentos/', documentos, name='documentos'),
path('faleconosco/', faleconosco, name='faleconosco'),
path('filiese/', filiese, name='filiese'),
path('sobrenos/', sobrenos, name='sobrenos'),

]