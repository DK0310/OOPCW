-- To create the tracks tabl for jukebox database
CREATE TABLE tracks (
    track_id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    rating FLOAT DEFAULT 0,
    play_count INT DEFAULT 0,
    mp3_file LONGBLOB,
    image_file LONGBLOB
);

-- To create the tracklists and tracklist_tracks tables for jukebox database
CREATE TABLE tracklists (
    tracklist_id INT AUTO_INCREMENT PRIMARY KEY,
    tracklist_name VARCHAR(255) NOT NULL
);

CREATE TABLE tracklist_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tracklist_id INT NOT NULL,
    track_id INT NOT NULL,
    FOREIGN KEY (tracklist_id) REFERENCES tracklists(tracklist_id) ON DELETE CASCADE,
    FOREIGN KEY (track_id) REFERENCES tracks(track_id) ON DELETE CASCADE,
    UNIQUE(tracklist_id, track_id)
);

-- To create the favorites table for jukebox database
CREATE TABLE favorites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_id INT NOT NULL,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    FOREIGN KEY (track_id) REFERENCES tracks(track_id) ON DELETE CASCADE,
    UNIQUE(track_id)

);


