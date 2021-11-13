from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name='shop'),
    path("about",views.about, name='AboutUs'),
    path("contact",views.contact, name='ContactUs'),
    path("tracker",views.tracker, name='TrackingStatus'),
    path("search",views.search, name='search'),
    path("productview",views.productView, name='shop'),
    path("checkout/",views.checkout, name='checkout'),
    path("data/",views.data, name='data'),
    path("djangoTerms/", views.terms, name='terms')
]
