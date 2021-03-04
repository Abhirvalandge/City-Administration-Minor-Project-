"""City_Admnistration_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from City_Admnistration_Project import settings
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.ShowIndex,name="index"),
    path('loginindex', views.loginIndex, name="loginindex"),

    path('login/',views.ShowLogin,name="login"),
    path('adminlogin/',views.AdminLogin,name="adlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

    path('main_administrator/', views.main_Administrator, name="main_administrator"),
    path('administrator/',views.ShowAdministrator,name="administrator"),
    path('reg_details/',views.ShowRegDetails,name="reg_details"),
    path('save_details/', views.SaveRegDetails, name="save_details"),
    path('ap_shareidea/',views.ap_shareidea,name="ap_shareidea"),
    path('ap_issuecomplaint/',views.ap_issuecomplaint,name="ap_issuecomplaint"),
    path('ap_givesuggestion/',views.ap_givesuggestion,name="ap_givesuggestion"),


    path('citizenlogin/',views.CitizenLogin,name="citilogin"),
    path('citizen_logout/', views.citizen_logout, name="logout"),
    path('get_citizenlogin/',views.get_CitizenLogin,name="get_citilogin"),
    path('registeration/',views.ShowRegistration,name="registeration"),

    path('aboutus/',views.ShowAboutUs,name="aboutus"),

    path('contactus/',views.ShowContactUs,name="contactus"),

    path('citizenservice/',views.ShowCitizenService,name="citizenservice"),

    path('popup_login_shareIdea/', views.Popup_Login_ShareIdea, name="popup_login_shareIdea"),
    path('shareIdea/',views.ShowShareIdea,name="shareIdea"),
    path('get_shareIdea/', views.get_ShareIdea, name="get_shareIdea"),

    path('issueComp/',views.ShowIssueCompaint,name="issueComp"),
    path('popup_login_issuecomplaint/', views.Popup_Login_IssueComplaint, name="popup_login_issuecomplaint"),
    path('get_issuecomplaint/', views.get_IssueCompaint, name="get_issuecomplaint"),

    path('giveSuggestion/',views.ShowGiveSuggestion,name="giveSugg"),
    path('popup_login_givesuggestion/', views.Popup_Login_GiveSuggestion, name="popup_login_givesuggestion"),
    path('showgiveSuggestion_InputFields/', views.Show_GiveSuggestion_InputFields, name="showgiveSugg_InputFields"),
    path('get_givesuggestion/', views.get_GiveSuggestion, name="get_givesuggestion"),

    path('publishproject/',views.PublishProject,name="publishproject"),
    path('get_publishproject/', views.get_PublishProject, name="get_publishproject"),
    path('DeleteProject/', views.DeleteProject, name="deleteproject"),
    path('ad_deleteproject/', views.ad_deleteproject, name="ad_deleteproject"),

    #path('myaccount/', views.myaccount, name="myaccount"),
    path('profile/', views.ad_deleteproject, name="profile"),
    #path('profile_update/', views.profileUpdate, name="profile_update"),
    #path('get_profile_update/', views.getProfileUpdate, name="get_profile_update"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
