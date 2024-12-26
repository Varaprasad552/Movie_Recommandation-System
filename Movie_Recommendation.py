import tkinter as tk
from tkinter import Toplevel, Scrollbar, Text, Entry, Button
from PIL import Image, ImageTk
import webbrowser
import openai

# Add your OpenAI API key here
#openai.api_key =   # <-- Insert your OpenAI API key here

# Sample movie data structure
movies = {
     "Humor": [
        ("You People", 2023, "English", "A comedy about an interracial couple and their families.",
         {"Netflix":"https://www.netflix.com/watch/81194505?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139296702%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139296702%7C2%2Cunknown%2C%2C%2CtitlesResults%2C81194505%2CVideo%3A81194505%2CminiDpPlayButton","Prime(Amzon)":"https://www.primevideo.com/offers/nonprimehomepage/ref=dv_web_force_root","Youtube (Trailer)":"https://www.youtube.com/watch?v=pCMHc-IFAB0"}),
        ("Murder Mystery 2", 2023, "English", "A couple's vacation turns into a hunt for a missing billionaire.",
         {"Netflix": "https://www.netflix.com/watch/81212842?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139628038%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139628038%7C2%2Cunknown%2C%2C%2CtitlesResults%2C%2CVideo%3A81212842%2CdetailsPagePlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube (Trailer)":"https://www.youtube.com/watch?v=5YEVQDr2f3Q"}),
        ("The Out-Laws", 2023, "English", "A bank manager’s wedding is interrupted by his in-laws’ criminal activities.", 
         {"Netflix":"https://www.netflix.com/watch/81186234?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139758288%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139758288%7C2%2Cunknown%2C%2C%2CtitlesResults%2C81186234%2CVideo%3A81186234%2CminiDpPlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube (Trailer)":"https://www.youtube.com/watch?v=MvPaDziB-ac"}),
        ("The other  Guys", 2023, "English", "Private eye and a hired enforcer team up to find a missing girl.", 
         {"Netflix":"https://www.netflix.com/watch/70127228?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139814906%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139814906%7C2%2Cunknown%2C%2C%2CtitlesResults%2C70127228%2CVideo%3A70127228%2CminiDpPlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube Trailer":"https://www.youtube.com/watch?v=kGO9IF67lqw"}),
        ("Dolemite Is My Name", 2023, "English", "A comedian creates a kung-fu film to become famous.", 
         {"Netflix":"https://www.netflix.com/watch/80182014?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139948469%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-139948469%7C2%2Cunknown%2C%2C%2CtitlesResults%2C%2CVideo%3A80182014%2CminiDpPlayButton","Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube Trailer":"https://www.youtube.com/watch?v=Ws1YIKsuTjQ"}),
        ("We Have a Ghost", 2023, "English", "A family discovers their house is haunted and becomes a social media sensation.",
         {"Netflix": "https://www.netflix.com/watch/80230619?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140020588%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140020588%7C2%2Cunknown%2C%2C%2CtitlesResults%2C80230619%2CVideo%3A80230619%2CminiDpPlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube Trailer":"https://www.youtube.com/watch?v=_Qq4U9LHA_0"}),
        ("Day Shift", 2022, "English", "A vampire hunter hides his real profession from his family.", 
         {"Netflix":"https://www.netflix.com/watch/81186049?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140088709%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140088709%7C2%2Cunknown%2C%2C%2CtitlesResults%2C%2CVideo%3A81186049%2CminiDpPlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube Trailer":"https://www.youtube.com/watch?v=hMU3JhSnwZI"}),
        ("The Lost City", 2022, "English", "A romance novelist is kidnapped during her book tour.",
         {"Netflix": "https://www.netflix.com/watch/81180203?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140134249%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140134249%7C2%2Cunknown%2C%2C%2CtitlesResults%2C%2CVideo%3A81180203%2CminiDpPlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube Trailer":"https://www.youtube.com/watch?v=nfKO9rYDmE8"}),
        ("The Kissing Booth 3", 2021, "English", "A teenager faces choices about her future after high school graduation.",
         {"Netflix": "https://www.netflix.com/watch/81026819?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140192743%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140192743%7C2%2Cunknown%2C%2C%2CtitlesResults%2C81026819%2CVideo%3A81026819%2CminiDpPlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube Trailer":"https://www.youtube.com/watch?v=7bfS6seiLhk"}),
        ("Eurovision Song Contest: The Story of Fire Saga", 2020, "English", "Two aspiring Icelandic musicians get a chance to compete in the Eurovision Song Contest.", 
         {"Netflix":"https://www.netflix.com/watch/80244088?trackId=255824129&tctx=0%2C0%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140275726%2C0b21f9af-467a-47e2-a2ed-cdc6fa7f2687-140275726%7C2%2Cunknown%2C%2C%2CtitlesResults%2C80244088%2CVideo%3A80244088%2CminiDpPlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2","Youtube Trailer":"https://www.youtube.com/watch?v=RaOLxoxYidU"})
    ],
    "Mystery": [
        ("The Killer", 2023, "English", "A hitman seeks revenge after being betrayed by his employer.", {"Netflix":"https://www.netflix.com/watch/80234448?trackId=255824129&tctx=0%2C0%2C5e63d8e1-602b-468b-bd67-b7fdded3ceb4-63360517%2C5e63d8e1-602b-468b-bd67-b7fdded3ceb4-63360517%7C2%2Cunknown%2C%2C%2CtitlesResults%2C%2CVideo%3A80234448%2CminiDpPlayButton", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2"}),
        ("The Night Agent", 2023, "English", "An FBI agent investigates a conspiracy involving a missing person and an assassination.", {"Netflix": "https://www.netflix.com/title/81090234", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"}),
        ("Rattenfänger", 2023, "German", "A detective hunts down a mysterious figure linked to a series of crimes.",{ "Netflix": "https://www.netflix.com/title/81080372", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"}),
        ("The Fall Guy", 2023, "English", "A stuntman becomes a private investigator in a search for a missing colleague.",{  "Netflix":"https://www.netflix.com/title/81081393", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"}),
        ("Dead Ringers", 2023, "English", "Twins with a shared profession face ethical dilemmas in their work.", {"Netflix": "https://www.netflix.com/title/81082305", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"}),
        ("Heart of Stone", 2023, "English", "An intelligence agent must stop a global crisis caused by a rogue organization.",{ "Netflix": "https://www.netflix.com/title/81085877", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"}),
        ("The Devil's Hour", 2022, "English", "A social worker investigates a series of mysterious deaths linked to a cult.", {"Netflix": "https://www.netflix.com/title/81085059", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"}),
        ("The Night Manager", 2023, "English", "A hotel manager becomes embroiled in an international arms deal.", {"Netflix": "https://www.netflix.com/title/81080091", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"}),
        ("Sherlock Holmes", 2022, "English", "A modern retelling of the classic detective stories.", {"Netflix": "https://www.netflix.com/title/81008466", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"}),
        ("The Widow", 2022, "English", "A woman searches for her missing husband in a war-torn country.",{ "Netflix": "https://www.netflix.com/title/81007182", "Aha": "https://www.aha.video/movie/you-people", "Amazon Prime": "https://www.primevideo.com/detail/0MNPQZKQZ2", "YouTube Trailer": "https://www.youtube.com/watch?v=81194505"})
    ],
    "Horror": [
        ("The Nun II", 2023, "English", "A sequel to the horror hit about a demonic nun.", "https://www.netflix.com/title/81085678"),
        ("Insidious: The Red Door", 2023, "English", "A family faces new nightmares as they return to their haunted house.", "https://www.netflix.com/title/81080152"),
        ("M3GAN", 2023, "English", "A lifelike doll becomes dangerously protective of its owner.", "https://www.netflix.com/title/81085687"),
        ("Texas Chainsaw Massacre", 2023, "English", "A new generation faces the horror of Leatherface.", "https://www.netflix.com/title/81084215"),
        ("The Last House on the Left", 2023, "English", "A family seeks revenge after their daughter is kidnapped and assaulted.", "https://www.netflix.com/title/81082843"),
        ("Evil Dead Rise", 2023, "English", "A new chapter in the Evil Dead franchise set in an apartment building.", "https://www.netflix.com/title/81087123"),
        ("Hell House LLC Origins", 2023, "English", "A group of friends uncover the truth behind a notorious haunted house.", "https://www.netflix.com/title/81080023"),
        ("No One Will Save You", 2023, "English", "A woman fights against an alien invasion in her isolated home.", "https://www.netflix.com/title/81087489"),
        ("Spiral: From the Book of Saw", 2022, "English", "A detective hunts a killer who is emulating the Jigsaw killer's methods.", "https://www.netflix.com/title/81082971"),
        ("The Exorcist: Believer", 2023, "English", "A new exorcism horror film in the famous franchise.", "https://www.netflix.com/title/81085421")
    ],
    "Fiction": [
        ("Dune: Part Two", 2023, "English", "The epic continuation of Paul Atreides' journey.", "https://www.netflix.com/title/81086347"),
        ("Guardians of the Galaxy Vol. 3", 2023, "English", "The Guardians face new threats and explore deeper character arcs.", "https://www.netflix.com/title/81087385"),
        ("Avatar: The Way of Water", 2022, "English", "The sequel to the groundbreaking sci-fi film, exploring the oceans of Pandora.", "https://www.netflix.com/title/81080061"),
        ("The Marvels", 2023, "English", "A superhero team-up featuring Captain Marvel, Ms. Marvel, and Monica Rambeau.", "https://www.netflix.com/title/81087712"),
        ("The Matrix Resurrections", 2021, "English", "Neo returns to the Matrix for a new adventure.", "https://www.netflix.com/title/81076941"),
        ("Jurassic World: Dominion", 2022, "English", "The dinosaurs are back and causing chaos across the globe.", "https://www.netflix.com/title/81080350"),
        ("Tenet", 2020, "English", "A secret agent manipulates the flow of time to prevent World War III.", "https://www.netflix.com/title/81074566"),
        ("Inception", 2010, "English", "A thief who steals corporate secrets through dream-sharing technology.", "https://www.netflix.com/title/70131314"),
        ("Blade Runner 2049", 2017, "English", "A young blade runner discovers a long-buried secret.", "https://www.netflix.com/title/80199484"),
        ("The Fifth Element", 1997, "English", "A cab driver becomes an unlikely hero on a futuristic adventure.", "https://www.netflix.com/title/60000816")
    ],
    "Biography": [
        ("The Crown", 2023, "English", "The series chronicles the reign of Queen Elizabeth II.", "https://www.netflix.com/title/80025678"),
        ("The Trial of the Chicago 7", 2023, "English", "A dramatization of the trial of anti-Vietnam War protesters.", "https://www.netflix.com/title/81004448"),
        ("The Empress", 2022, "German", "A biographical drama about Empress Elisabeth of Austria.", "https://www.netflix.com/title/81022242"),
        ("Elvis", 2022, "English", "A biopic of the legendary musician Elvis Presley.", "https://www.netflix.com/title/81006274"),
        ("A Beautiful Mind", 2001, "English", "The life of John Nash, a Nobel Laureate in Economics.", "https://www.netflix.com/title/60020628"),
        ("The Social Network", 2010, "English", "The story of Facebook's founding.", "https://www.netflix.com/title/70132721"),
        ("Gandhi", 1982, "English", "The life of Mahatma Gandhi.", "https://www.netflix.com/title/60020994"),
        ("Schindler's List", 1993, "English", "Oskar Schindler saves Jews during the Holocaust.", "https://www.netflix.com/title/60000724"),
        ("The Imitation Game", 2014, "English", "The story of Alan Turing and his work in breaking the Enigma code.", "https://www.netflix.com/title/80025172"),
        ("Bohemian Rhapsody", 2018, "English", "The life of Freddie Mercury and the band Queen.", "https://www.netflix.com/title/81008487")
    ],
    "Action": [
        ("RRR", 2022, "Telugu", "A fictional tale of two legendary revolutionaries on their journey away from home before they began fighting for their country in the 1920s.",
         {"Netflix": "https://www.netflix.com/title/81294232", "Amazon Prime": "https://www.primevideo.com/detail/John-Wick-4", "YouTube Trailer": "https://www.youtube.com/watch?v=qEVUtrk8_B4"}),
        ("Pushpa: The Rise", 2021, "Telugu", "The story of Pushpa Raj, a red sandalwood smuggler, who rises to power in the underworld of South India.",
         {"Netflix": "https://www.netflix.com/title/81283247", "Aha": "https://www.aha.video/movie/mission-impossible", "YouTube Trailer": "https://www.youtube.com/watch?v=hb2r8-GS_NQ"}),
        ("Sarkaru Vaari Paata", 2022, "Telugu","A money lender's pursuit for justice against a powerful man leads to unexpected twists and action-packed sequences.",
         {"Netflix": "https://www.netflix.com/title/81283247", "Aha": "https://www.aha.video/movie/mission-impossible", "YouTube Trailer": "https://www.youtube.com/watch?v=hb2r8-GS_NQ"}),
        ("Vikram", 2022, "Telugu", "A high-octane action thriller about a black ops cop seeking revenge on a drug syndicate.",
         {"Disney+ Hotstar": "https://www.hotstar.com/in/movies/vikram/1260108290"}), 
         ("Saaho", 2019, "Telugu", "An undercover cop and a mysterious thief cross paths in a quest to expose a massive conspiracy.",
         {"Netflix": "https://www.netflix.com/title/81040362", "YouTube (Trailer)": "https://www.youtube.com/watch?v=mqEdhDk_VEI"}),

        ("Bheemla Nayak", 2022, "Telugu", "A clash of egos between a law-abiding cop and a hot-headed ex-military man leads to intense action.",
         {"Disney+ Hotstar": "https://www.hotstar.com/in/movies/bheemla-nayak/1260082313"}),

        ("K.G.F: Chapter 2", 2022, "Telugu", "Rocky continues his quest for power as he faces new enemies in the gold mines of Kolar.",
         {"Amazon Prime": "https://www.amazon.com/dp/B09T4RGTXD", "YouTube (Trailer)": "https://www.youtube.com/watch?v=1Lomz4toKTA"})
    ],
    "Romance": [
        ("Past Lives", 2023, "English/Korean", "Two childhood friends reunite and contemplate what might have been.",
         {"Netflix": "https://www.netflix.com/title/81381235", "Amazon Prime": "https://www.primevideo.com/detail/Past-Lives", "YouTube Trailer": "https://www.youtube.com/watch?v=6df0rha_Opw"}),
        ("Love Again", 2023, "English", "A grieving woman finds love with a man who reads her old texts.",
         {"Netflix": "https://www.netflix.com/title/81293752", "YouTube Trailer": "https://www.youtube.com/watch?v=HE-2lo_6v3Y"})
    ],
    "Documentary": [
        ("The Elephant Whisperers", 2023, "English", "A heartfelt documentary about a family who raises orphaned elephants.",
         {"Netflix": "https://www.netflix.com/title/81381273", "YouTube Trailer": "https://www.youtube.com/watch?v=ZJ_VwnFzJCg"}),
        ("The Tinder Swindler", 2022, "English", "A documentary about a conman who uses Tinder to manipulate and scam women.",
         {"Netflix": "https://www.netflix.com/title/81284288", "YouTube Trailer": "https://www.youtube.com/watch?v=_KlZSz2EKjk"})
    ]
    

}

# Initialize the main window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("800x600")

# Function to set a background image
def set_background(window, image_path):
    try:
        image = Image.open(image_path)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        resized_image = image.resize((screen_width, screen_height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(resized_image)

        background_label = tk.Label(window, image=photo_image)
        background_label.image = photo_image  # Keep a reference to avoid garbage collection
        background_label.place(relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error loading image: {e}")

# Set the background for the main window (Home Page)
set_background(root, "C:\\Users\\DANAT TARADING .CO\\Pictures\\chrome images.jpg")  # Home Page Background

# Create the home frame
home_frame = tk.Frame(root, bg="white")  # Set background to white for visibility
home_frame.place(relx=0.5, rely=0.5, anchor="center")

# Add a welcome label
welcome_label = tk.Label(home_frame, text="Welcome to the Movie Recommendation System", font=("Arial", 24, "bold"), bg="white")
welcome_label.pack(pady=(20, 10))  # Add padding to prevent overlap

# Add a description label
description_label = tk.Label(home_frame, text="Explore a wide selection of movies from various genres.", font=("Arial black", 16), bg="white")
description_label.pack(pady=(0, 20))  # Add padding to ensure no overlap with other widgets

# Function to go to the genre selection page
def open_genre_page():
    home_frame.place_forget()  # Hide the home page
    genre_frame.place(relx=0.5, rely=0.5, anchor="center")  # Show the genre frame
    set_background(root, "C:\\Users\\DANAT TARADING .CO\\Pictures\\movie_recommendation.jpg")  # Genre Page Background

# Start button
start_button = tk.Button(home_frame, text="Start Exploring", font=("Arial", 16), command=open_genre_page)
start_button.pack(pady=(10, 20))  # Padding to ensure proper spacing between widgets

# Create the genre frame (hidden by default)
genre_frame = tk.Frame(root, bg="white", bd=2)

def show_movies(genre):
    movie_window = Toplevel(root)
    movie_window.title(f"{genre} Movies")
    movie_window.geometry("800x600")
    
    # Set black background for the movie list
    movie_window.configure(bg="black")

    list_frame = tk.Frame(movie_window, bg="black")
    list_frame.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(list_frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    canvas = tk.Canvas(list_frame, yscrollcommand=scrollbar.set, bg="black")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=canvas.yview)

    movie_list_frame = tk.Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=movie_list_frame, anchor="nw")

    def open_movie_details(movie):
        details_window = Toplevel(movie_window)
        details_window.title(f"{movie[0]} - Details")
        details_window.geometry("500x400")
        
        # Set black background for the details window
        details_window.configure(bg="black")

        title_label = tk.Label(details_window, text=f"Title: {movie[0]}", font=("Courier New", 16, "bold"), bg="black", fg="white")
        title_label.pack(pady=10)

        year_label = tk.Label(details_window, text=f"Year: {movie[1]}", font=("Courier New", 14), bg="black", fg="white")
        year_label.pack(pady=5)

        language_label = tk.Label(details_window, text=f"Language: {movie[2]}", font=("Courier New", 14), bg="black", fg="white")
        language_label.pack(pady=5)

        description_label = tk.Label(details_window, text=f"Description: {movie[3]}", wraplength=450, justify="left", font=("Courier New", 12), bg="black", fg="white")
        description_label.pack(pady=5)

        platforms = movie[4]
        for platform, url in platforms.items():
            tk.Button(details_window, text=f"Watch on {platform}", command=lambda u=url: webbrowser.open(u)).pack(pady=5)

    for movie in movies[genre]:
        title, year, language, description, links = movie
        tk.Label(movie_list_frame, text=f"{title} ({year})", font=("Courier New", 14, "bold"), bg="black", fg="white").pack(anchor="w", padx=10, pady=(5, 0))
        tk.Label(movie_list_frame, text=f"Language: {language}", bg="black", fg="white").pack(anchor="w", padx=10)
        tk.Label(movie_list_frame, text=f"Description: {description}", bg="black", fg="white").pack(anchor="w", padx=10, pady=(0, 10))
        tk.Button(movie_list_frame, text="Details", command=lambda m=movie: open_movie_details(m)).pack(anchor="w", padx=10, pady=(0, 5))

    movie_list_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def create_genre_buttons():
    for genre in movies.keys():
        genre_button = tk.Button(genre_frame, text=genre, font=("Arial", 14), command=lambda g=genre: show_movies(g))
        genre_button.pack(fill="x", padx=20, pady=10)

create_genre_buttons()

# Chatbot integration
def open_chatbot():
    chatbot_window = Toplevel(root)
    chatbot_window.title("Movie Chatbot Assistant")
    chatbot_window.geometry("500x600")
    chatbot_window.configure(bg="#2D2D2D")

    chat_display = Text(chatbot_window, wrap="word", state="disabled", bg="#F0F0F0", font=("Courier New", 12), height=20)
    chat_display.pack(padx=10, pady=(10, 0), fill="both", expand=True)

    user_input = Entry(chatbot_window, font=("Courier New", 12), bg="#FFFFFF", justify="left")
    user_input.pack(padx=10, pady=(5, 10), fill="x")

    def send_message():
        message = user_input.get()
        if message:
            chat_display.config(state="normal")
            chat_display.insert("end", f"You: {message}\n")
            chat_display.config(state="disabled")
            chat_display.see("end")

            response = get_chatbot_response(message)
            chat_display.config(state="normal")
            chat_display.insert("end", f"Chatbot: {response}\n\n")
            chat_display.config(state="disabled")
            chat_display.see("end")

            user_input.delete(0, "end")

    send_button = Button(chatbot_window, text="Send", command=send_message, bg="#4CAF50", fg="white", font=("Courier New", 12))
    send_button.pack(pady=5)

    def get_chatbot_response(prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # Use your specific model name here
                messages=[{"role": "user", "content": prompt}],

                max_tokens=150,
                temperature=0.7,
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"Error: {e}")
            return "Sorry, I'm having trouble responding right now."

# Add a "Chat with Assistant" button on the main page
chat_button = tk.Button(home_frame, text="Chat with Assistant", font=("Arial", 16), command=open_chatbot)
chat_button.pack(pady=(10, 20))  # Position button appropriately

root.mainloop()
