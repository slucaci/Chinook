import psycopg2
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

# Define the PostgreSQL database connection string
db_url = "postgresql://35389:1234@localhost:5432/chinook"  # Adjust the username, password, and database name

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create the base class for declarative models
Base = declarative_base()

# Define the class-based models

# Create a class-based model for the "Artist" table
class Artist(Base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# Create a class-based model for the "Album" table
class Album(Base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# Create a class-based model for the "Track" table
class Track(Base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Create a session
Session = sessionmaker(engine)
session = Session()

# Create the database tables if they don't exist
Base.metadata.create_all(engine)

# Query 1 - Select all records from the "Artist" table
# artists = session.query(Artist).all()  # Use `.all()` to fetch all results
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - Select only the "Name" column from the "Artist" table
# artists = session.query(Artist.Name).all()
# for artist in artists:
#     print(artist.Name)

# Query 3 - Select only "Queen" from the "Artist" table
# artists = session.query(Artist).filter_by(Name="Queen").first()
# print(artists.ArtistId, artists.Name, sep=" | ")

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
artists = session.query(Artist).filter_by(ArtistId=51).first()
print(artists.ArtistId, artists.Name, sep=" | ")

# Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - Select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, track.GenreId, track.Composer, track.Milliseconds, track.Bytes, track.UnitPrice, sep=" | ")