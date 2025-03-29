from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk,ImageDraw
import requests
import random
import webbrowser

#Initialize main window
root = Tk()
root.title("Echo-Sky")
root.geometry("900x500+300+200")
root.resizable(False,False)

#Weather
def getWeather():
    try:
        city=textfield.get()
        WEATHER_API_KEY = 'b827addb22e04e4b8af71748242910'
        BASE_URL = 'http://api.weatherapi.com/v1/current.json'
        api_url = f'{BASE_URL}?key={WEATHER_API_KEY}&q={city}'
        
        json_data =requests.get(api_url).json()
        condition = json_data['current']['condition']['text']
        temp = json_data['current']['temp_c'] 
        humidity = json_data['current']['humidity']  

        t.config(text=f"{temp} °C")
        c.config(text=(condition))
        h.config(text=f"{humidity}%")
        
        return temp, humidity, condition
    
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!")
        return None,None,None


weather_genre_artist = {
    'Sunny': [
        'Arijit Singh', 'Kishore Kumar', 'Mohit Chauhan', 'Lata Mangeshkar',
        'Atif Aslam', 'Bruno Mars', 'One Direction', 'Kanye West',
        'Post Malone', 'Zayn Malik', 'BTS', 'Backstreet Boys',
        'NSYNC', 'The Wanted', '5 Seconds of Summer', 'Sukhwinder Singh',
        'Jubin Nautiyal', 'Divine', 'Kartik Aaryan', 'The Local Train',
        'Shubham Soni', 'Naseeruddin Shah', 'Shankar Mahadevan', 'Amaal Mallik'
    ],
    'Rainy': [
        'Mohit Chauhan', 'Ankit Tiwari', 'Arijit Singh', 'Kishore Kumar',
        'Badshah', 'Sam Smith', 'John Mayer', 'Harry Styles',
        'Kumar Sanu', 'Sonu Nigam', 'Diljit Dosanjh', 'Jass Manak',
        'Karan Aujla', 'Gurdaas Mann', 'Folk Bhangra', 'Vishal Mishra',
        'Bhuvan Bam', 'Raja Kumari', 'Nucleya', 'Naseeruddin Shah',
        'Prateek Kuhad', 'Shubh', 'Karan Singh Arora'
    ],
    'Cloudy': [
        'Kishore Kumar', 'Lata Mangeshkar', 'Tulsi Kumar', 'Shreya Ghoshal',
        'Mohit Chauhan', 'Sam Smith', 'Arijit Singh', 'Ankit Tiwari',
        'Taylor Swift', 'Calvin Harris', 'John Legend', 'Amaan Malik',
        'Banda Banda', 'Karan Aujla', 'Harrdy Sandhu', 'Indeep Bakshi',
        'Khan Bhaini', 'Mellow D', 'Karan Aujla', 'Shubh', 'Dilljit Dosanjh'
    ],
    'Overcast': [
        'Norah Jones', 'Kumar Sanu', 'Shreya Ghoshal', 'Coldplay',
        'Arijit Singh', 'Mohit Chauhan', 'Lata Mangeshkar', 'Tulsi Kumar',
        'Billie Eilish', 'Jubin Nautiyal', 'Gajendra Verma', 'Vishal Dadlani',
        'Rashmeet Kaur', 'Shubh', 'Khan Bhaini', 'Shubham Soni'
    ],
    'Thunderstorm': [
        'Badshah', 'Divine', 'Kanye West', 'Eminem', 'Lil Wayne',
        'Drake', 'Post Malone', 'Khalid', 'Travis Scott', 'Arijit Singh',
        'Maroon 5', 'Linkin Park', 'Metallica', 'Imagine Dragons',
        'Florence + The Machine', 'The Weeknd', 'Billie Eilish', 'Sam Smith',
        'Sik-K', 'Kendrick Lamar', 'Logic', 'G-Eazy', 'J. Cole'
    ],
    'Fog': [
        'Shreya Ghoshal', 'Kumar Sanu', 'Taylor Swift', 'Armaan Malik',
        'Kishore Kumar', 'Billie Eilish', 'John Legend', 'Norah Jones',
        'Louis Armstrong', 'Duke Ellington', 'Jubin Nautiyal',
        'Guru Randhawa', 'Harrdy Sandhu', 'Shubh', 'Khan Bhaini',
        'Bhuvan Bam', 'Anuv Jain'
    ],
    'Clear': [
        'Arijit Singh', 'Kishore Kumar', 'Mohit Chauhan', 'Shawn Mendes',
        'The Chainsmokers', 'Bruno Mars', 'OneRepublic', 'Calvin Harris',
        'Khalid', 'Zayn Malik', 'BTS', 'Backstreet Boys', '5 Seconds of Summer',
        'NSYNC', 'The Vamps', 'Karan Singh Arora', 'The Local Train',
        'Gurdaas Mann', 'Shubh', 'Prateek Kuhad', 'Khan Bhaini'
    ],
    'Partly Cloudy': [
        'Coldplay', 'One Direction', 'Ed Sheeran', 'Kishore Kumar',
        'Mohit Chauhan', 'Shawn Mendes', 'Imagine Dragons', 'Linkin Park',
        'Maroon 5', 'The Weeknd', 'The Chainsmokers', 'Florence + The Machine',
        'Banda Banda', 'Karan Aujla', 'Khan Bhaini', 'Shubh', 'Gurdaas Mann'
    ],
    'Snowy': [
        'Neeti Mohan', 'Lata Mangeshkar', 'Arijit Singh', 'Shreya Ghoshal',
        'Sam Smith', 'Coldplay', 'Taylor Swift', 'John Mayer',
        'Louis Armstrong', 'Frank Sinatra', 'Dean Martin', 'Ed Sheeran',
        'Justin Bieber', 'Jubin Nautiyal', 'Amaal Mallik', 'Shankar Mahadevan',
        'Indeep Bakshi', 'Bhuvan Bam'
    ],
    'Windy': [
        'Calvin Harris', 'Justin Bieber', 'Zayn Malik', 'Armaan Malik',
        'Mohit Chauhan', 'Kishore Kumar', 'Shawn Mendes', 'The Chainsmokers',
        'Banda Banda', 'Diljit Dosanjh', 'Jass Manak', 'Gurdaas Mann',
        'Prateek Kuhad', 'Shubh', 'Khan Bhaini'
    ],
    'Mist': [
        'Mohit Chauhan', 'Ankit Tiwari', 'Arijit Singh',
        'Kishore Kumar', 'Shawn Mendes', 'The Chainsmokers',
        'Florence + The Machine', 'Jubin Nautiyal', 'Amaal Mallik',
        'Indeep Bakshi', 'The Local Train', 'Shubh'
    ]
}

