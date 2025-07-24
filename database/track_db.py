import mysql.connector

# Cấu hình kết nối
DB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jukebox'
}

def connect():
    return mysql.connector.connect(**DB_CONFIG)

def create_track(track_name, artist, play_count=0, rating=0):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tracks (track_name, artist, play_count, rating)
        VALUES (%s, %s, %s, %s)
    ''', (track_name, artist, play_count, rating))
    conn.commit()
    conn.close()

def get_track(track_id):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tracks WHERE track_id = %s', (track_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_tracks():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tracks')
    result = cursor.fetchall()
    conn.close()
    return result

def update_track(track_id, track_name=None, artist=None, play_count=None, rating=None):
    conn = connect()
    cursor = conn.cursor()
    fields = []
    values = []
    if track_name is not None:
        fields.append('track_name = %s')
        values.append(track_name)
    if artist is not None:
        fields.append('artist = %s')
        values.append(artist)
    if play_count is not None:
        fields.append('play_count = %s')
        values.append(play_count)
    if rating is not None:
        fields.append('rating = %s')
        values.append(rating)
    if not fields:
        conn.close()
        return
    values.append(track_id)
    sql = f'UPDATE tracks SET {", ".join(fields)} WHERE track_id = %s'
    cursor.execute(sql, tuple(values))
    conn.commit()
    conn.close()

def delete_track(track_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tracks WHERE track_id = %s', (track_id,))
    conn.commit()
    conn.close()
