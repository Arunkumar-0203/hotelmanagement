import datetime

from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from hotel_app.models import Hotelss, Rooms, facility, Reservation, facilityselected, customer, payment, Manager


class IndexView(TemplateView):
    template_name = 'customer/user_index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        hotel = Hotelss.objects.filter(Status='active')
        print(hotel)
        context['h']=hotel
        print(hotel)
        return context

class ViewDetails(TemplateView):
    template_name = 'customer/view_details.html'
    def get_context_data(self, **kwargs):
        context = super(ViewDetails,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        print(id)
        d = Rooms.objects.filter(HOTEL_id=id,status='1')
        context['D']= d
        print(d)
        return context

class ViewRoom(TemplateView):
    template_name = 'customer/viewroom_details.html'
    def get_context_data(self, **kwargs):
        context = super(ViewRoom,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id)
        idd = self.request.GET['id']
        # print(idd)
        f = Reservation.objects.filter(users_id=id,ROOM_id=idd,status1=1)
        fc = facility.objects.filter(status='1')
        context['FC']=fc
        context['F']= f
        # print(f)
        return context
    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        rooms = Rooms.objects.get(id=id)
        # print(rooms)
        hot = rooms.HOTEL_id
        M = Manager.objects.get(hotel_id=hot)
        m = M.Userr.id

        CUSTOMER = customer.objects.get(user_id=self.request.user.id)
        # print(CUSTOMER)
        customers = User.objects.get(id=self.request.user.id)
        pay = payment.objects.filter(userr_id=self.request.user.id)


        ch_date = request.POST['in_date']
        ch_time =  request.POST['in_time']
        out_d =  request.POST['out_date']
        out_t =  request.POST['out_time']
        rsv = Reservation()

        rsv.ROOM_id = id
        rsv.users = customers
        rsv.manager = m

        rsv.check_in_date = ch_date
        rsv.Customer_id = CUSTOMER.id
        rsv.check_in_time = ch_time
        rsv.check_out_date = out_d
        rsv.check_out_time = out_t
        rsv.status ='wait for response'
        rsv.status1 = '1'
        rsv.status2 = 'room tacked'
        f = Reservation.objects.filter(users_id=self.request.user.id)
        for i in f:
            if i.status2=="room tacked":
                return render(request,'customer/user_index.html',{'message':"this user allready room booked vacate after book"})
        rsv.save()
        return redirect(request.META['HTTP_REFERER'])

class RejectBocking(TemplateView):
     def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=Reservation.objects.get(id=id)
        user.status1='0'
        user.save()
        return redirect(request.META['HTTP_REFERER'])

class FacilityView(TemplateView):
    template_name = 'customer/add_facility.html'
    def get_context_data(self, **kwargs):
        context = super(FacilityView,self).get_context_data(**kwargs)
        fc = facility.objects.filter(status='1')
        idd = User.objects.get(id=self.request.user.id)
        id = self.request.GET['id']
        selectedfc =facilityselected.objects.filter(statuss='1',Users_id=idd,Reserve_id=id)
        print(selectedfc)

        # x=0
        # for us in selectedfc:
        #     x=list(us.facilityy)
        # #     # print(x)
        # #     # for i in x:
        # #     #   print(i)
        context['selctfc']= selectedfc
        # print(type(x))
        context['fc']=fc
        return context
    def post(self,request,*args,**kwargs):
        id=request.GET['id']
        user = User.objects.get(id=self.request.user.id)

        f = request.POST.getlist('i')
        # print(type(f))
        F =facilityselected()
        F.facilityy = f
        F.Reserve_id = id
        F.Users = user
        F.statuss = "1"
        F.save()
        return redirect(request.META['HTTP_REFERER'])


class ViewaddedFacility(TemplateView):
    template_name = 'customer/added_facility.html'
    def get_context_data(self, **kwargs):
        context = super(ViewaddedFacility,self).get_context_data(**kwargs)
        idd = User.objects.get(id=self.request.user.id)
        id = self.request.GET['id']
        print(id)
        selectedfcc =facilityselected.objects.filter(statuss='1',Users_id=idd)
        print(selectedfcc)
        x=0
        for us in selectedfcc:
            x=list(us.facilityy)
            print(x)
            # for i in x:
            #   print(i)
        context['S']= x
        return context
        # print(type(x))

class CheckoutView(TemplateView):
    template_name ='customer/checkout.html'
    def get_context_data(self, **kwargs):
        id=self.request.GET['id']
        room = Rooms.objects.get(id=id)
        print(room)
        context = super(CheckoutView,self).get_context_data(**kwargs)
        faclty = facility.objects.filter(status="1")
        user = User.objects.get(id=self.request.user.id)
        reserve = Reservation.objects.filter(users_id=user,ROOM_id=id)
        selectedfc =facilityselected.objects.filter(Users_id=user,Reserve__ROOM_id=id)

        # print(faclty)
        T=0
        # x=0
        TOTAL=0
        for st in reserve:
          s = st.status
          s2 = st.status2
          if s=="Rooms available":

            for j in faclty:
               F = j.Facility
               for us in selectedfc:
                   x=list(us.facilityy)

                   for i in x:


                       if i==F:
                          Fc = facility.objects.get(Facility=i)

                          total = int(Fc.price)

                          T = int(T)+int(total)
            D=0
            print(T)
            R = room.Price
            R =int(T)+int(R)
            print(R)
            chin=st.check_in_date
            chout=st.check_out_date
            sd_obj = datetime.datetime.strptime(chin, '%Y-%m-%d')
            fd_obj = datetime.datetime.strptime(chout, '%Y-%m-%d')
            print(sd_obj)
            print(fd_obj)
            day = fd_obj - sd_obj
            print(day)
            d=day.days
            D = (d) *int(R)
            context['room']=D
            return context
          else:
              context['not']="ROOM NOT AVAILABLE"
              return context
    def post(self,request,*args,**kwargs):
        T = request.POST['t']
        idd = request.GET['id']
        # print(T)
        # print(idd)
        user = User.objects.get(id=self.request.user.id)
        C =Reservation.objects.get(users_id=user,ROOM_id=idd,status1=1)
        R=C.ROOM_id

        Rm = Rooms.objects.get(id=R)

        rm = Rm.HOTEL_id
        H = Hotelss.objects.get(id=rm)

        manager = Manager.objects.get(hotel_id=H)


        a=C.status
        b= C.status1
        print(b)
        Cc =C.status2

        if Cc=="room tacked":
          if a=="Rooms available":
            print("hi")
            if b=='1':

               pay = payment()
               pay.price = T
               pay.Customers_Id = user
               pay.MANAGER_id=manager.id
               pay.userr_id = user.id
               pay.room_id = idd
               pay.status = 'paid'
               pay.save()
               C.status1='0'

               C.save()
               room =Rooms.objects.get(id=idd)


               R=room.total
               print(R)
               Total = int(R)-1

               room.total=Total
               room.save()
            else:
                 return render(request,'customer/user_index.html',{'message':"room note available"})
          else:
              return render(request,'customer/user_index.html',{'message':"room note available"})
        else:
            return render(request,'customer/user_index.html',{'message':"user allready paid"})

        return render(request,'customer/user_index.html',{'message':"successfully paid"})



class Viewbooking(TemplateView):
    template_name = 'customer/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(Viewbooking,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id)
        f = Reservation.objects.filter( status="Rooms available",status1='0',users_id=id,status2="room tacked")
        print(f)
        pay = payment.objects.filter(status="paid",userr_id=id)
        print(pay)
        for i in pay:
          P=i.price
          s = i.status
          print(pay)
          context['PAY']= P
          context['pay']= pay
          context['S']= s
          context['F']= f


        return context

class VaccatedRoom(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']


        reserve = Reservation.objects.get(status2='room tacked',users_id=self.request.user.id)
        print(reserve)
        room = reserve.ROOM_id

        user=User.objects.get(id=self.request.user.id)
        pay = payment.objects.get(room_id=room,userr_id=user.id,status="paid")

        if pay.status=='paid':
          pay.status='Room Vaccated'
          pay.save()
          room =Rooms.objects.get(id=room)
          r=room.total
          reserve.status2="Room Vaccated"
          reserve.save()
          R=int(r)+1
          room.total=R
          room.save()
        else:
            return render(request,'customer/user_index.html',{'message':"Already Room Vaccated"})

        return render(request,'customer/user_index.html',{'message':"Room Vaccated"})








