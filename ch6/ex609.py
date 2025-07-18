# 6-9. Favorite Places (Bands/artists)

fav_artists = {
    "mick": ["ac/dc", "kiss", "the angels", "iron maiden"],
    "viv": ["pink", "abba", "skyhooks"],
    "jess": ["oasis", "ac/dc", "suzie quatro"],
}

for name, artists in fav_artists.items():
    print(f"\n{name.title()} likes:")
    for artist in artists:
        if artist == "ac/dc":
            print(f" - {artist.upper()}")
        else:
            print(f" - {artist.title()}")
