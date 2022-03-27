from django.urls import path

from hotel_app.managers_view import IndexView, ViewDetails, ViewRequest, ViewuserDetails, ApproveView, RejectView, \
    ViewCustomers, ViewFacilities, ViewBooking

urlpatterns =[
    path('',IndexView.as_view()),
    path('D',IndexView.as_view()),
    path('details',ViewDetails.as_view()),
    path('request',ViewRequest.as_view()),
    path('Details',ViewuserDetails.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('Customers',ViewCustomers.as_view()),
    path('facility',ViewFacilities.as_view()),
    path('booking',ViewBooking.as_view())


]
def urls():
    return urlpatterns, 'manager', 'manager'