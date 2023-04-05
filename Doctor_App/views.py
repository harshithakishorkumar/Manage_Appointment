from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db import connection

# Create your views here.


def Home(request):
	return render(request,"Home.html",{})

def Admin_Login(request):
	if request.method == "POST":
		A_username = request.POST['aname']
		A_password = request.POST['apass']
		if AdminDetails.objects.filter(username = A_username,password = A_password).exists():
			ad = AdminDetails.objects.get(username=A_username, password=A_password)
			print('d')
			messages.info(request,'Admin login is Sucessfull')
			request.session['type_id'] = 'Admin'
			request.session['UserType'] = 'Admin'
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			print('y')
			messages.error(request, 'Error wrong username/password')
			return render(request, "Admin_Login.html", {})
	else:
		return render(request, "Admin_Login.html", {})


def Manage_Doctor(request):
	details = Doctor.objects.all()
	return render(request,"Manage_Doctor.html",{'details':details})

def Doctor_Login(request):
	if request.method == "POST":
		C_name = request.POST['username']
		C_password = request.POST['password']
		if Doctor.objects.filter(username=C_name, password=C_password).exists():
			users = Doctor.objects.all().filter(username=C_name, password=C_password)
			messages.info(request,'Dr. '+C_name+ ' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'Doctor'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			messages.error(request, 'Admin has not registered you')
			return redirect("/Doctor_Login")
	else:
		return render(request,'Doctor_Login.html',{})
	return render(request,'Doctor_Login.html',{})

def Add_Doctor(request):
	if request.method == "POST":
		Name = request.POST['Name']
		Age= request.POST['Age']
		Gender= request.POST['Gender']
		Phone= request.POST['phone']
		Address= request.POST['Address']
		Speciality= request.POST['Speciality']
		Username= request.POST['username']
		Password= request.POST['Password']
		obj = Doctor(
								Name=Name
								,Age=Age
								,Gender=Gender
								,Phone=Phone
								,Address=Address
								,Speciality=Speciality
								,username=Username
								,password=Password)
		obj.save()
		messages.info(request,Name +" Registered")
		return redirect("/Manage_Doctor/")
	else:
		return render(request,"Add_Doctor.html",{})

def Doctor_Change_Password(request):
	Userid = request.session['UserId']
	if request.method == "POST":
		newpass = request.POST['new_pass']
		confirm = request.POST['confirm_pass']
		if newpass == confirm:
			Doctor.objects.filter(id=Userid).update(password=newpass)
			messages.info(request,'Password changed')
			details = Doctor.objects.filter(id=Userid)
			return render(request,'Doctor_Change_Password.html',{'details':details})
		else:
			messages.info(request,'Passwords dont match')
			return redirect('/Doctor_Change_Password')
	else:
		Userid = request.session['UserId']
		details = Doctor.objects.filter(id=Userid)
		return render(request,'Doctor_Change_Password.html',{'details':details})

	return render(request,"Doctor_Change_Password.html",{})

def Update_Doctor(request):
	if request.method == "POST":
		Doc_Id = request.POST['viewid']
		Name=request.POST['viewname']
		Name =Name.strip()
		Age=request.POST['viewage']
		Gender=request.POST['viewgender']
		Phone=request.POST['viewphone']
		Address=request.POST['viewadd']
		Speciality=request.POST['viewmed']
		Age =Age.strip()
		Gender =Gender.strip()
		Phone =Phone.strip()
		Address =Address.strip()
		Speciality =Speciality.strip()
		Doctor.objects.filter(id=Doc_Id).update(
															Name=Name
															,Age=Age
															,Gender=Gender
															,Phone=Phone
															,Address=Address
															,Speciality=Speciality
			)
		messages.info(request,"Doctor Details Updated")
		return redirect('Manage_Doctor')
	else:
		return render(request,"Manage_Doctor.html",{})

def Patient_Login(request):
	if request.method == "POST":
		C_name = request.POST['username']
		C_password = request.POST['password']
		if Patient_Details.objects.filter(Username=C_name, Password=C_password).exists():
			users = Patient_Details.objects.all().filter(Username=C_name, Password=C_password)
			messages.info(request,C_name+ ' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'User'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			return redirect("/")
		else:
			messages.error(request, 'Please Register')
			return redirect("/Patient_Registeration")
	else:
		return render(request,'Patient_Login.html',{})
	return render(request,'Patient_Login.html',{})

def Patient_Registeration(request):
	if request.method == "POST":
		Name = request.POST['Name']
		Age= request.POST['Age']
		Gender= request.POST['Gender']
		Phone= request.POST['phone']
		Address= request.POST['Address']
		Medication= request.POST['Medication']
		Username= request.POST['username']
		Password= request.POST['Password']
		obj = Patient_Details(
								Name=Name
								,Age=Age
								,Gender=Gender
								,Phone=Phone
								,Address=Address
								,Medication=Medication
								,Username=Username
								,Password=Password)
		obj.save()
		messages.info(request,Name +" Registered")
		return redirect("/Patient_Login/")
	else:
		return render(request,"Patient_Registeration.html",{})


def Patient_Profile(request):
	Userid = request.session['UserId']
	details = Patient_Details.objects.all().filter(id=Userid)
	return render(request,"Patient_Profile.html",{'details':details})


def Patient_Change_Password(request):
	Userid = request.session['UserId']
	if request.method == "POST":
		newpass = request.POST['new_pass']
		confirm = request.POST['confirm_pass']
		if newpass == confirm:
			Patient_Details.objects.filter(id=Userid).update(Password=newpass)
			messages.info(request,'Password changed')
			details = Patient_Details.objects.filter(id=Userid)
			return render(request,'Patient_Change_Password.html',{'details':details})
		else:
			messages.info(request,'Passwords dont match')
			return redirect('/Patient_Change_Password')
	else:
		Userid = request.session['UserId']
		details = Patient_Details.objects.filter(id=Userid)
		return render(request,'Patient_Change_Password.html',{'details':details})

	return render(request,"Patient_Change_Password.html",{})

def Doctor_Profile(request):
	Userid = request.session['UserId']
	details = Doctor.objects.all().filter(id=Userid)
	return render(request,"Doctor_Profile.html",{'details':details})

def Delete_Doctor(request,id):
	Doctor.objects.filter(id=id).delete()
	return redirect('Manage_Doctor')

def New_Booking(request):
	if request.method == "POST":
		Doctor_ID = request.POST['updateid']
		print(Doctor_ID)
		slot = request.POST['slot']
		date = request.POST['date']
		print('Slot: '+slot)
		print('date: '+date)
		Patient_Id = Userid = request.session['UserId']
		if Booking.objects.filter(Doctor_Id=Doctor_ID,Patient_Id=Patient_Id,Slot=slot,Date=date).exists():
			messages.info(request,"You have already booked an appointment for following date and time")
		else:
			obj = Booking(Doctor_Id=Doctor_ID
						,Patient_Id=Patient_Id
						,Slot=slot
						,Date=date)
			obj.save()
			messages.info(request,"Booking Confirmed")
	details = Doctor.objects.all()
	return render(request,"New_Booking.html",{'details':details})

def Booking_History(request):
	Patient_Id = Userid = request.session['UserId']
	details = Booking.objects.all().filter(Patient_Id=Patient_Id)
	return render(request,"Booking_History.html",{'details':details})

def Delete_Apt(request,id):
	Booking.objects.filter(id=id).delete()
	return redirect('/Booking_History/')

def Search_Doctor(request):
	if request.method =="POST":
		searched = request.POST['searched']
		searched = str(searched)
		print(searched)
		if searched:
			details = Doctor.objects.filter(Name__icontains=searched)|Doctor.objects.filter(Speciality__icontains=searched)|Doctor.objects.filter(Address__icontains=searched)
			return render(request,"Search_Doctor.html",{'details':details,'searched':searched})
		else:
			return render(request,"Search_Doctor.html",{})
	else:
	 	return render(request,"Search_Doctor.html",{})

def Post_Feedback(request):
	if request.method == "POST":
		Patient_Id = request.session['UserId']
		feedback =  request.POST['feedback']
		obj = Feedback(Patient_Id=Patient_Id,Feedback=feedback)
		obj.save()
		messages.info(request,"Feedback Submitted")
		return redirect('/Post_Feedback/')
	else:
		return render(request,"Post_Feedback.html",{})

def View_Treatment(request):
	Patient_Id = request.session['UserId']
	details = Booking.objects.all().filter(Patient_Id=Patient_Id)
	return render(request,"View_Treatment.html",{'details':details})

def View_Appointments(request):
	if request.method =="POST":
		searched = request.POST['searched']
		searched = str(searched)
		print(searched)
		if searched:
			details = Booking.objects.filter(Date__icontains=searched)
			return render(request,"View_Appointments.html",{'details':details,'searched':searched})
		else:
			doc_id = request.session['UserId']
			Info = Booking.objects.all().filter(Doctor_Id=doc_id)
			return render(request,'View_Appointments.html',{'Info':Info})
	else:
		doc_id = request.session['UserId']
		Info = Booking.objects.all().filter(Doctor_Id=doc_id)
		return render(request,'View_Appointments.html',{'Info':Info})

def View_Patient(request,Patient_Id):
	info = Patient_Details.objects.filter(id =Patient_Id)
	for a in info:
		name = info[0].Name
		print(name)
	return render(request,"View_Patient.html",{'info':info})

def Add_Treatment(request):
	if request.method == "POST":
		Booking_Id = request.POST['viewid']
		Patient_id = request.POST['viewname']
		Treatment = request.POST['viewphone']
		searched = request.POST['searched']
		Booking.objects.filter(id=Booking_Id).update(Treatment=Treatment)
		return render(request,"View_Appointments.html",{'searched':searched})
	else:
		return render(request,"View_Appointments.html",{})

def Doctor_ViewPatients(request):
	if request.method =="POST":
		searched = request.POST['searched']
		searched = str(searched)
		print(searched)
		if searched:
			details = Patient_Details.objects.filter(id__icontains=searched)|Patient_Details.objects.filter(Name__icontains=searched)
			return render(request,"Doctor_ViewPatients.html",{'details':details,'searched':searched})
		else:
			details = Patient_Details.objects.all()
			return render(request,"Doctor_ViewPatients.html",{'details':details})
	else:
		details = Patient_Details.objects.all()
		return render(request,"Doctor_ViewPatients.html",{'details':details})

def Doctor_ViewTreatment(request,id):
	details = Booking.objects.all().filter(Patient_Id=id)
	info = Patient_Details.objects.filter(id=id)
	for i in info:
		name = info[0].Name
	return render(request,'Doctor_ViewTreatment.html',{'details':details,'name':name})

def View_AppointmentAdmin(request):
	if request.method =="POST":
		searched = request.POST['searched']
		searched = str(searched)
		print(searched)
		if searched:
			details = Booking.objects.filter(Date__icontains=searched)
			return render(request,"View_AppointmentAdmin.html",{'details':details,'searched':searched})
		else:

			Info = Booking.objects.all()
			return render(request,'View_AppointmentAdmin.html',{'Info':Info})
	else:
		
		Info = Booking.objects.all()
		return render(request,'View_AppointmentAdmin.html',{'Info':Info})

def View_Feedback(request):
	details = Feedback.objects.all()
	return render(request,"View_Feedback.html",{'details':details})

def Logout(request):
	Session.objects.all().delete()
	return redirect("/")
