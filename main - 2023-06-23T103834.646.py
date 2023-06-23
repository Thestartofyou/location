import geocoder

def track_location():
    g = geocoder.ip('me')
    if g.ok:
        location = g.latlng
        print("Latitude:", location[0])
        print("Longitude:", location[1])
    else:
        print("Failed to track location.")

if __name__ == "__main__":
    track_location()

