from django.shortcuts import render
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q 
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from core.models import *

# Create your views here.

def index(request):
    items = Item.objects.filter(available=True).order_by('-date')[0:20]

    return render(request, "index.html",{
        'items':items,
    })

def logout(request):
    auth.logout(request)
    return redirect('home')


def detail(request, slug, id):
    item = get_object_or_404(Item, slug=slug, id=id)
   
    related_items = Item.objects.filter(type=item.type).exclude(pk=id).order_by('-date')[0:5]
    characteristics = Item_Characteristics.objects.filter(item=item)
    images = ImageModel.objects.filter(item=item)

    owner_phone_number = item.owner.phonenumber.phone_number

    return render(request, "detail.html", {
        'item':item,
        'related_items':related_items,
        'characteristics':characteristics,
        'images':images,
        'owner_phone_number': owner_phone_number,
    })

def detail_job(request, slug, id):
    job = get_object_or_404(Job, slug=slug, id=id)
   
    related_jobs = Job.objects.filter(category=job.category).exclude(pk=id).order_by('-date')[0:5]
    characteristics = Job_Characteristics.objects.filter(job=job)
    {}

    owner_phone_number = job.owner.phonenumber.phone_number

    return render(request, "detail-job.html", {
        'job':job,
        'related_jobs':related_jobs,
        'characteristics':characteristics,
        'owner_phone_number': owner_phone_number,
    })

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('annonces')
            else:
                messages.info(request, "Mot de passe incorrect.")
                return redirect('login')
        except User.DoesNotExist:
            messages.info(request, "Email incorrect.")
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def register_view(request):
    if request.method == 'POST':
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password1']
       password2 = request.POST['password2']
       phone_number = request.POST['phone']
       
       if password == password2:
        if User.objects.filter(email=email).exists():
            messages.info(request, "L'Email choisi est déjà utilisé.")
            return redirect('register')
           
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Le nom d'utilisateur existe déjà.")
            return redirect('register')
           
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            phone_number_obj, created = PhoneNumber.objects.get_or_create(phone_number=phone_number, defaults={'user': user})
            
            if created:
                pass

            else:
                messages.info(request, "Le numéro de téléphone existe déjà.")
            
            # Log in the user
            
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('annonces')
        
       else:
        messages.info(request, "Les mots de passe ne correspondent pas.")
        return redirect('register')


    return render(request, 'register.html')

def products_clothes(request):

    subcategory = Subcategory.objects.get(name='Vêtements')
    items = Item.objects.filter(available=True, subcategory=subcategory).order_by('-date')
    return render(request,"list/products_clothes.html",{
        'items':items,
    })

def products_plans(request):

    type = Type.objects.get(name='Plan')
    items = Item.objects.filter(available=True, type=type).order_by('-date')
    return render(request,"list/products_plans.html",{
        'items':items,
    })

def jobs(request):
    
    jobs = Job.objects.filter(available=True).order_by('-date')
    return render(request, "list/jobs.html",{
        'jobs':jobs,
    })


@login_required
def profile(request):

    user = request.user
    phone_number = user.phonenumber.phone_number

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        new_phone = request.POST.get('phone')
        new_password = request.POST.get('newpass')
        current_password = request.POST.get('password')
        
        if user.check_password(current_password):
            if username:
                user.username = username
            if email:
                user.email = email
            if new_phone:
                phone_number = new_phone  # Update phone_number based on your data
            if new_password:
                if not user.check_password(current_password):
                    messages.error(request, 'Current password is incorrect.')
                else:
                    user.set_password(new_password)
                    update_session_auth_hash(request, user)  # Keep the user logged in
                    messages.success(request, 'Your password has been changed successfully.')

            try:
                user.full_clean()  # Validate the user model fields
                user.save()
                messages.success(request, 'Your profile has been updated successfully.')
            except ValidationError as e:
                messages.error(request, e)

            return redirect('profile')  # Redirect back to the profile page
        
        else:
            messages.error(request, 'Current password is incorrect.')
    return render(request, "account/profile.html",{
        'phone_number':phone_number,
    })

@login_required
def annonces(request):
    return render(request, "account/annonces.html")



@login_required
def category(request):
    return render(request, "creation/category.html")

