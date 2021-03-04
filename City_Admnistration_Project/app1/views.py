
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app1.models import RegistrationDataModel,ShareIdeaModel,CompIssueModel,PublishProjectModel,GiveSuggestionModel,ProfileImageModel

global emailid,password

def ShowIndex(request):
    try:
      return render(request,"index.html")
    except KeyError:
        return render(request,"admin.html")

def loginIndex(request):
    try:
        if request.session["emailid"]:
          return render(request,"login_index.html")
    except KeyError:
        return render(request,"citizen.html")

def ShowLogin(request):
    return render(request,"login.html")

def AdminLogin(request):
    return render(request,"admin.html")

def admin_logout(request):
   try:
      del request.session["emailid"]
      request.session.modified = True
      return redirect('index')
   except KeyError:
       return render(request, "admin.html")


def main_Administrator(request):
    return render(request,"administrator.html")

def ShowAdministrator(request):
    admin_id = request.POST.get("emailid")
    admin_pass = request.POST.get("password")

    if admin_id == "abhirva" and admin_pass == "landge":
       request.session["emailid"]=admin_id
       return render(request, "administrator.html")
    else:
        return render(request,"admin.html",{"message1" :"Invalid User"})

def ap_shareidea(request):
    try:
        if request.session["emailid"]:
          qs = ShareIdeaModel.objects.all()
          return render(request,"ap_shareidea.html",{"data":qs})
    except KeyError:
        return render(request,"admin.html")

def ap_issuecomplaint(request):
    try:
        if request.session["emailid"]:
          qs = CompIssueModel.objects.all()
          return render(request,"ap_issuecomplaint.html",{"data":qs})
    except KeyError:
        return render(request,"admin.html")


def ap_givesuggestion(request):
    try:
        if request.session["emailid"]:
           qs = GiveSuggestionModel.objects.all()
           return render(request,"ap_givesuggestion.html",{"data":qs})
    except KeyError:
        return render(request,"admin.html")


def ShowRegDetails(request):
    if request.session["emailid"]:
      qs = RegistrationDataModel.objects.all()
      return render(request,"reg_details.html", {"data": qs})

def ShowRegistration(request):
    try:
          return render(request,"registraion.html")
    except KeyError:
        return render(request,"admin.html")


def SaveRegDetails(request):
    if request.method == "POST":
       # Personal Detail
       name = request.POST.get("name")
       lname = request.POST.get("lname")
       fname = request.POST.get("fname")
       f_lname = request.POST.get("f_lname")
       dob = request.POST.get("dob")
       gender = request.POST.get("gender")
       nationality = request.POST.get("nationality")
       #Address Details
       houseno = request.POST.get("houseno")
       address = request.POST.get("address")
       city = request.POST.get("city")
       pin = request.POST.get("pin")
       state = request.POST.get("state")
       district = request.POST.get("district")
       # Contact Details
       mobileno = request.POST.get("mobileno")
       emailid = request.POST.get("emailid")
       password = request.POST.get("password")

       #To save a registration record into table
       RegistrationDataModel(name=name,lname=lname,f_lname=f_lname,fname=fname,dob=dob,
                             gender=gender,nationality=nationality,houseno=houseno,
                             address=address,city=city,pin=pin,state=state,district=district,
                             mobileno=mobileno,emailid=emailid,password=password).save()

       return render(request,"citizen.html",{"message":"Registration Successful"})

def CitizenLogin(request):
    return render(request,"citizen.html")

def get_CitizenLogin(request):
    if request.method == "POST":
        emailid = request.POST.get("emailid")
        password = request.POST.get("password")
        qs = RegistrationDataModel.objects.filter(emailid=emailid,password=password)
        if qs:
            request.session["emailid"]=emailid
            return render(request,"login_index.html", {"data":qs})
        else:
            return render(request,"citizen.html",{"message":"Invalid User"})

def citizen_logout(request):
    try:
      del request.session["emailid"]
      request.session.modified = True
      return redirect('index')
    except KeyError:
        return render(request,"citizen.html")


def ShowCitizenService(request):
    return render(request,"citizenservice.html")

def ShowShareIdea(request):
    try:
      if request.session["emailid"]:
        return render(request, "shareIdea.html")
    except KeyError:
        return render(request, "citizen.html")


def Popup_Login_ShareIdea(request):
    if request.method == "POST":
        emailid = request.POST.get("emailid")
        password = request.POST.get("password")
        si = RegistrationDataModel.objects.filter(emailid=emailid, password=password)
        if si:
            request.session["emailid"] = emailid
            return render(request, "shareIdea.html")
        else:
            return render(request,"index.html",{"messageSI": "Invalid User"})

