from rest_framework import serializers
from .models import Categoria, Prodotto, OrdineProdotto, Ordine
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodotto
        fields = '__all__'

# Richiesta JSON --> utente Django
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # VALIDAZIONE DATI
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    # CREA UTENTE DB
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # RITORNA LA RISPOSTA
        return user

# OrdineProdotto per la relazione
class OrdineProdottoSerializer(serializers.ModelSerializer):
    prodotto_id = serializers.IntegerField()

    class Meta:
        model = OrdineProdotto
        fields = ['prodotto_id', 'quantita']

# Richiesta JSON --> crea l'ordine
class OrdineSerializer(serializers.ModelSerializer):
    prodotti = OrdineProdottoSerializer(many=True, write_only=True)

    class Meta:
        model = Ordine
        fields = ['id', 'data_ordine', 'stato', 'totale', 'note', 'prodotti']
        read_only_fields = ['totale', 'stato', 'data_ordine']

    def create(self, validated_data):
        prodotti_data = validated_data.pop('prodotti') # Prendi i dati dei prodotti
        user = self.context['request'].user            # Chi sta facendo la richiesta JWT

        # Crea ordine
        ordine = Ordine.objects.create(
            utente=user,
            stato="in_attesa",
            totale=0,
            note=validated_data.get("note")
        )

        # Calcolo totale
        totale = 0
        for item in prodotti_data:
            prodotto = Prodotto.objects.get(id=item['prodotto_id'])

            # Aggiungi il record in tabella relazione
            OrdineProdotto.objects.create(
                ordine=ordine,
                prodotto=prodotto,
                quantita=item['quantita']
            )

            totale += prodotto.prezzo * item['quantita']

        ordine.totale = totale
        ordine.save()

        return ordine