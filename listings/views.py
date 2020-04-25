from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date') #this will show discending order of houses by dates
    paginator = Paginator(listings, 3)         #
    page = request.GET.get('page')             #
    paged_listings = paginator.get_page(page)  #
    context = { 
        'listings' : paged_listings            # see django pagination documentation to recall the idea!
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    #here get_object_or_404 returns the page if the listing_id is valid else returns 404 message 
    #pk means primary key of listing
    context = {
        'listing' : listing
    } 
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')
