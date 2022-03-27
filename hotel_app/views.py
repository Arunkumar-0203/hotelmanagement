from django.contrib.auth import login
from django.contrib.auth.models import auth, User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from hotel_app.models import customer, UserType, Hotelss, Rooms


class IndexView(TemplateView):
    template_name = 'index.html'
    user =User.objects.get(id=1)
    user.last_name=1
    user.save()
    # def get_context_data(self, **kwargs):
    #     context = super(IndexView,self).get_context_data(**kwargs)
    #     hotel = Hotelss.objects.filter(Status='active')
    #     user =User.objects.filter(id=1)
    #     user.last_name=1
    #     user.save()
    #     print(hotel)
    #     context['h']=hotel
    #     print(hotel)
    #     return context
class ViewDetails(TemplateView):
    template_name = 'view_details.html'
    def get_context_data(self, **kwargs):
        context = super(ViewDetails,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        print(id)
        d = Rooms.objects.filter(HOTEL_id=id,status='1')
        context['D']= d
        print(d)
        return context

class LoginView(TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        username = request.POST['Username']
        password= request.POST['Password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "manager":
                    return redirect('/manager')
                # elif UserType.objects.get(user_id=user.id).type == "delivery":
                #     return redirect('/delivery')

            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})


class RegisterView(TemplateView):
    template_name = 'registration.html'
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
        state = request.POST['State']
        district = request.POST['District']
        try:
            user = User.objects.create_user(first_name = first_name,email=Email,password=password,username=username,last_name=0)
            user.save()
            c= customer()
            c.user=user
            c.contact = Phone
            c.emil =Email
            c.district = district
            c.nation = state
            c.dob = DOB
            c.id_proof = file
            c.place = Place
            c.Address = addr
            c.status = 'active'
            c.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            return redirect('Register')
        except:
             messages = "Enter Another Username"
             return render(request,'index.html',{'messages':messages})






