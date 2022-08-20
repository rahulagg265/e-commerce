from django.urls import path
from rapp import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('',views.store,name='store'),
    # path('store',views.store,name='store'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('updateitem',views.updateitem,name='updateitem'),
    path('processorder',views.processorder,name='processorder'),
    path('payment',views.payment,name='payment'),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  