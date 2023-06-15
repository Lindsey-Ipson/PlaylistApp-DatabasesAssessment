from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, Optional
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    
    name = StringField(
        'Name',
        validators=[InputRequired()]
    )
    description = StringField(
        'Description',
        validators=[InputRequired(), Optional()]
    )

    
class SongForm(FlaskForm):

    title = StringField(
        'Title',
        validators=[InputRequired()]
    )
    artist = StringField(
        'Artist',
        validators=[InputRequired()]
    )


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)




