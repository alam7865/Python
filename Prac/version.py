import requests
import datetime

city_name = "New Delhi"
key = "70fc880bb6dd527322cd4fc1b42196a5"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # City;
    # print(data["name"])

    # ////////// Temperature

    # kelvin = data["main"]["temp"]
    # celcius = kelvin - 273.15
    # print(celcius)

    # /////////// Weather Description ////////////////
    # weatherDesc = data["weather"][0]["description"]
    # print(weatherDesc)

    # //////////// Humidity /////////////////////////

    # humidity = data["main"]["temp"]
    # print(humidity)
    # print(f"Humidity: {data['main']['humidity']}%")

    # humidity = data["main"]["humidity"]
    # print(humidity)

    # //////////////// Wind Speed ////////////////////

    # speed = f"{data["wind"]["speed"]} M/S"
    # print(speed)

    # ////////////////// SunRise /////////////////////
    # sunRise = data["sys"]["sunrise"]
    # print(sunRise)

    # sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    # print(sunrise)
    # print("Sunrise:", sunrise.strftime("%H:%M:%S"))

    # //////  main ///////
    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

    # print("SunRise: ", sunrise.strftime("%H:%M:%S"))
    print("SunSet: ", sunset.strftime("%H:%M:%S"))
    hour = int(sunset.strftime("%H"))
    if hour > 12:
        h1 = hour - 12
    print(h1)

    # /////////////////// Clouds //////////////////////

    # clouds = data["clouds"]["all"]
    # print(clouds)
