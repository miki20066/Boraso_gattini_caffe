from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveAPIView
from .serializers import (ProdottoSerializer, CategoriaSerializer, RegisterSerializer, OrdineSerializer, OrdineProdottoSerializer)
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Prodotto, Ordine, Categoria

# IN QUESTO CODICE CI SONO ANCHE DEGLI APPUNTI
# SU NUOVI ELEMENTI NON VISTI IN CLASSE

# DEBUG - (VIEW COME NEL PRIMO TUTORIAL)
class AllProducts(ListView):
    model = Prodotto
    template_name = "prodotti/index.html"

class AllCategories(ListView):
    model = Categoria
    template_name = "categorie/index.html"

# VIEW RICHIESTE DALLA CONSEGNA

# LISTA PRODOTTI CON PARAMETRI AGGIUNTIVI - API PUBBLICA
class ProdottoList(ListAPIView):
    serializer_class = ProdottoSerializer

    # Check dati da Query String
    def get_queryset(self):
        queryset = Prodotto.objects.all()

        categoria = self.request.query_params.get('categoria')
        disponibile = self.request.query_params.get('disponibile')
        search = self.request.query_params.get('search')

        if categoria:
            queryset = queryset.filter(categoria_id=categoria)

        if disponibile:
            if disponibile.lower() == 'true':
                queryset = queryset.filter(disponibile=True)

        if search:
            # Q: QUERY COMPLESSE (BOOLEAN OP)
            queryset = queryset.filter(
                Q(nome__icontains=search) | Q(descrizione__icontains=search)
            )

        return queryset

# LISTA CATEGORIE (NO FILTRI RICHIESTI) - API PUBBLICA
class CategoriaList(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# REGISTRAZIONE NEL DB
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []  # vuoto => nessun permesso richiesto

# DETTAGLI ADMIN - JWT
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })

#is_staff fa parte di User in Django
# POST + GET - CREA PRODOTTO E VISUALIZZA
class ProdottoListCreate(ListCreateAPIView):
    queryset = Prodotto.objects.all()
    serializer_class = ProdottoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] #IsAdminUser ha anche IsAuthenticated internamente => lascio così per revisioni

# PUT + PATCH + DELETE - MODIFICA / AGGIORNA / ELIMINA PRODOTTO
class ProdottoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Prodotto.objects.all()
    serializer_class = ProdottoSerializer
    permission_classes =[IsAuthenticated, IsAdminUser]
    lookup_field = 'id'

# POST + GET - CREA CATEGORIA
class CategoriaListCreate(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# PUT + DELETE - MODIFICA / ELIMINA CATEGORIA
class CategoriaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'id'

# GET + POST - LISTA DEGLI ORDINI
class OrdineListCreate(ListCreateAPIView):
    serializer_class = OrdineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Ordine.objects.all()
        return Ordine.objects.filter(utente=user)

    def perform_create(self, serializer):
        serializer.save(utente=self.request.user)

# DETTAGLIO DELL'ORDINE
class OrdineDetail(RetrieveAPIView):
    serializer_class = OrdineSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Ordine.objects.all()
        return Ordine.objects.filter(utente=user)

# MODIFICA STATO (SOLO ADMIN)
class OrdineStatoUpdate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request, id):
        ordine = Ordine.objects.get(id=id)

        ordine.stato = request.data.get("stato")
        ordine.save()

        return Response({"message": "stato aggiornato"})