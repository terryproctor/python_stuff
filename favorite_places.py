favorite_places = {
    'Bilbo': ['New Zealand', 'Modor'],
    'Terry': ['Japan', 'Thailand', 'Munich', 'Scotland'],
    'Elizabeth': ['China', 'Thailand']
}

for name, places in favorite_places.items():
    print(f"{name}: ")
    for place in places:
        print(f"\t-{place}")
    