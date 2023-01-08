# from django.shortcuts import render
from django.shortcuts import render
from dashboard.models import Otherproducts, Surfaceproducts,Throughproducts
from .forms import surface_form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
# Create your views here.
from django.http import JsonResponse
from .models import Surfaceproducts
from django.db.models import Q
import os
cwd=os.getcwd()
print(cwd)
def home_page(request):

    return render(request,'pages/home.html')

#  id = models.AutoField(db_column='ID', primary_key=True, blank=True, null=True)  # Field name made lowercase.
#     mrfppartno = models.TextField(db_column='MrfpPartNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     datasheet = models.TextField(blank=True, null=True)  # This field type is a guess.
#     ref = models.TextField(db_column='REF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     mounting = models.TextField(db_column='Mounting', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     value = models.TextField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     ht = models.TextField(db_column='HT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     dia = models.TextField(db_column='Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     spring_dia = models.TextField(db_column='Spring_Dia', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     pitch = models.TextField(db_column='Pitch', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     three_d_drawing = models.TextField(db_column='Three_d_drawing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     size_of_component = models.TextField(db_column='Size_of_component', blank=True, null=True)  #
# print(Otherproducts.objects.filter(mrfppartno='ERM8-025-01-L-D-EM2-DS-TR'))
def surfaceProduct(request):
    Datao_obj=Surfaceproducts.objects.all()
    page = request.GET.get('page', 1)
    # paginator = Paginator(Datao_obj, 25) 
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # print(page_obj)
    # print(len(paginator.__dict__["object_list"]))
    data=[]
    paginator = Paginator(Datao_obj, 25)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
 
    return render(request,'pages/surface.html',{'page_obj':page_obj})



def edit_surface_data(request):
    form = surface_form()
    id=request.GET.get("id")
    find_data=Surfaceproducts.objects.get(id=id)
   
    return render(request, "pages/edit_surface.html", {"find_data": find_data})


def update_surface(request):
    id=request.GET.get("id")

    ht=request.GET.get("ht")
    dia=request.GET.get("dia")
    spring_dia=request.GET.get("spring_dia")
 
    material=request.GET.get("material")
    pitch=request.GET.get("pitch")
    value=request.GET.get("value")
    data={'added':False}
    
    find_data=Surfaceproducts.objects.filter(id=id)
   
    if find_data.exists():
        add_industry_objet = find_data.update(
            ht=ht,
            dia=dia,
            spring_dia=spring_dia,
            material=material,
            pitch=pitch,
            value=value
        )
        data["added"] = True
    return JsonResponse(data)

def get_surface_unique_data(request):
    id=request.GET.get("id")
    get_data=Surfaceproducts.objects.filter(id=id).first()

    data={'ht':get_data.ht,'manufacture':get_data.mrfppartno,'mounting':get_data.mounting,'dia':get_data.dia,'spring_dia':get_data.spring_dia,'material':get_data.material,'pitch':get_data.pitch,'value':get_data.value,"Datasheet":get_data.datasheet,"Ref":get_data.ref}
    return JsonResponse(data)







# -----------------------------------------------------------------------------------

def throughproducts(request):
    Datao_obj=Throughproducts.objects.all()
    page = request.GET.get('page', 1)
    # paginator = Paginator(Datao_obj, 25) 
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # print(page_obj)
    # print(len(paginator.__dict__["object_list"]))
    data=[]
    paginator = Paginator(Datao_obj, 25)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    print(len(data))
    return render(request,'pages/throughproducts.html',{'page_obj':page_obj})

def edit_through_data(request):
    form = surface_form()
    
    id=request.GET.get("id")
    find_data=Throughproducts.objects.get(id=id)
    return render(request, "pages/edit_through.html", {"find_data": find_data})



def add_data(request):
    form = surface_form()
    
    id=request.GET.get("id")
    # find_data=Throughproducts.objects.get(id=id)
    return render(request, "pages/add_data.html")