@login_required
def location(request):

    phone_number = request.user.phonenumber.phone_number

    if request.method == 'POST':
        category = Category.objects.get(name = 'Immobilier')
        subCategory = Subcategory.objects.get(name = 'Location')
       
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        type_object = request.POST.get('type')

        superficie = Characteristics.objects.get(name = 'Superficie')

        superficie_value = request.POST.get('superficie')

        type = Type.objects.get(name = type_object)
        
        # Retrieve other form field values in a similar way


        item = Item.objects.create(
            category=category,
            subcategory=subCategory,
            
            title=title,
            description=description,
            price=price,
            owner = request.user,
            type=type,
            # Assign other field values here
        )
        
        primary_image_uploaded = False
        for image_file in request.FILES.getlist('product_image'):
            if not primary_image_uploaded:
                # If the primary image has not been set yet, assign it to the item
                item.primary_image = image_file
                primary_image_uploaded = True
            else:
                # For the rest of the images, create ImageModel objects
                ImageModel.objects.create(item=item, image=image_file)

        # Save the item after processing images
        item.save() 


        characteristic1 = Item_Characteristics.objects.create(
            item = item,
            characteristics = superficie,
            value = superficie_value,
        )

        # Additional processing or manipulation of the form data can be done here

        return redirect('detail',slug=item.slug, id=item.id)  # Redirect to item detail page

    return render(request, "creation/immobilier/location.html", {
        'phone_number':phone_number,
    })







@login_required
def vente(request):

    phone_number = request.user.phonenumber.phone_number

    if request.method == 'POST':
        category = Category.objects.get(name = 'Immobilier')
        subCategory = Subcategory.objects.get(name = 'Vente')
       
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        type_object = request.POST.get('type')

        superficie = Characteristics.objects.get(name = 'Superficie')

        superficie_value = request.POST.get('superficie')

        type = Type.objects.get(name = type_object)
        
        # Retrieve other form field values in a similar way


        item = Item.objects.create(
            category=category,
            subcategory=subCategory,
            
            title=title,
            description=description,
            price=price,
            owner = request.user,
            type=type,
            # Assign other field values here
        )
        
        primary_image_uploaded = False
        for image_file in request.FILES.getlist('product_image'):
            if not primary_image_uploaded:
                # If the primary image has not been set yet, assign it to the item
                item.primary_image = image_file
                primary_image_uploaded = True
            else:
                # For the rest of the images, create ImageModel objects
                ImageModel.objects.create(item=item, image=image_file)

        # Save the item after processing images
        item.save() 


        characteristic1 = Item_Characteristics.objects.create(
            item = item,
            characteristics = superficie,
            value = superficie_value,
        )

        # Additional processing or manipulation of the form data can be done here

        return redirect('detail',slug=item.slug, id=item.id)  # Redirect to item detail page

    return render(request, "creation/immobilier/vente.html", {
        'phone_number':phone_number,
    })








@login_required
def plan(request):

    phone_number = request.user.phonenumber.phone_number

    if request.method == 'POST':
        category = Category.objects.get(name = 'Immobilier')
        subCategory = Subcategory.objects.get(name = 'Plan')
       
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        type_object = request.POST.get('type')

        superficie = Characteristics.objects.get(name = 'Superficie')

        superficie_value = request.POST.get('superficie')

        type = Type.objects.get(name = type_object)
        
        # Retrieve other form field values in a similar way


        item = Item.objects.create(
            category=category,
            subcategory=subCategory,
            
            title=title,
            description=description,
            price=price,
            owner = request.user,
            type=type,
            # Assign other field values here
        )
        
        primary_image_uploaded = False
        for image_file in request.FILES.getlist('product_image'):
            if not primary_image_uploaded:
                # If the primary image has not been set yet, assign it to the item
                item.primary_image = image_file
                primary_image_uploaded = True
            else:
                # For the rest of the images, create ImageModel objects
                ImageModel.objects.create(item=item, image=image_file)

        # Save the item after processing images
        item.save() 


        characteristic1 = Item_Characteristics.objects.create(
            item = item,
            characteristics = superficie,
            value = superficie_value,
        )

        # Additional processing or manipulation of the form data can be done here

        return redirect('detail',slug=item.slug, id=item.id)  # Redirect to item detail page

    return render(request, "creation/immobilier/plan.html", {
        'phone_number':phone_number,
    })







