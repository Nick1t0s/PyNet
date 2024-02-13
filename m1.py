from pygeocoder import Geocoder
if __name__ == "__main__":
    addres = 'Orel'
    print(Geocoder.geocode(addres)[0].cordinates)