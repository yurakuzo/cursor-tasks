from flask import Flask, jsonify

from datetime import datetime

from models import db, Song, Album, Author, AuthorSong

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_AppleMusic.db'
db.init_app(app)

@app.route('/songs')
def songs():
    songs = Song.query.all()    
    authors = Author.query
    albums = Album.query
    
    song_list = {song.name: (authors.filter_by(id=song.author_id).first().name,
                             albums.filter_by(id=song.album_id).first().name)
                 for song in songs}
    return jsonify(song_list)


@app.route('/songs')
@app.route('/songs/<int:id>')
def songs_by_id(id):
    songs = Song.query.filter_by(id=id)
    authors = Author.query
    albums = Album.query
    
    song_list = {song.name: (authors.filter_by(id=song.author_id).first().name,
                             albums.filter_by(id=song.album_id).first().name)
                 for song in songs}
    return jsonify(song_list)


if __name__ == '__main__':
    with app.app_context():
        
        # Clear all records in db
        # db.session.query(Author).delete()
        # db.session.query(Song).delete()
        # db.session.query(Album).delete()
        # db.session.query(AuthorSong).delete()
        
        # db.session.commit()
        
        db.create_all()
        
        author1 = Author(name='Pink Floyd', birth_date=datetime(1980, 1, 1))
        
        author2 = Author(name='VIA Vodogray', birth_date=datetime(1990, 1, 1))
        
        db.session.add(author1)
        db.session.add(author2)
        db.session.commit()


        song1 = Song(name='The Great Gig In The Sky', author=author1)
        song2 = Song(name='Brain Damage', author=author1)
        
        song3 = Song(name='Try Trembity', author=author2)
        
        db.session.add(song1)
        db.session.add(song2)
        db.session.add(song3)
        db.session.commit()

        album1 = Album(name='The Dark Side of the Moon', author_id=author1.id, songs=[song1, song2])
        db.session.add(album1)
        db.session.commit()
        
        album2 = Album(name='Single', author_id=author2.id, songs=[song3])
        db.session.add(album2)
        db.session.commit()

        author_song1 = AuthorSong(author_id=author1.id, song_id=song1.id)
        
        author_song2 = AuthorSong(author_id=author1.id, song_id=song2.id)
        
        author_song3 = AuthorSong(author_id=author2.id, song_id=song3.id)
        
        db.session.add(author_song1)
        db.session.add(author_song2)
        db.session.add(author_song3)
        db.session.commit()


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    