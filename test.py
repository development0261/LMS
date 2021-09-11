# 192.168.0.89
import geocoder


def get_Ip():
    g = geocoder.ip('me')
    print(g.latlng)
    print(g.city)
    print(g.state)
    print(g.country)


get_Ip()
