-- Table for music artists
CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    name TEXT
);

-- Table for albums, each album belongs to one artist
CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    name TEXT,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

-- Table for songs, each song belongs to one album
CREATE TABLE song (
    id INTEGER PRIMARY KEY,
    name TEXT,
    album_id INTEGER,
    track_number INTEGER,
    duration INTEGER,  -- length of song in seconds
    FOREIGN KEY (album_id) REFERENCES album(id)
);
