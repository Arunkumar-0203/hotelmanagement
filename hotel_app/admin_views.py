from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from hotel_app.models import customer, Hotelss, UserType, Manager, RoomType, facility, Rooms, Reservation, payment


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class ViewUsers(TemplateView):
    template_name = 'admin/view_users.html'
    def get_context_data(self, **kwargs):
        context = super(ViewUsers,self).get_context_data(**kwargs)
        user = customer.objects.filter(user__last_name='0',user__is_staff='0')
        context['u']=user
        return context

class ApproveView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=User.objects.get(id=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class RejectView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=User.objects.get(id=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class UserView(TemplateView):
    template_name = 'admin/users.html'
    def get_context_data(self, **kwargs):
        context = super(UserView,self).get_context_data(**kwargs)
        user = customer.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['User'] = user

        return context

class AddhotelView(TemplateView):
    template_name = 'admin/add_hotels.html'
    def get_context_data(self, **kwargs):
        context = super(AddhotelView,self).get_context_data(**kwargs)
        hotel = Hotelss.objects.filter(Status='active')
        print(hotel)
        context['h']=hotel
        return context
    def post(self,request,*args,**kwargs):
        Name = request.POST['name']
        img =  request.FILES['imge']

        f = FileSystemStorage()

        file = f.save(img.name, img)
        Place = request.POST['place']
        H = Hotelss()
        H.Name=Name
        H.Image = file
        H.Status = 'active'
        H.Place = Place
        H.save()
        return redirect(request.META['HTTP_REFERER'])

class AddmangerView(TemplateView):
    template_name = 'admin/add_manager.html'
    def get_context_data(self, **kwargs):
        context = super(AddmangerView,self).get_context_data(**kwargs)
        hotel = Hotelss.objects.filter(Status='active',status1='0')
        print(hotel)
        context['h']=hotel
        return context
    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        password = request.POST['password']
        Email = request.POST['email']
        Phone = request.POST['phone']
        DOB = request.POST['Dob']
        addr = request.POST['address']

        first_name =request.POST['first_name']
        Place = request.POST['place']
        image= request.FILES['proof']
        f = FileSystemStorage()
        file = f.save(image.name, image)
        H = request.POST['hotel']
        print(H)
        district = request.POST['District']
        try:
            user = User.objects.create_user(first_name = first_name,email=Email,password=password,username=username,last_name=1)
            user.save()
            m= Manager()
            m.Userr=user
            m.Contact = Phone
            m.Emil =Email
            m.District = district

            m.Dob = DOB
            m.Id_proof = file
            m.Place = Place
            m.Address = addr
            h = Hotelss.objects.get(id=H)
            h.status1 = '1'
            h.save()
            m.hotel_id = H
            m.status = 'active'
            m.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "manager"
            usertype.save()
            return redirect('Register')
        except:
             messages = "Enter Another Username"
             return render(request,'admin/admin_index.html',{'messages':messages})

class ManagerView(TemplateView):
    template_name = 'admin/view_manager.html'
    def get_context_data(self, **kwargs):
        context = super(ManagerView,self).get_context_data(**kwargs)
        u = Manager.objects.filter(Userr__last_name='1',Userr__is_staff='0',Userr__is_active='1')
        context['u'] = u

        return context

class RejectmanagerView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']

        user=User.objects.get(id=id)
        m = Manager.objects.get(Userr_id=id)
        H = Hotelss.objects.get(id=m.hotel_id)
        H.status1='0'
        H.save()
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/view_manager.html',{'message':"Account Removed"})

class HotelView(TemplateView):
    template_name = 'admin/add_hoteldetails.html'
    def get_context_data(self, **kwargs):

        context = super(HotelView,self).get_context_data(**kwargs)
        ID = self.request.GET['id']
        print(ID)
        R = RoomType.objects.filter(status='1',Hotel_id=ID)
        D = Rooms.objects.filter(status='1',HOTEL_id =ID)
        context['r']=R
        context['d']=D
        return context
    def post(self,request,*args,**kwargs):
        Id = request.GET['id']
        print("dsdfdfdfd",Id)
        p = request.POST['price']
        print(p)
        t = request.POST['type']
        T = request.POST['numbers']
        room = Rooms()
        room.status = '1'
        room.HOTEL_id = Id
        room.Price = p
        room.total = T
        room.roomtype_id = t
        room.save()
        return redirect(request.META['HTTP_REFERER'])





class RoomView(TemplateView):
    template_name = 'admin/add_Room.html'
    def get_context_data(self, **kwargs):
        context = super(RoomView,self).get_context_data(**kwargs)
        hotel = Hotelss.objects.all()
        R = RoomType.objects.filter(status='1')
        context['h']=hotel
        context['r']=R
        return context


    def post(self,request,*args,**kwargs):
        Name = request.POST['name']
        D  = request.POST['details']
        Ima =request.FILES['img']
        H = request.POST['hotel']
        print("1111111111111",H)
        R = RoomType()
        R.roomtype = Name
        R.images = Ima
        R.Details = D
        R.status = '1'
        R.Hotel_id = H
        R.save()
        return redirect(request.META['HTTP_REFERER'])

class RoomReject(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        hotel =RoomType.objects.get(id=id)
        hotel.status = '0'
        hotel.save()
        return redirect(request.META['HTTP_REFERER'])

class RoomdetailReject(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        hotel =Rooms.objects.get(id=id)
        hotel.status = '0'
        hotel.save()
        return redirect(request.META['HTTP_REFERER'])

class AddFacility(TemplateView):
    template_name = 'admin/add_facility.html'
    def get_context_data(self, **kwargs):
        context = super(AddFacility,self).get_context_data(**kwargs)
        hotels = Hotelss.objects.all()
        R = facility.objects.filter(status='1')
        context['H']=hotels
        context['r']=R
        return context
    def post(self,request,*args,**kwargs):
        Name = request.POST['name']
        p = request.POST['Price']
        F = facility()
        F.price = p
        F.status = '1'
        F.Facility = Name
        F.save()
        return redirect(request.META['HTTP_REFERER'])

class FacilityReject(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        hotel =facility.objects.get(id=id)
        hotel.status = '0'
        hotel.save()
        return redirect(request.META['HTTP_REFERER'])
class ViewBooking(TemplateView):
    template_name = 'admin/view_bookingrecord.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBooking,self).get_context_data(**kwargs)
        # id = User.objects.get(id=self.request.user.id)
        f = Reservation.objects.filter()
        pay = payment.objects.all()
        for i in pay:

         P=i.price
         s = i.status
         print(P)
         context['F']= f
         context['PAY']= P
         context['S']= s
         # print(f)
        return context
class HotelsRemove(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        hotel =Hotelss.objects.get(id=id)
        hotel.Status = '0'
        hotel.save()
        return redirect(request.META['HTTP_REFERER'])