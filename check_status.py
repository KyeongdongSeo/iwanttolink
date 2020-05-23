import os
import sys
import requests
import django


sys.path.append(os.path.dirname(os.path.realpath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings') 
django.setup()


from web.models import Site


def get_request(url, timeout=3, headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}):
    try:
        response = requests.get(url=url, headers=headers, timeout=timeout)
    except Exception as e:
        response = 'error'
    return response


if __name__ == '__main__':
    sites = Site.objects.all()

    for site in sites:
        update_flag = False
        response = get_request(site.url)
        if response != 'error':
            if response.history:
                site.url = response.url
                update_flag = True

            if site.status != response.status_code:
                site.status = response.status_code
                update_flag = True
        else:
            site.status = 4
            update_flag = True

        if update_flag:
            site.save()
