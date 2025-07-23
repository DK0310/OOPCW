import mysql.connector

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jukebox'
}

def connect():
    return mysql.connector.connect(**db_config)

def insert_track(id, title, artist, rating=0, play_count=0, mp3_path=None, image_path=None):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tracks (id, title, artist, rating, play_count, mp3_path, image_path)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            title = VALUES(title),
            artist = VALUES(artist),
            rating = VALUES(rating),
            play_count = VALUES(play_count),
            mp3_path = VALUES(mp3_path),
            image_path = VALUES(image_path)
    ''', (id, title, artist, rating, play_count, mp3_path, image_path))
    conn.commit()
    conn.close()


def delete_track(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tracks WHERE id = %s", (id,))
    conn.commit()
    conn.close()

def fetch_track(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tracks WHERE id = %s", (id,))
    result = cursor.fetchone()
    conn.close()
    return result

def fetch_all_tracks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tracks")
    result = cursor.fetchall()
    conn.close()
    return result
