from django.urls import path
from home import views
from authorization import views as auth_views
from productorder import views as order_views


urlpatterns = [
    path("", views.home, name="home"),
    path('products/<int:pk>/', views.show_products, name="products_men"),
    path('product_details/<str:product_name>/', views.product_details, name="product_deatils"),
    path('search_category', views.search, name="search_category"),
]

urlpatterns_auth =[
    path('register/', auth_views.register, name="register"),
    path('register/login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
]
urlpatterns += urlpatterns_auth

urlpatterns_order_product =[
    path('update_item/', order_views.update_item, name="update_item"),
    path('cart/', order_views.cart, name="cart"),
    path('checkout/', order_views.checkout, name="checkout"),
    path('process_order/', order_views.process_order, name="process_order"),
    path('user_orders', order_views.user_orders, name="user_orders")
]
urlpatterns += urlpatterns_order_product