"""Seed file to make sample data for db."""

from models import Playlist, Song,PlaylistSong, db
from app import app

db.drop_all()
db.create_all()

Playlist.query.delete()
Song.query.delete()

p1 = Playlist(name='Gym Workout Songs', description='These songs are great to listen to while jogging on the treadmill!')
p2 = Playlist(name='Relaxation Songs', description='These songs really help you relax and unwind.')
p3 = Playlist(name='Happy Songs', description='These songs will put you in a great mood!')
p4 = Playlist(name='Sad Songs')

db.session.add_all([p1, p2, p3, p4])
db.session.commit()

s1 = Song(title='Champagne Problems', artist='Taylor Swift')
s2 = Song(title='Blowing In The Wind', artist='Bob Dylan')
s3 = Song(title='Happy', artist='Bruno Mars')
s4 = Song(title='Wake Me Up', artist='avicci')
s5 = Song(title='Cardigan', artist='Taylor Swift')
s6 = Song(title='22', artist='Taylor Swift')
s7 = Song(title='Walking on Sunshine', artist='Katrina and the Waves')
s8 = Song(title='Pump Up the Jam', artist='Technotronic')
s9 = Song(title='What a Wonderful World', artist='Louis Armstrong')
s10 = Song(title='Fix You', artist='Coldplay')

db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10])
db.session.commit()

ps1 = PlaylistSong(playlist_id=4, song_id=1)
ps2 = PlaylistSong(playlist_id=2, song_id=2)
ps3 = PlaylistSong(playlist_id=3, song_id=3)
ps4 = PlaylistSong(playlist_id=1, song_id=4)
ps5 = PlaylistSong(playlist_id=4, song_id=5)
ps6 = PlaylistSong(playlist_id=3, song_id=6)
ps7 = PlaylistSong(playlist_id=3, song_id=7)
ps8 = PlaylistSong(playlist_id=1, song_id=8)
ps9 = PlaylistSong(playlist_id=2, song_id=9)

db.session.add_all([ps1, ps2, ps3, ps4, ps5, ps6, ps7, ps8, ps9])
db.session.commit()