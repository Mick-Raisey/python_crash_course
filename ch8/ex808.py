# 8-8. User Albums:
# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop


def make_album(artist_name, album_title, tracks=None):
    """Returns a dictionary of an artist and an album"""
    album = {
        "artist": artist_name,
        "album": album_title,
    }

    if tracks:
        album["tracks"] = int(tracks)

    return album


artist_prompt = "Enter an artist: "
album_prompt = "What album did they record: "
print("Enter 'q' at ay time to quit")

while True:
    artist = input(artist_prompt)
    if artist == "q":
        break

    album = input(album_prompt)
    if album == "q":
        break

    tracks = input("How many tracks 'enter in unsure' ")

    album = make_album(artist, album, tracks)
    print(album)

print("\nThanks for responding!")
