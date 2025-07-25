import requests
from tkinter import *

# Fetch and display weather info
def get_weather():
    city = city_entry.get()
    api_key = "d2cceeb63b444945a2e100953252507"
    base_url = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            result = f"""
            📍 City: {city.title()}
            🌡️ Temp: {data['current']['temp_c']} °C
            💧 Humidity: {data['current']['humidity']}%
            🌬️ Pressure: {data['current']['pressure_mb']} hPa
            🌥️ Condition: {data['current']['condition']['text']}
            """

            result_label.config(text=result, fg="white", bg="#000000")
        else:
            result_label.config(text=f"Error: {response.status_code}", fg="red", bg="#000000")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red", bg="#000000")

# ---------- GUI Setup ----------
window = Tk()
window.title("🌦 Weather Detection App")
window.geometry("500x350")
window.configure(bg="#000000")  # Black background

# Title Label
title_label = Label(window, text="🌤️ Weather Info", font=("Helvetica", 20, "bold"),
                    fg="#00BFFF", bg="#000000")  # DeepSkyBlue + black
title_label.pack(pady=15)

# Entry Field
city_entry = Entry(window, width=30, font=("Arial", 14), bd=3, relief="solid", justify="center",
                   bg="white", fg="black")
city_entry.pack(pady=10)
city_entry.insert(0, "")

# Button
search_button = Button(window, text="Get Weather", command=get_weather,
                       font=("Arial", 12, "bold"), bg="#00BFFF", fg="white", padx=10, pady=5,
                       activebackground="#005f99", activeforeground="white")
search_button.pack(pady=10)

# Result Label
result_label = Label(window, text="", font=("Courier", 12), justify="left",
                     bg="#000000", fg="white", wraplength=480)
result_label.pack(pady=15)

window.mainloop()