@login_required
def voiture(request):

    phone_number = request.user.phonenumber.phone_number

    if request.method == 'POST':
        category = Category.objects.get(name = 'Véhicules')
        subCategory = Subcategory.objects.get(name = 'Voiture')
       
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        type_object = request.POST.get('type')
        type = Type.objects.get(name = 'Modèle')

        marque = Characteristics.objects.get(name='Marque')
        marque_value = request.POST.get('marque')

        serie = Characteristics.objects.get(name='Série')
        serie_value = request.POST.get('serie')
        
        # Retrieve other form field values in a similar way


        item = Item.objects.create(
            category=category,
            subcategory=subCategory,
            
            title=title,
            description=description,
            price=price,
            owner = request.user,
            type=type,
            # Assign other field values here
        )
        
        primary_image_uploaded = False
        for image_file in request.FILES.getlist('product_image'):
            if not primary_image_uploaded:
                # If the primary image has not been set yet, assign it to the item
                item.primary_image = image_file
                primary_image_uploaded = True
            else:
                # For the rest of the images, create ImageModel objects
                ImageModel.objects.create(item=item, image=image_file)

        # Save the item after processing images
        item.save() 


        characteristic1 = Item_Characteristics.objects.create(
            item = item,
            characteristics = marque,
            value = marque_value,
        )

        characteristic2 = Item_Characteristics.objects.create(
            item = item,
            characteristics = serie,
            value = serie_value,
        )

        # Additional processing or manipulation of the form data can be done here

        return redirect('detail',slug=item.slug, id=item.id)  # Redirect to item detail page

    return render(request, "creation/vehicule/voiture.html", {
        'phone_number':phone_number,
    })







@login_required
def chantier(request):

    phone_number = request.user.phonenumber.phone_number

    if request.method == 'POST':
        category = Category.objects.get(name = 'Services')
        subCategory = Subcategory.objects.get(name = 'Chantier')
       
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        type_object = request.POST.get('type')
        type = Type.objects.get(name =type_object)

        nego = Characteristics.objects.get(name='Négociable')
        nego_value = request.POST.get('nego')

        travail = Characteristics.objects.get(name='Travail')
        travail_value = request.POST.get('travail')
        
        experience = Characteristics.objects.get(name='Expérience')
        experience_value = request.POST.get('experience')

        contact1 = Characteristics.objects.get(name='Contact 1')
        contact1_value = request.POST.get('contact1')

        contact2 = Characteristics.objects.get(name='Contact 2')
        contact2_value = request.POST.get('contact2')
        # Retrieve other form field values in a similar way


        item = Item.objects.create(
            category=category,
            subcategory=subCategory,
            
            title=title,
            description=description,
            price=price,
            owner = request.user,
            type=type,
            # Assign other field values here
        )
        
        primary_image_uploaded = False
        for image_file in request.FILES.getlist('product_image'):
            if not primary_image_uploaded:
                # If the primary image has not been set yet, assign it to the item
                item.primary_image = image_file
                primary_image_uploaded = True
            else:
                # For the rest of the images, create ImageModel objects
                ImageModel.objects.create(item=item, image=image_file)

        # Save the item after processing images
        item.save() 


        characteristic1 = Item_Characteristics.objects.create(
            item = item,
            characteristics = nego,
            value = nego_value,
        )

        characteristic2 = Item_Characteristics.objects.create(
            item = item,
            characteristics = travail,
            value = travail_value,
        )

        characteristic3 = Item_Characteristics.objects.create(
            item = item,
            characteristics = experience,
            value = experience_value,
        )

        characteristic4 = Item_Characteristics.objects.create(
            item = item,
            characteristics = contact1,
            value = contact1_value,
        )

        characteristic5 = Item_Characteristics.objects.create(
            item = item,
            characteristics = contact2,
            value = contact2_value,
        )



        # Additional processing or manipulation of the form data can be done here

        return redirect('detail',slug=item.slug, id=item.id)  # Redirect to item detail page

    return render(request, "creation/services/chantier.html", {
        'phone_number':phone_number,
    })




