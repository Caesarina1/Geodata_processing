from .models import Target


# if __name__ == "__main__":

locations = []
targets = Target.objects.all()

for target in targets:
    locations.append({
                    "id": target.id,
                    "title": target.type,
                    # "src": {geo_base/static/images/tank.jpg},
                    "lat": target.latitude,
                    "long": target.latitude,
                    })

print(f"{locations}")
