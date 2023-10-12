from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('html/', show_html, name='show_html'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_amount/<int:id>/', add_amount, name='add_amount'),
    path('subtract_amount/<int:id>/', subtract_amount, name='subtract_amount'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('add-amount-ajax/<int:id>/', add_amount_ajax, name='add_amount_ajax'),
    path('subtract-amount-ajax/<int:id>/', subtract_amount_ajax, name='subtract_amount_ajax'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
]