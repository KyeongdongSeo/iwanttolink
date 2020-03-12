from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Site


def site_list(request):
    sites = Site.objects.filter(status=200).order_by('-created_date')
    return render(request, 'web/site_list.html', {'sites': sites})

def site_detail(request, pk):
    site = get_object_or_404(Site, pk=pk)
    return render(request, 'web/site_detail.html', {'site': site})
