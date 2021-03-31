from lib.misc import tkinter, path, location_placeholder
from lib import pytemp
from lib import entry
from lib import button


def gui():
    WIDTH, HEIGHT = 512, 512
    window = tkinter.Tk()
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.resizable(False, False)
    window.title("7 Day Forecast")

    bg = tkinter.PhotoImage(file=f"{path}/images/background.png")
    canvas = tkinter.Canvas(window, width=400, height=400)
    canvas.pack(fill="both", expand=True)

    # Display image
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # Add Text
    canvas.create_text(WIDTH/2, 80, fill="white", text="7 Day Forecast", font=("Chango", 25))

    location = entry.InputField(window, 20, 120, WIDTH-40, 30, location_placeholder)
    location.show()

    get_forecast_btn = button.Button(window, WIDTH/2-75, HEIGHT/2-40, 150, 40, "Get Forecast", lambda: pytemp.pytemp(location.get()))
    get_forecast_btn.show()

    window.mainloop()
