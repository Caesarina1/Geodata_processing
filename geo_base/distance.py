from geopy import distance as gd
# from .models import User, Target
# from views import position_page

# For the specified locations, load their latitude and longitude data.
# Abuja = (9.072264, 7.491302)
# Dakar = (14.716677, -17.467686)
# Finally, print the distance between the two sites in kilometers.
# print("The distance between Abuja and Dakar is: ", gd.distance(Abuja, Dakar).km)


def count_dist(a, b):
    dist = gd.distance(a, b).km
    return dist

# def count_dist(latitude, longitude):
#     a = get(CombatUnit coordinates from position page
#     b = Target.objects.get(latitude=latitude, longitude=longitude)
#     dist = gd.distance(a, b).km
#     return dist
