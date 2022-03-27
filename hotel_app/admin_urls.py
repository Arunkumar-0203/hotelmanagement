
from django.contrib import admin
from django.urls import path

from hotel_app.admin_views import IndexView, ViewUsers, ApproveView, RejectView, UserView, AddhotelView, AddmangerView, \
    ManagerView, RejectmanagerView, HotelView, RoomView, RoomReject, AddFacility, FacilityReject, RoomdetailReject, \
    ViewBooking, HotelsRemove

urlpatterns = [

    path('',IndexView.as_view()),
    path('i',IndexView.as_view()),
    path('newusers',ViewUsers.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('users',UserView.as_view()),
    path('hotels',AddhotelView.as_view()),
    path('managers',AddmangerView.as_view()),
    path('newmanagers',ManagerView.as_view()),
    path('rejects',RejectmanagerView.as_view()),
    path('hoteldetails',HotelView.as_view()),
    path('roomtype',RoomView.as_view()),
    path('rejectss',RoomReject.as_view()),
    path('rejectsss',FacilityReject.as_view()),
    path('facility',AddFacility.as_view()),
    path('rejectt',RoomdetailReject.as_view()),
    path('booking',ViewBooking.as_view()),
    path('remove',HotelsRemove.as_view()),




]
def urls():
    return urlpatterns, 'admin', 'admin'