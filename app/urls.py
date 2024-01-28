from django.urls import path
from .views import home, andijon, buxoro, urganch, xiva, guliston, namangan, jizzax, qarshi, termiz, samarqand,fargona, nukus, navoiy

urlpatterns = [
    path('', home, name='tashkent'),
    path('andijan/', andijon, name='andijan'),
    path('buxoro/', buxoro, name='buxoro'),
    path('urganch/', urganch, name='urganch'),
    path('xiva/', xiva, name='xiva'),
    path('guliston/', guliston, name='guliston'),
    path('namangan/', namangan, name='namangan'),
    path('jizzah/', jizzax, name='jizzah'),
    path('qarshi/', qarshi, name='qarshi'),
    path('termiz/', termiz, name='termiz'),
    path('samarqand/', samarqand, name='samarqand'),
    path('fargona/', fargona, name='fargona'),
    path('navoiy/', navoiy, name='navoiy'),
    path('nukus/', nukus, name='nukus')
]
