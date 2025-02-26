from django.urls import path
from acseace.views import agentedesaude, conquistas, faq, ifa, juntese, pccv, quemsomos, proximoseventos

urlpatterns = [
path('agentedesaude/', agentedesaude, name='agentedesaude'),
path('agentedesaude/conquistas', conquistas, name='conquistas'),
path('agentedesaude/faq', faq, name='faq'),
path('agentedesaude/ifa', ifa, name='ifa'),
path('agentedesaude/juntese', juntese, name='juntese'),
path('agentedesaude/pccv', pccv, name='pccv'),
path('agentedesaude/quemsomos', quemsomos, name='quemsomos'),
path('agentedesaude/proximoseventos', proximoseventos, name='proximoseventos'),
]