#Spotify-Connection
SPOTIFY_CLIENT_ID = 'cf02b432872847a9902355ab4322ad0b'
SPOTIFY_CLIENT_SECRETS = 'c69b673a7dd242fc9fa07caee842ad1b'

def normalize_weather_condition(weather):
    weather = weather.lower()
    if 'cloudy' in weather:
        return 'Cloudy'
    elif 'sunny' in weather:
        return 'Sunny'
    elif 'rain' in weather or 'drizzle' in weather:
        return 'Rainy'
    elif 'thunderstorm' in weather:
        return 'Thunderstorm'
    elif 'fog' in weather:
        return 'Fog'
    elif 'clear' in weather:
        return 'Clear'
    elif 'partly cloudy' in weather:
        return 'Partly Cloudy'
    elif 'snow' in weather:
        return 'Snowy'
    elif 'windy' in weather:
        return 'Windy'
    elif 'overcast' in weather:
        return 'Overcast'
    elif 'mist' in weather:
        return 'Mist'
    else:
        return None

def get_music_recommendations(weather):
    normalized_weather = normalize_weather_condition(weather)
    if normalized_weather in weather_genre_artist:
        artists = weather_genre_artist[normalized_weather]
        sample_size = min(15, len(artists))
        recommendations = random.sample(artists, sample_size)
        return recommendations
    else:
        print("Weather condition not recognized.")
        return []

def get_spotify_token():
    client_id = "cf02b432872847a9902355ab4322ad0b"  # Replace with your actual client ID
    client_secret = "c69b673a7dd242fc9fa07caee842ad1b"  # Replace with your actual client secret
    auth_url = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })

    if auth_response.status_code == 200:
        auth_response_data = auth_response.json()
        return auth_response_data['access_token']
    else:
        print(f"Error obtaining Spotify token: {auth_response.status_code} - {auth_response.text}")
        return None

# Initialize Spotify token
spotify_token = get_spotify_token()

# Spotify API to get song links
def get_song_links(artists):
    global spotify_token  # Allow updates to spotify_token if it refreshes
    all_songs = []

    if not spotify_token:
        print("No valid Spotify token provided.")
        return all_songs

    for artist in artists:
        search_url = f'https://api.spotify.com/v1/search?q={artist}&type=track&limit=5'
        headers = {'Authorization': f'Bearer {spotify_token}'}
        response = requests.get(search_url, headers=headers)

        # Refresh token if expired
        if response.status_code == 401:  # 401 indicates the token is expired
            spotify_token = get_spotify_token()  # Refresh the token
            headers['Authorization'] = f'Bearer {spotify_token}'
            response = requests.get(search_url, headers=headers)

        if response.status_code == 200:
            tracks = response.json().get('tracks', {}).get('items', [])
            for track in tracks:
                song_name = track.get('name')
                song_link = track.get('external_urls', {}).get('spotify')
                if song_name and song_link:
                    all_songs.append((song_name, song_link))
        else:
            print(f"Error fetching songs for {artist}: {response.status_code} - {response.text}")

    return all_songs

