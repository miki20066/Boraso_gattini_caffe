from django.urls import path
from .views import ProdottoList, ProdottoDetail, CategoriaList, CategoriaDetail, RegisterView, MeView, OrdineDetail, OrdineListCreate, OrdineStatoUpdate, AllProducts, AllCategories

urlpatterns = [
    # PAGINE HTML
    path('prodotti-html/', AllProducts.as_view()),
    path('categorie-html/', AllCategories.as_view()),

    # PRODOTTI
    path('prodotti/', ProdottoList.as_view()),
    path('prodotti/<int:id>/', ProdottoDetail.as_view()),

    # CATEGORIE
    path('categorie/', CategoriaList.as_view()),
    path('categorie/<int:id>/', CategoriaDetail.as_view()),

    # AUTH (interno app ma sotto /api/auth/)
    path('auth/register/', RegisterView.as_view()),
    path('auth/me/', MeView.as_view()),

    # ORDINI
    path('ordini/', OrdineListCreate.as_view()),
    path('ordini/<int:id>/', OrdineDetail.as_view()),
    path('ordini/<int:id>/stato/', OrdineStatoUpdate.as_view()),
]