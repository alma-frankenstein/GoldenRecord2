# combines app/__init__.py, app/routes.py, and microblog.py from Grinberg

from flask import Flask, render_template, flash, redirect, url_for, request, abort
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.urls import url_parse
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import *
from forms import EmptyForm, PostForm

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Song': Song}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add_a_song', methods=['GET', 'POST'])
def add_a_song():
    form = PostForm()
    if request.method == 'POST':
        song = Song(song_name=form.song.data, artist_name=form.artist.data, song_link=form.song_link.data)
        db.session.add(song)
        db.session.commit()
        flash('you have posted a song')
        return redirect(url_for('browse'))
    return render_template('add_a_song.html',form=form)




@app.route('/browse')
def browse():
    page = request.args.get('page', 1, type=int)
    songs = Song.query.order_by(Song.timestamp.desc()).paginate(page, app.config['SONGS_PER_PAGE'], False)
    next_url = url_for('browse', page=songs.next_num) \
        if songs.has_next else None
    prev_url = url_for('browse', page=songs.prev_num) \
        if songs.has_prev else None
    return render_template('browse.html', songs=songs.items, next_url=next_url, prev_url=prev_url)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(413)
def file_too_large(e):
    return render_template('413.html'), 413

@app.errorhandler(400)
def bad_request(e):
    return render_template('400.html'), 400