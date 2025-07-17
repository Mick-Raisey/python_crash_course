# 6-5. Rivers (Bands):
# Make a dictionary containing three rivers/ bands and an album
# each band has recordered.

artists = {
    "ac/dc": "let there be rock",
    "kiss": "love gun",
    "iron maiden": "number of the beast",
    "ddep purple": "machine head",
}

for band, album in artists.items():
    print(f"{band.upper()} has an album called {album.title()}")
