from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from . import views
app_name = 'products'

urlpatterns = [
    path('', views.ProductHome.as_view(), name='homepage'),
    path('products/list/', views.ProductList.as_view(), name='list_of_product'),
    path('products/list/<int:product_id>/', views.ProductDetail, name='productdetail'),
    path('products/add/', views.Product_Addition.as_view(), name='product_add'),
    path('login/', LoginView.as_view(), name="login"),
    path('products/list/<int:product_id>/login/', LoginView.as_view(), name="detail_login"),
    path('products/list/<int:product_id>/logout/', LogoutView.as_view(), name="detail_logout"),
    path('products/list/login/', LoginView.as_view(), name="list_login"),
    path('products/list/logout/', LogoutView.as_view(), name="list_logout"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)