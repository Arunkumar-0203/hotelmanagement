from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

from hotel_app.models import Manager, Rooms, Reservation, customer, facility, RoomType, payment


class IndexView(TemplateView):
    template_name = 'manager/manager_index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        idd = User.objects.get(id=self.request.user.id)
        hotel = Manager.objects.filter(hotel__Status='active',Userr_id=idd)
        print(hotel)
        context['h']=hotel
        print(hotel)
        return context

class ViewDetails(TemplateView):
    template_name = 'manager/view_hoteldetails.html'
    def get_context_data(self, **kwargs):
        context = super(ViewDetails,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        print(id)
        d = Rooms.objects.filter(HOTEL_id=id,status='1')
        context['D']= d
        print(d)
        return context

class ViewRequest(TemplateView):
    template_name = 'manager/view_request.html'
    def get_context_data(self, **kwargs):
        context = super(ViewRequest,self).get_context_data(**kwargs)
        id=self.request.user.id
        # print(id)
        # manager = Manager.objects.get(Userr=id)
        # print(manager)
        # hotl = manager.hotel
        # print(hotl)
        # Hotel = Rooms.objects.filter(HOTEL_id=hotl,status=1)
        # print(Hotel)
        #
        # # idd = Reservation.objects.get(users_id=self.request.user.id)
        # # print(idd)
        reserve = Reservation.objects.filter(status1='1',status='wait for response',manager=id)
        print(reserve)
        context['Reserve']=reserve
        return context

class ViewuserDetails(TemplateView):
    template_name = 'manager/view_details.html'
    def get_context_data(self, **kwargs):
        context = super(ViewuserDetails,self).get_context_data(**kwargs)
        # idd = User.objects.get(id=self.request.user.id)
        # print(idd)
        id=self.request.GET['id']
        reserve = Reservation.objects.filter(users_id=id,status1=1)
        print(reserve)
        context['Reserve']=reserve
        return context

class ApproveView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=Reservation.objects.get(id=id)
        user.status='Rooms available'
        user.save()
        return render(request,'manager/manager_index.html',{'message':"Approved"})
#
class RejectView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=Reservation.objects.get(id=id)
        user.status='Room is not available'
        # user.status1='Rooms available'
        user.save()
        return render(request,'manager/manager_index.html',{'message':" Rejected"})


class ViewCustomers(TemplateView):
    template_name = 'manager/view_customers.html'
    def get_context_data(self, **kwargs):
        context = super(ViewCustomers,self).get_context_data(**kwargs)
        user = customer.objects.filter(user__last_name='1',user__is_staff='0')
        context['u']=user
        return context

class ViewFacilities(TemplateView):
    template_name = 'manager/view_facility.html'
    def get_context_data(self, **kwargs):
        context = super(ViewFacilities,self).get_context_data(**kwargs)
        F=facility.objects.filter(status=1)
        print(F)
        context['f']=F
        return context

class ViewBooking(TemplateView):
    template_name = 'manager/view_bookingrecord.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBooking,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id)
        print(id)
        M=Manager.objects.get(Userr_id=id)
        f = Reservation.objects.filter()

        pay = payment.objects.filter(MANAGER_id=M.id)
        for i in pay:
           P=i.price
           s = i.status
        # print(P)
           context['F']= f
           context['PAY']= P
           context['S']= s
        # print(f)
        return context