def create_playlist():
    temperature, humidity, condition = getWeather()
    recommendations = get_music_recommendations(condition)
    song_links = get_song_links(recommendations)

    if not song_links:
        messagebox.showerror("Error", "No song links found.")
        return

    # Clear existing entries in the Listbox instead of destroying widgets
    playlist_box.delete(0, END)

    # Populate the Listbox with new song recommendations
    for song, link in song_links:
        playlist_box.insert(END, song)
        
    # Make items clickable to open links in the browser
    def on_select(event):
        selected_index = playlist_box.curselection()
        if selected_index:
            webbrowser.open(song_links[selected_index[0]][1])

    # Bind Listbox selection to open the corresponding song link
    playlist_box.bind("<<ListboxSelect>>", on_select)


#Setting Background Image
original_image = Image.open("background.jpg") 
bg_image = original_image.resize((900, 500), Image.LANCZOS) 
bg_image_tk = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_image_tk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Setting Shape over Background
def create_rounded_rectangle(width, height, radius, color):
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle(
        [(0, 0), (width, height)],
        radius=radius,
        fill=color  # Fill color with transparency
    )
    return image

rounded_rectangle_image = create_rounded_rectangle( 800,400,15,(232,232,232,150))
rounded_rectangle_tk = ImageTk.PhotoImage(rounded_rectangle_image)

canvas = tk.Canvas(root, width=900, height=500, bg='white', highlightthickness=0)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image_tk)
canvas.create_image(50, 50, anchor=tk.NW, image=rounded_rectangle_tk)

#Search-Box
search_box = canvas.create_rectangle(70, 70, 460, 110, outline='', fill='#404040')

textfield = tk.Entry(root, justify="left", width=20, font=("Poppins", 15, "bold"),bg="#404040", fg="white", border=0)
textfield.place(x=90, y=77)
textfield.focus()

search_icon = Image.open("search_icon.png").resize((34,32), Image.LANCZOS) 
search_icon_tk =ImageTk.PhotoImage(search_icon)
myimage_icon=tk.Button(image=search_icon_tk,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=419,y=73)

#WeatherBox
logo=Image.open("logo.png").resize((80,68),Image.LANCZOS)
logo_image=ImageTk.PhotoImage(logo)
logo=Label(image=logo_image,bg="#404040")
logo.place(x=112,y=153)

weather_box = canvas.create_rectangle(110, 150, 400, 340, outline='', fill='#404040')

temp=Label(root,text="Temperature - ",font=("Times New Roman",15),fg="white",bg="#404040")
temp.place(x=140,y=230)
t=Label(text="",font=("Times New Roman",15),bg="#404040",fg="white")
t.place(x=270,y=230)

humid=Label(root,text="Humidity - ",font=("Times New Roman",15),fg="white",bg="#404040")
humid.place(x=140,y=260)
h=Label(text="",font=("Times New Roman",15),bg="#404040",fg="white")
h.place(x=270,y=260)

condition=Label(root,text="Condition - ",font=("Times New Roman",15),fg="white",bg="#404040")
condition.place(x=140,y=290)
c=Label(text="",font=("Times New Roman",15),bg="#404040",fg="white")
c.place(x=270,y=290)

#PLaylist button
gen_playlist=tk.Button(text="Generate Playlist 🎶", font =("Times New Roman",15),borderwidth=0,cursor="hand2",bg="#404040",fg="white",command=create_playlist)
gen_playlist.place(x=260,y=370)

#Playlist Box
playlist_frame = Frame(root, bg="#404040")
playlist_frame.place(x=510, y=80, width=300, height=340)

scrollbar = Scrollbar(playlist_frame, orient=VERTICAL)

playlist_box = Listbox(
    playlist_frame, 
    font=("Helvetica", 12), 
    bg="#404040", 
    fg="white", 
    selectbackground="#606060", 
    selectforeground="white", 
    yscrollcommand=scrollbar.set,
    justify=CENTER
)

playlist_box.place(x=24, y=30, width=226, height=282)  
scrollbar.place(x=270, y=10, height=320)
scrollbar.config(command=playlist_box.yview)

song=Image.open("song.png").resize((44,44),Image.LANCZOS)
song_image=ImageTk.PhotoImage(song)
song=Label(image=song_image,bg="#404040" ,fg="white")
song.place(x=518,y=88)


root.mainloop()