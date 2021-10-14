from heavy_app import db, login
from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(140))
    song_name = db.Column(db.String(140))
    song_link = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Song {}'.format(self.song_name)
