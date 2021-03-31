import requests
import datetime
import geocoder
from numpy import arange
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from lib.misc import location_placeholder
from tkinter import messagebox

API_KEY  = "866da5bb6a904a5a8289e2cf6debfe3c"
LOCATION = ""
FORECAST = {}


def get_location(city):
    global LOCATION

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    data = requests.get(url).json()

    if data["cod"] != "404":
        LOCATION = f"{data['name'].capitalize()}, {data['sys']['country']}"
        lon, lat = data["coord"]["lon"], data["coord"]["lat"]
        return lon, lat
    else:
        messagebox.showinfo("City not found", f"Couldn't find the forecast for '{city.capitalize()}'")


def get_forecast(lon, lat):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lon={lon}&lat={lat}&units=metric&exclude=minutely,alerts&appid={API_KEY}"
    data = requests.get(url).json()

    for day in data["daily"]:
        td = datetime.datetime.utcfromtimestamp(int(day["dt"])).strftime('%d.%m\n%A')
        average = (day["temp"]["day"] + day["temp"]["night"]) / 2
        FORECAST[td] = (day["temp"]["max"], day["temp"]["min"], average)


def visualize():
    max_temp = [FORECAST[temp][0] for temp in FORECAST]
    min_temp = [FORECAST[temp][1] for temp in FORECAST]
    avg_temp = [FORECAST[temp][2] for temp in FORECAST]
    dates = [date for date in FORECAST.keys()]

    # Setup
    plt.style.use("seaborn")
    plt.rcParams["toolbar"] = "None"
    plot, ax = plt.subplots(1)

    # Plots
    plt.rcParams['lines.linewidth'] = 3
    plt.rcParams['lines.linestyle'] = "-"

    ax.plot(dates, max_temp, color="orange", label="Max")
    ax.plot(min_temp, color="lightblue", label="Min")

    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams['lines.linestyle'] = ":"

    ax.plot(avg_temp, color="red", label="Avg")
    ax.legend()

    if max(max_temp) < 20:
        ax.set_ylim(0, max(max_temp))

    # Styling
    plt.xticks(rotation=45)
    plt.yticks(arange(min(min_temp) - 1, max(max_temp) + 2, 1.0))

    plt.gcf().subplots_adjust(bottom=0.2, top=0.85)
    plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.0f}"))
    plt.gcf().canvas.set_window_title(f"7 Day Forecast | {LOCATION}")

    plt.title(f"7 Day Forecast\n{LOCATION}")
    plt.xlabel("Date [day.month]")
    plt.ylabel("Temperature $^\circ$C")

    plt.show()


def pytemp(city):
    if city == "" or city == location_placeholder:
        city = f"{geocoder.ip('me').city}"

    location_info = get_location(city)
    # If get_location returns a tuple, the location was found, otherwise an error have occurred
    if isinstance(location_info, tuple):
        lat, lon = location_info
        get_forecast(lat, lon)
        visualize()
