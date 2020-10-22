__author__ = 'David Guzman with help from Gordon'
import requests
import turtle
import time


def read_names_and_spacecraft():
    res = requests.get('http://api.open-notify.org/astros.json')
    res_json = res.json()
    people = res_json['people']
    print(
        f"Total number of people on space station: {res_json['number']}")
    for person in people:
        name = person['name']
        craft = person['craft']
        print(f"Full name: {name}, Spacecraft: {craft}")


def read_iss_coord():
    res = requests.get('http://api.open-notify.org/iss-now.json')
    res_json = res.json()
    pos = res_json['iss_position']
    for coords in pos:
        print(f"Longitude: {pos['longitude']}, Latitude: {pos['latitude']}")


def iss_over_indy():
    params = {'lat': float(39.76838), 'lon': float(-86.15804)}
    res = requests.get('http://api.open-notify.org/iss-pass.json',
                       params=params).json()
    res = res['response'][0]['risetime']
    convert_time = time.ctime(res)
    return convert_time


def read_current_coords():
    res_json = requests.get(
        'http://api.open-notify.org/iss-now.json').json()
    return res_json


def canvas(location):
    screen = turtle.Screen()
    screen.bgpic('map.gif')
    turtle.setup(width=720, height=360, startx=None, starty=None)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    latitude = float(location['iss_position']['latitude'])
    longitude = float(location['iss_position']['longitude'])
    iss.penup()
    iss.goto(longitude, latitude)


def indy_mapping():
    latitude = float(39.768402)
    longitude = float(-86.158066)
    indy_iss = turtle.Turtle()
    indy_iss.penup()
    indy_iss.goto(longitude, latitude)
    indy_iss.color('red')
    indy_iss.dot(8)
    indy_iss.write(iss_over_indy())
    indy_iss.hideturtle()
    turtle.done()


def main():
    read_names_and_spacecraft()
    read_current_coords()
    canvas(read_current_coords())
    indy_mapping()
    iss_over_indy()


if __name__ == '__main__':
    main()
