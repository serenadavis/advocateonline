from .models import Ad

def getAds(section):
	try:
		ads = Ad.objects.filter(location=section, enabled=True).order_by('date_added')
		return ads
	except (Ad.DoesNotExist, IndexError):
		return None
