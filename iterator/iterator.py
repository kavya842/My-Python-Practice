a=[10,20,30,40,50]
i=iter(a)
print(next(i))
# print(next(i))
# print(next(i))

"""Music Player using Iterator"""
class Playlist:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0

    def __iter__(self):
        return self   
    
    def __next__(self):
        if self.index < len(self.songs):
            song = self.songs[self.index]
            self.index += 1
            return song
        else:
            raise StopIteration  
         
songs_list = ["Song1", "Song2", "Song3"]
playlist = Playlist(songs_list)
for song in playlist:
    print("Now Playing:", song)