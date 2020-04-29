from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import send_mail


# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST.get('realtor_email')

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        
    messages.success(request, 'your request has been submitted, a realtor will get back to you soon')

    #now send email 
    send_mail(
        'property Listing Inquiry',
        'there has been an inquiry for' + listing + '. Sign in to view more', 'intense.me0926@gmail.com', ['barsha.upadhaya1996@gmail.com', realtor_email],
        fail_silently=False
    )
    return redirect ('/listings/'+listing_id)