@login_required
def marketing_vente(request):
    phone_number = request.user.phonenumber.phone_number

    if request.method == 'POST':
        category = Category_job.objects.get(name='Marketing & Vente')
        title = request.POST.get('title')
        description = request.POST.get('description')
        type = request.POST.get('type')
        salary = request.POST.get('salary')
        contract_type = request.POST.get('contract_type')
        heures = request.POST.get('heures')
        period = request.POST.get('period')
        website = request.POST.get('website')
        job_logo = request.FILES.get('job_logo')
        

        french = request.POST.get('l1')
        if french:
            Language1 = Languages.objects.get(name=french)
        else:
            Language1 = None


        english = request.POST.get('l2')
        if english:
            Language2 = Languages.objects.get(name=english)
        else:
            Language2 = None


        dutch = request.POST.get('l3')
        if dutch:
            Language3 = Languages.objects.get(name=dutch)
        else:
            Language3 = None



        aucun_niveau = request.POST.get('nv0')
        if aucun_niveau:
            niveau0 = Niveau.objects.get(name=aucun_niveau)
        else:
            niveau0 = None
        
        niveau1 = request.POST.get('nv1')
        if niveau1:
            niveau1 = Niveau.objects.get(name=niveau1)
        else:
            niveau1 = None
        
        niveau2 = request.POST.get('nv2')
        if niveau2:
            niveau2 = Niveau.objects.get(name=niveau2)
        else:
            niveau2 = None
        
        niveau3 = request.POST.get('nv3')
        if niveau3:
            niveau3 = Niveau.objects.get(name=niveau3)
        else:
            niveau3 = None

        niveau4 = request.POST.get('nv4')
        if niveau4:
            niveau4 = Niveau.objects.get(name=niveau4)
        else:
            niveau4 = None

        niveau5 = request.POST.get('nv5')
        if niveau5:
            niveau5 = Niveau.objects.get(name=niveau5)
        else:
            niveau5 = None


        job = Job.objects.create(
            category=category,
            title=title,
            description=description,
            type=type,
            salary=salary,
            contract_type=contract_type,
            heures=heures,
            period=period,
            website=website,
            job_logo=job_logo,
            owner=request.user,
        )

        if Language1:
            job.langues.add(Language1)

        if Language2:
            job.langues.add(Language2)

        if Language3:
            job.langues.add(Language3)
        

        if niveau0:
            job.niveau.add(niveau0)
        
        if niveau1:
            job.niveau.add(niveau1)
        
        if niveau2:
            job.niveau.add(niveau2)
        
        if niveau3:
            job.niveau.add(niveau3)
        
        if niveau4:
            job.niveau.add(niveau4)
        
        if niveau4:
            job.niveau.add(niveau4)

        job.save()

        return redirect('detail-job',slug=job.slug, id=job.id)

        #return redirect('detail-job',slug=job.slug, id=job.id)



    return render(request, "creation/emplois/marketing-vente.html" , {
        'phone_number':phone_number,
    })





@login_required
def clothes(request):
    phone_number = request.user.phonenumber.phone_number

    if request.method == 'POST':
        category = Category.objects.get(name = 'Divers')
        subCategory = Subcategory.objects.get(name = 'Vêtements')
       
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        type_object = request.POST.get('type')
        type = Type.objects.get(name =type_object)


        genre = Characteristics.objects.get(name='Genre')
        genre_value = request.POST.get('genre')
        
        age = Characteristics.objects.get(name='Âge')
        age_value = request.POST.get('age')

        # Retrieve other form field values in a similar way


        item = Item.objects.create(
            category=category,
            subcategory=subCategory,
            
            title=title,
            description=description,
            price=price,
            owner = request.user,
            type=type,
            # Assign other field values here
        )
        
        primary_image_uploaded = False
        for image_file in request.FILES.getlist('product_image'):
            if not primary_image_uploaded:
                # If the primary image has not been set yet, assign it to the item
                item.primary_image = image_file
                primary_image_uploaded = True
            else:
                # For the rest of the images, create ImageModel objects
                ImageModel.objects.create(item=item, image=image_file)

        # Save the item after processing images
        item.save() 


        characteristic1 = Item_Characteristics.objects.create(
            item = item,
            characteristics = age,
            value = age_value,
        )

        characteristic2 = Item_Characteristics.objects.create(
            item = item,
            characteristics = genre,
            value = genre_value,
        )


        # Additional processing or manipulation of the form data can be done here

        return redirect('detail',slug=item.slug, id=item.id)  # Redirect to item detail page

    return render(request, "creation/divers/clothes.html", {
        'phone_number':phone_number,
    })