from urllib.parse import urlparse


def get_previous_list_type(request):
    referer = request.META.get('HTTP_REFERER', '')
    path = urlparse(referer).path

    if 'explore/provinces' in path:
        return 'Provinces'
    elif 'explore/dioceses' in path:
        return 'Dioceses'
    elif 'explore/archdeaconries' in path:
        return 'Archdeaconries'
    elif 'explore/deaneries' in path:
        return 'Deaneries'
    elif 'explore/parishes' in path:
        return 'Parishes'
    else:
        return 'Explore the Valor'
