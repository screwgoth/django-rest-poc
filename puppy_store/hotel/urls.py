from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/hotels/categories/$',
        views.get_hotel_categories,
        name='get_hotel_categories'
    ),
    url(
        r'^api/v1/hotels/collections/$',
        views.get_hotel_collections,
        name='get_hotel_collections'
    )
]
