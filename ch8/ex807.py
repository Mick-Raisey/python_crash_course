# 8-7. Album:
# Write a function called make_album() that builds a dictionary
# describing a music album.


def make_album(artist_name, album_title, tracks=None):
    """Returns a dictionary of an artist and an album"""
    album = {
        "artist": artist_name,
        "album": album_title,
    }

    if tracks:
        album["tracks"] = tracks

    return album


album_info = make_album("ac/dc", "let there be rock", tracks=8)
print(album_info)

album_info = make_album("deep purple", "machine head")
print(album_info)
