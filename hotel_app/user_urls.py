from django.urls import path

from hotel_app.user_views import IndexView, ViewDetails, ViewRoom, RejectBocking, FacilityView, CheckoutView, \
    ViewaddedFacility, Viewbooking, VaccatedRoom

urlpatterns=[
    path('',IndexView.as_view()),
    path('t',IndexView.as_view()),
    path('details',ViewDetails.as_view()),
    path('rooms',ViewRoom.as_view()),
    path('reject',RejectBocking.as_view()),
    path('facility',FacilityView.as_view()),
    path('checkout',CheckoutView.as_view()),
    path('facilityy',ViewaddedFacility.as_view()),
    path('booking',Viewbooking.as_view()),
    path('vaccated',VaccatedRoom.as_view())


]
def urls():
    return urlpatterns, 'user', 'user'