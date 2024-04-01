from django.urls import path 
from livraria.views import home,sobre,logout_user,login_user,register_user,book_detail

urlpatterns  = [
    path("",home, name = "home"),
    path("sobre/" ,sobre),
    path("logout/",logout_user,name="logout"),
    path("login/",login_user,name="login"),
    path("cadastro/",register_user,name="register"),
    path("book/<int:id>/",book_detail,name="book")
]