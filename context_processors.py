from index import models

def siteInfo(request):
    info = models.SiteInfo.objects.get_or_create()[0]

    return{
        'siteName': info.siteName,
    }