def update_through(request):
    id=request.GET.get("id")

    ht=request.GET.get("ht")
    dia=request.GET.get("dia")
    spring_dia=request.GET.get("spring_dia")
 
    material=request.GET.get("material")
    pitch=request.GET.get("pitch")
    value=request.GET.get("value")
    data={'added':False}
    
    find_data=Throughproducts.objects.filter(id=id)
   
    if find_data.exists():
        add_industry_objet = find_data.update(
            ht=ht,
            dia=dia,
            spring_dia=spring_dia,
            material=material,
            pitch=pitch,
            value=value
        )
        data["added"] = True
    return JsonResponse(data)

def get_through_unique_data(request):
    id=request.GET.get("id")
    get_data=Throughproducts.objects.filter(id=id).first()

    data={'ht':get_data.ht,'manufacture':get_data.mrfppartno,'mounting':get_data.mounting,'dia':get_data.dia,'spring_dia':get_data.spring_dia,'material':get_data.material,'pitch':get_data.pitch,'value':get_data.value,"Datasheet":get_data.datasheet,"Ref":get_data.ref}
    return JsonResponse(data)




# -----------------------------------------------------------------------------------

def otherproducts(request):
    Datao_obj=Otherproducts.objects.all()
    page = request.GET.get('page', 1)
    # paginator = Paginator(Datao_obj, 25) 
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # print(page_obj)
    # print(len(paginator.__dict__["object_list"]))
    data=[]
    paginator = Paginator(Datao_obj, 25)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    print(len(data))
    return render(request,'pages/other.html',{'page_obj':page_obj})

def edit_other_data(request):
    id=request.GET.get("id")
    find_data=Otherproducts.objects.get(id=id)
   

    return render(request, "pages/edit_other.html", {"find_data": find_data})


def update_other(request):
    id=request.GET.get("id")

    ht=request.GET.get("ht")
    dia=request.GET.get("dia")
    spring_dia=request.GET.get("spring_dia")
 
    material=request.GET.get("material")
    pitch=request.GET.get("pitch")
    value=request.GET.get("value")
    data={'added':False}
    
    find_data=Otherproducts.objects.filter(id=id)
   
    if find_data.exists():
        add_industry_objet = find_data.update(
            ht=ht,
            dia=dia,
            spring_dia=spring_dia,
            material=material,
            pitch=pitch,
            value=value
        )
        data["added"] = True
    return JsonResponse(data)

 
def add_menu_data(request):

    if request.method == "POST":
        is_private = False
        print(request.POST)
        Manufacturer = request.POST.get('Manufacturer')
        Mounting = request.POST.get('Mounting')
        productvalue = request.POST.get('productvalue')
        ht = request.POST.get('HT')  
          
        Dia = request.POST.get('Dia')
        Spring = request.POST.get('Spring')
        url=None
        try:
            file=request.FILES['file']
            
            if file:
                
                
                if "pdf" not  in file.name:
                    
                    data["flag"] =False
                    data["msg"]="Only Pdf formate is allowed"
                    return JsonResponse(data)
                with open('media/'+file.name, 'wb+') as destination:  
                    for chunk in file.chunks():  
                        destination.write(chunk)
                url= '/media/'+file.name
        except:
            pass 
        
        Pitch = request.POST.get('Pitch')
        Material = request.POST.get('Material')
        data={'added':False}
        data["flag"] =True
       
            

        
        
        if Mounting =="0":
            find_data=Surfaceproducts.objects.filter(mrfppartno=Manufacturer)
            if find_data.exists():
                data["flag"] =False
                data["msg"]="Data Already exists"
                return JsonResponse(data)
            if  not find_data.exists():


                add_industry_objet = Surfaceproducts(
                    ht=ht,
                    dia=Dia,
                    spring_dia=Spring,
                    material=Material,
                    pitch=Pitch,
                    value=productvalue,
                    mrfppartno=Manufacturer,
                    mounting="Surface Mount",
                    datasheet=url

                )
                add_industry_objet.save()
                data["flag"] =True
                data["msg"]="Data Added Successfully"
                return JsonResponse(data)
        
        if Mounting =="1":
            find_data1=Throughproducts.objects.filter(mrfppartno=Manufacturer)
            if find_data1.exists():
                data["flag"] =False
                data["msg"]="Data Already exists"
                return JsonResponse(data)
            if not find_data1.exists():
                add_industry_objet = Throughproducts(
                    ht=ht,
                    dia=Dia,
                    spring_dia=Spring,
                    material=Material,
                    pitch=Pitch,
                    value=productvalue,
                    mrfppartno=Manufacturer,
                    mounting="Through Hole",
                    datasheet=url

                )
                add_industry_objet.save()
                data["flag"] =True
                data["msg"]="Data Added Successfully"
                return JsonResponse(data)
        
        if Mounting =="2":
            find_data2=Otherproducts.objects.filter(mrfppartno=Manufacturer)
            if find_data2.exists():
                data["flag"] =False
                data["msg"]="Data Already exists"
                return JsonResponse(data)

            if not find_data2.exists():

                add_industry_objet = Otherproducts(
                    ht=ht,
                    dia=Dia,
                    spring_dia=Spring,
                    material=Material,
                    pitch=Pitch,
                    value=productvalue,
                    mrfppartno=Manufacturer,
                    mounting="Chassis Mount",
                    datasheet=url

                )
                add_industry_objet.save()
                data["flag"] =True
                data["msg"]="Data Added Successfully"
                return JsonResponse(data)
        
        data["added"] = True
    return JsonResponse(data)






