from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
				path('',views.Home,name="Home"),
				path('Admin_Login/',views.Admin_Login,name="Admin_Login"),
				path('Manage_Doctor/',views.Manage_Doctor,name="Manage_Doctor"),
				path('Add_Doctor/',views.Add_Doctor,name="Add_Doctor"),
				path('Doctor_Login/',views.Doctor_Login,name="Doctor_Login"),
				path('Delete_Doctor/<int:id>',views.Delete_Doctor,name="Delete_Doctor"),
				path('Doctor_Profile/',views.Doctor_Profile,name="Doctor_Profile"),
				path('Doctor_Change_Password/',views.Doctor_Change_Password,name="Doctor_Change_Password"),
				path('Update_Doctor/',views.Update_Doctor,name="Update_Doctor"),
				path('Patient_Login/',views.Patient_Login,name="Patient_Login"),
				path('Patient_Registeration/',views.Patient_Registeration,name="Patient_Registeration"),
				path('Patient_Profile/',views.Patient_Profile,name="Patient_Profile"),
				path('Patient_Change_Password/',views.Patient_Change_Password,name="Patient_Change_Password"),
				path('New_Booking/',views.New_Booking,name="New_Booking"),
				path('Booking_History/',views.Booking_History,name="Booking_History"),
				path('Delete_Apt/<int:id>',views.Delete_Apt,name="Delete_Apt"),
				path('Search_Doctor/',views.Search_Doctor,name="Search_Doctor"),
				path('Post_Feedback/',views.Post_Feedback,name="Post_Feedback"),
				path('View_Treatment/',views.View_Treatment,name="View_Treatment"),
				path('View_Appointments/',views.View_Appointments,name="View_Appointments"),
				path('View_Patient/<int:Patient_Id>',views.View_Patient,name="View_Patient"),
				path('Add_Treatment/',views.Add_Treatment,name="Add_Treatment"),
				path('Doctor_ViewPatients/',views.Doctor_ViewPatients,name="Doctor_ViewPatients"),
				path('Doctor_ViewTreatment/<int:id>',views.Doctor_ViewTreatment,name="Doctor_ViewTreatment"),
				path('View_AppointmentAdmin/',views.View_AppointmentAdmin,name="View_AppointmentAdmin"),
				path('View_Feedback/',views.View_Feedback,name="View_Feedback"),
				path('Logout/',views.Logout,name="Logout"),
				

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)