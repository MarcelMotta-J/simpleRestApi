from django.contrib import admin
from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail

# http://127.0.0.1:8000/api/item/
# http://127.0.0.1:8000/api/location   # adicionar locations e clicar em POST
# clicar em GET e lista todas locations criadas 
# http://127.0.0.1:8000/api/item/     # adicionar items (escolha location no dropbox) e clicar em POST
# clicar em GET e lista todos items criados 

# http://127.0.0.1:8000/api/location/1  # location pelo id

# http://127.0.0.1:8000/api/location  # mostra todas 
# http://127.0.0.1:8000/api/item/     # mostra todos
#  

urlpatterns = [
    path('item/', ItemList.as_view() ),
    path('item/<int:pk>', ItemDetail.as_view() ),
    path('location/', LocationList.as_view() ),
    path('location/<int:pk>', LocationDetail.as_view() ),
]