def get_other_unique_data(request):
    id=request.GET.get("id")
    get_data=Otherproducts.objects.filter(id=id).first()

    data={'ht':get_data.ht,'manufacture':get_data.mrfppartno,'mounting':get_data.mounting,'dia':get_data.dia,'spring_dia':get_data.spring_dia,'material':get_data.material,'pitch':get_data.pitch,'value':get_data.value,"Datasheet":get_data.datasheet,"Ref":get_data.ref}
    return JsonResponse(data)

# def find_record(request):
#     return render(request,'pages/search.html')

def find_record(request):
    print(request.GET)
    Manufacturer = request.GET.get('Manufacturer')
    Mounting = request.GET.get('Mounting')
    productvalue = request.GET.get('productvalue')
    ht = request.GET.get('HT')      
    Dia = request.GET.get('Dia')
    Spring = request.GET.get('Spring')
    Spring = request.GET.get('Spring')
    Pitch = request.GET.get('Pitch')
    Material = request.GET.get('Material')
    print(Manufacturer,Mounting,productvalue,ht,Dia,Spring)

    query = Q()
    if Manufacturer:
        query &= Q(mrfppartno__icontains =Manufacturer)
    # if Mounting:
    #     query &= Q(mrfppartno__icontains =Mounting)
    if productvalue:
        query &= Q(value__icontains =productvalue)
    if ht:
        query &= Q(ht__icontains =ht)
    if Dia:
        query &= Q(dia__icontains =Dia)
    if Spring:
        query &= Q(spring_dia__icontains =Spring)
    if Material:
        query &= Q(material__icontains =Material)
    if Pitch:
        query &= Q(pitch__icontains =Pitch)
    product_type=2
    # objects=Otherproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    if Mounting=="0" or Mounting==None:
        product_type="0"
        objects=Surfaceproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    elif Mounting=="1":
        product_type="1"
        objects=Throughproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
    elif Mounting=="2":
        product_type="2"
        objects=Otherproducts.objects.filter(query).values('id','mrfppartno','datasheet','ref','mounting' ,'value','ht','dia','spring_dia' ,'material','pitch','three_d_drawing' ,'size_of_component')
   
    paginator = Paginator(objects, 25)
    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    url="/find_record/?"
    if Manufacturer:
        url+="Manufacturer="+Manufacturer
    if Mounting:
        url+="&Mounting="+Mounting
    if productvalue:
        url+="&Manufacturer="+productvalue
    if ht:
        url+="&Manufacturer="+ht
    if Dia:
        url+="&Manufacturer="+Dia
    if Spring:
        url+="&Manufacturer="+Spring
    if Material:
        url+="&Manufacturer="+Material
    if Pitch:
        url+="&Manufacturer="+Pitch
    
    return  render(request,'pages/search.html',{'page_obj':page_obj,'url':url,'type':product_type})