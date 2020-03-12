from django.shortcuts import render


def site_list(request):
    return render(request, 'web/site_list.html', {})