def get_ShareIdea(request):
    s_name = request.POST.get("s_name")
    s_address = request.POST.get("s_address")
    s_email = request.POST.get("s_email")
    s_mobile = request.POST.get("s_mobile")
    s_message = request.POST.get("s_message")

    # To save a share_idea record into table
    ShareIdeaModel(s_name=s_name, s_address=s_address, s_email=s_email,
                   s_mobile=s_mobile, s_message=s_message).save()
    return render(request, "shareIdea.html",{"s_message": "Your idea has been successfully send and you will get response in 24 hour."})


def ShowIssueCompaint(request):
    try:
        if request.session["emailid"]:
          return render(request,"issueComplaint.html")
    except KeyError:
        return render(request,"citizen.html")


def Popup_Login_IssueComplaint(request):
    if request.method == "POST":
        emailid = request.POST.get("emailid")
        password = request.POST.get("password")
        si = RegistrationDataModel.objects.filter(emailid=emailid, password=password)
        if si:
            request.session["emailid"] = emailid
            return render(request, "issueComplaint.html")
        else:
            return render(request, "index.html", {"messageSI": "Invalid User"})

def get_IssueCompaint(request):
    com_name = request.POST.get("com_name")
    com_address = request.POST.get("com_address")
    com_email = request.POST.get("com_email")
    com_mobile = request.POST.get("com_mobile")
    #com_problem = request.POST.get("com__problem")
    com_image = request.FILES["com_image"]
    com_message = request.POST.get("com_message")

    # To save a share_idea record into table
    CompIssueModel(com_name=com_name, com_address=com_address, com_email=com_email,
                   com_mobile=com_mobile,com_image=com_image, com_message=com_message).save()
    return render(request,"issueComplaint.html",{"s_message": "Your Complaint has been successfully send and you will get response in 24 hour."})


def ShowGiveSuggestion(request):
    try:
        if request.session["emailid"]:
           qs = PublishProjectModel.objects.all()
           return render(request,"givesuggestion.html",{"projectdata": qs})
    except KeyError:
        return render(request,"citizen.html")

def Popup_Login_GiveSuggestion(request):
    if request.method == "POST":
        emailid = request.POST.get("emailid")
        password = request.POST.get("password")
        si = RegistrationDataModel.objects.filter(emailid=emailid, password=password)
        if si:
            request.session["emailid"] = emailid
            qs = PublishProjectModel.objects.all()
            return render(request, "givesuggestion.html",{"projectdata": qs})
        else:
            return render(request, "aboutus.html", {"messageSI": "Invalid User"})

def Show_GiveSuggestion_InputFields(request):
    try:
        if request.session["emailid"]:
          return render(request,"GiveSuggestion_InputField.html")
    except KeyError:
         return render(request,"citizen.html")

def get_GiveSuggestion(request):
    g_name = request.POST.get("g_name")
    g_projectname = request.POST.get("g_projectname")
    g_address = request.POST.get("g_address")
    g_email = request.POST.get("g_email")
    g_mobile = request.POST.get("g_mobile")
    g_message = request.POST.get("g_message")

    # To save a share_idea record into table
    GiveSuggestionModel(g_name=g_name, g_projectname=g_projectname, g_address=g_address, g_email=g_email,
                   g_mobile=g_mobile, g_message=g_message).save()
    return render(request, "GiveSuggestion_InputField.html",{"s_message": "Your Suggestion has been successfully send and you will get response in 24 hour."})


def PublishProject(request):
    return render(request,"administrator.html")

def get_PublishProject(request):
    project_name = request.POST.get("project_name")
    project_image = request.FILES["project_image"]

    # To save a publish_project record into table
    p = PublishProjectModel(project_name=project_name, project_image=project_image)
    p.save()
    return PublishProject(request)

def DeleteProject(request):
    project_name = request.GET.get("del_no")
    PublishProjectModel.objects.filter(project_name=project_name).delete()
    return ad_deleteproject(request)

def ShowAboutUs(request):
    return render(request,"aboutus.html")

def ShowContactUs(request):
    return render(request,"contactus.html")

#def myaccount(request):
    #    if request.method == "POST":
    #   emailid = request.POST.get("emailid")
    #   password = request.POST.get("password")
    ##   qs = RegistrationDataModel.objects.all()
    #  qs = ProfileImageModel.objects.all()
#   return render(request,"login_index.html",{"data":qs})

def ad_deleteproject(request):
    qs = PublishProjectModel.objects.all()
    return render(request,"deleteproject.html",{"projectdata": qs})