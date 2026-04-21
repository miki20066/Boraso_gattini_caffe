from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Non ho usato le migration, ma ho usato la class Meta con managed = False

class Categoria(models.Model):
    id = models.AutoField(primary_key=True) # Chiave --> valore auto
    nome = models.CharField(max_length=255)
    descrizione = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'categoria'

class Prodotto(models.Model):
    id = models.AutoField(primary_key=True)  # Chiave --> valore auto
    nome = models.CharField(max_length=255)
    descrizione = models.TextField(null=True, blank=True)
    prezzo = models.FloatField()
    disponibile = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    immagine_url = models.URLField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'prodotto'

class Ordine(models.Model):
    id = models.AutoField(primary_key=True)
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_ordine = models.DateTimeField(default=timezone.now)
    stato = models.CharField(max_length=50)
    totale = models.FloatField()
    note = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ordine'

class OrdineProdotto(models.Model):
    ordine = models.ForeignKey(Ordine, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ordine_prodotto'
