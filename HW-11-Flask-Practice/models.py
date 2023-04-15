from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()

class Song(db.Model):
    __tablename__ = 'Song'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    author_id = db.Column(db.Integer, db.ForeignKey('Author.id'))
    album_id = db.Column(db.Integer, db.ForeignKey('Album.id'))

class Album(db.Model):
    __tablename__ = 'Album'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    author_id = db.Column(db.Integer, db.ForeignKey('Author.id'))
    songs = db.relationship('Song', backref='album', lazy=True)

class Author(db.Model):
    __tablename__ = 'Author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    birth_date = db.Column(db.DateTime, default=datetime.now())
    songs = db.relationship('Song', backref='author', lazy=True)

class AuthorSong(db.Model):
    __tablename__ = 'AuthorSong'
    author_id = db.Column(db.Integer, db.ForeignKey('Author.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('Song.id'), primary_key=True)

# class Song_AuthorSong(db.Model):
#     __tablename__ = 'Song_AuthorSong'
#     Song_id = db.Column(db.Integer, db.ForeignKey('Song.id'), primary_key=True)
#     AuthorSong_song_id = db.Column(db.Integer, db.ForeignKey('AuthorSong.song_id'), primary_key=True)

# class Author_AuthorSong(db.Model):
#     __tablename__ = 'Author_AuthorSong'
#     Author_id = db.Column(db.Integer, db.ForeignKey('Author.id'), primary_key=True)
#     AuthorSong_author_id = db.Column(db.Integer, db.ForeignKey('AuthorSong.author_id'), primary_key=True)
