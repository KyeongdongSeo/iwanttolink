from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from .models import Site
from .forms import SiteForm


@login_required
def site_list(request):
    sites = Site.objects.filter(Q(status=200)|Q(status=503)).order_by('-created_date')
    return render(request, 'web/site_list.html', {'sites': sites})

@login_required
def site_detail(request, pk):
    site = get_object_or_404(Site, pk=pk)
    return render(request, 'web/site_detail.html', {'site': site})

@login_required
def site_new(request):
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.created_date = timezone.now()
            site.save()
            return redirect('site_detail', pk=site.pk)
    else:
        form = SiteForm()
    return render(request, 'web/site_edit.html', {'form': form})

@login_required
def site_edit(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method == "POST":
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            site = form.save(commit=False)
            site.created_date = timezone.now()
            site.save()
            return redirect('site_detail', pk=site.pk)
    else:
        form = SiteForm(instance=site)
    return render(request, 'web/site_edit.html', {'form': form})

@login_required
def site_dead_list(request):
    sites = Site.objects.filter(~Q(status=200)|~Q(status=503)).order_by('-created_date')
    return render(request, 'web/site_dead_list.html', {'sites': sites})

@login_required
def site_remove(request, pk):
    site = get_object_or_404(Site, pk=pk)
    site.delete()
    return redirect('site_list')
