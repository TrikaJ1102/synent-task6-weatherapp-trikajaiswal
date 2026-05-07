import customtkinter as ctk
import requests

# ---------------- APP SETTINGS ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

API_KEY = "f8820024eccd1c29b907dc4a46edf7ad"

# ---------------- MAIN WINDOW ----------------
root = ctk.CTk()

root.geometry("900x700")
root.title("Modern Weather App")
root.resizable(False, False)

# Default background
root.configure(fg_color="#1f1f1f")

# ---------------- WEATHER FUNCTION ----------------
def get_weather():

    city = city_entry.get().strip()

    if city == "":
        result_label.configure(text="Please enter a city name")
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        # Error Handling
        if data["cod"] != 200:
            result_label.configure(
                text=f"Error: {data['message']}"
            )
            return

        # ---------------- WEATHER DATA ----------------
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]

        # ---------------- WEATHER EMOJIS ----------------
        if weather.lower() == "clear":
            emoji = "☀️"
            root.configure(fg_color="#1f3b4d")

        elif weather.lower() == "clouds":
            emoji = "☁️"
            root.configure(fg_color="#2b2b2b")

        elif weather.lower() == "rain":
            emoji = "🌧️"
            root.configure(fg_color="#1b263b")

        elif weather.lower() == "snow":
            emoji = "❄️"
            root.configure(fg_color="#394867")

        elif weather.lower() == "thunderstorm":
            emoji = "⛈️"
            root.configure(fg_color="#2c3333")

        else:
            emoji = "🌤️"
            root.configure(fg_color="#242424")

        # ---------------- UPDATE UI ----------------
        city_label.configure(text=city.title())

        temp_label.configure(
            text=f"{temp:.1f}°C"
        )

        weather_label.configure(text=weather)

        desc_label.configure(
            text=description.title()
        )

        humidity_value.configure(
            text=f"{humidity}%"
        )

        wind_value.configure(
            text=f"{wind} m/s"
        )

        feels_value.configure(
            text=f"{feels_like:.1f}°C"
        )

        emoji_label.configure(text=emoji)

        result_label.configure(text="")

    except Exception as e:
        result_label.configure(
            text=f"Error: {str(e)}"
        )


# ---------------- TITLE ----------------
title = ctk.CTkLabel(
    root,
    text="Weather App",
    font=("Poppins", 42, "bold")
)
title.pack(pady=30)

# ---------------- SEARCH FRAME ----------------
search_frame = ctk.CTkFrame(
    root,
    corner_radius=25
)
search_frame.pack(pady=20)

# Search Entry
city_entry = ctk.CTkEntry(
    search_frame,
    width=420,
    height=55,
    placeholder_text="Enter city name",
    font=("Poppins", 18),
    corner_radius=18
)
city_entry.grid(
    row=0,
    column=0,
    padx=15,
    pady=15
)

# Search Button
search_btn = ctk.CTkButton(
    search_frame,
    text="Search",
    width=140,
    height=55,
    font=("Poppins", 18, "bold"),
    corner_radius=18,
    hover_color="#1f6fbf",
    cursor="hand2",
    command=get_weather
)
search_btn.grid(
    row=0,
    column=1,
    padx=15
)

# Enter key support
root.bind("<Return>", lambda event: get_weather())

# ---------------- RESULT LABEL ----------------
result_label = ctk.CTkLabel(
    root,
    text="",
    text_color="red",
    font=("Poppins", 15)
)
result_label.pack()

# ---------------- WEATHER CARD ----------------
weather_frame = ctk.CTkFrame(
    root,
    width=650,
    height=450,
    corner_radius=30
)
weather_frame.pack(pady=30)

# ---------------- EMOJI ----------------
emoji_label = ctk.CTkLabel(
    weather_frame,
    text="☁️",
    font=("Arial", 80)
)
emoji_label.pack(pady=(25, 5))

# ---------------- CITY ----------------
city_label = ctk.CTkLabel(
    weather_frame,
    text="",
    font=("Poppins", 34, "bold")
)
city_label.pack()

# ---------------- TEMPERATURE ----------------
temp_label = ctk.CTkLabel(
    weather_frame,
    text="",
    font=("Poppins", 78, "bold"),
    text_color="#4da6ff"
)
temp_label.pack()

# ---------------- WEATHER TYPE ----------------
weather_label = ctk.CTkLabel(
    weather_frame,
    text="",
    font=("Poppins", 30)
)
weather_label.pack()

# Description
desc_label = ctk.CTkLabel(
    weather_frame,
    text="",
    font=("Poppins", 18),
    text_color="gray"
)
desc_label.pack(pady=(0, 25))

# ---------------- INFO CARD ----------------
info_frame = ctk.CTkFrame(
    weather_frame,
    corner_radius=25
)
info_frame.pack(
    pady=20,
    padx=20,
    fill="x"
)

# ---------------- HUMIDITY ----------------
humidity_text = ctk.CTkLabel(
    info_frame,
    text="Humidity",
    font=("Poppins", 18, "bold")
)
humidity_text.grid(
    row=0,
    column=0,
    padx=45,
    pady=(20, 5)
)

humidity_value = ctk.CTkLabel(
    info_frame,
    text="",
    font=("Poppins", 24)
)
humidity_value.grid(
    row=1,
    column=0,
    padx=45,
    pady=(0, 20)
)

# ---------------- WIND ----------------
wind_text = ctk.CTkLabel(
    info_frame,
    text="Wind Speed",
    font=("Poppins", 18, "bold")
)
wind_text.grid(
    row=0,
    column=1,
    padx=45,
    pady=(20, 5)
)

wind_value = ctk.CTkLabel(
    info_frame,
    text="",
    font=("Poppins", 24)
)
wind_value.grid(
    row=1,
    column=1,
    padx=45,
    pady=(0, 20)
)

# ---------------- FEELS LIKE ----------------
feels_text = ctk.CTkLabel(
    info_frame,
    text="Feels Like",
    font=("Poppins", 18, "bold")
)
feels_text.grid(
    row=0,
    column=2,
    padx=45,
    pady=(20, 5)
)

feels_value = ctk.CTkLabel(
    info_frame,
    text="",
    font=("Poppins", 24)
)
feels_value.grid(
    row=1,
    column=2,
    padx=45,
    pady=(0, 20)
)

# ---------------- FOOTER ----------------
footer = ctk.CTkLabel(
    root,
    text="Developed by Trika Jaiswal",
    font=("Poppins", 12),
    text_color="gray"
)

footer.pack(side="bottom", pady=12)

# ---------------- RUN APP ----------------
root.mainloop()