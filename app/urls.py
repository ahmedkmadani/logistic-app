from . import views
from django.urls import path
from .views.login import login
from .views.index import index
from .views.buisness import buisness
from .views.driver import driver
from .views.order import order, update_order
from .views.region import region
from .views.neighborhood import neighborhood
from .views.buisness import get_neighborhoods
from .views.shipment import shipment, update_shipment
from .api.order import get_order_details, assgin_driver_order, get_driver_shipment, deliver_shipment

urlpatterns = [
    path("", view=login, name="login"),
    path("index", view=index, name="index"),
    path("buisness", view=buisness, name="buisness"),
    path("driver", view=driver, name="driver"),
    path("order", view=order, name="order"),
    path("shipment", view=shipment, name="shipment"),
    path("update_order/<int:pk>/", view=update_order, name="update_order"),
    path("update_shipment/<int:pk>/", view=update_shipment, name="update_shipment"),
    path("region", view=region, name="region"),
    path("neighborhood", view=neighborhood, name="neighborhood"),
    path("get_neighborhoods/", get_neighborhoods, name="get_neighborhoods"),
    path("api/orders/<str:order_number>/", get_order_details, name="get_order_details"),
    path(
        "api/orders_driver/<str:order_number>/<int:driver_id>",
        assgin_driver_order,
        name="assgin_driver_order",
    ),
     path(
        "api/shipment_driver/<int:driver_id>",
        get_driver_shipment,
        name="get_driver_shipment",
    ),
      path(
        "api/deliver_shipment/<str:order_number>/",
        deliver_shipment,
        name="deliver_shipment",
    ),
]
