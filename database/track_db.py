import mysql.connector

# Cấu hình kết nối
DB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jukebox',
    'port': 3306,
}

def connect():
    return mysql.connector.connect(**DB_CONFIG)

def create_track(track_name, artist, play_count=0, rating=0, mp3_path=None, image_path=None):
    conn = connect()
    cursor = conn.cursor()
    mp3_data = None
    image_data = None

    if mp3_path:
        with open(mp3_path, "rb") as f: 
            mp3_data = f.read()
    if image_path:
        with open(image_path, "rb") as f:
            image_data = f.read()

    cursor.execute('''
        INSERT INTO tracks (track_name, artist, play_count, rating, mp3_file, image_file)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (track_name, artist, play_count, rating, mp3_data, image_data))
    conn.commit()
    conn.close()

def get_track(track_id):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tracks WHERE track_id = %s', (track_id,))
    result = cursor.fetchone()
    conn.close()
    if result and result['mp3_file'] is not None:
        print("mp3_file type:", type(result['mp3_file']))
        print("mp3_file size:", len(result['mp3_file']))
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
