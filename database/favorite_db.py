import mysql.connector
from .track_db import get_track

DB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jukebox'
}

def connect():
    return mysql.connector.connect(**DB_CONFIG)

def add_favorite(track_id):
    conn = connect()
    cursor = conn.cursor()
    
    track = get_track(track_id)
    if not track:
        conn.close()
        return
    track_name = track['track_name']
    artist = track['artist']
    # Thêm vào bảng favorite (nếu chưa có)
    cursor.execute(
        "INSERT IGNORE INTO favorites (track_id, track_name, artist) VALUES (%s, %s, %s)",
        (track_id, track_name, artist)
    )
    conn.commit()
    conn.close()

def get_all_favorites():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT * FROM favorites
    ''')
    result = cursor.fetchall()
    conn.close()
    return result

def remove_favorite(track_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM favorites WHERE track_id = %s', (track_id,))
    conn.commit()
    conn.close()

def clear_all_favorites():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM favorites')
    conn.commit()
    conn.close()

def is_favorite(track_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM favorites WHERE track_id = %s', (track_id,))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0