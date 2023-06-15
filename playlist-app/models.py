"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    songs = db.relationship('Song', secondary='playlists_songs', backref='playlists')



class Song(db.Model):
    
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)


class PlaylistSong(db.Model):

    __tablename__ = 'playlists_songs'

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False, primary_key=True)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

