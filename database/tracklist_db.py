import mysql.connector

DB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jukebox'
}

def connect():
    return mysql.connector.connect(**DB_CONFIG)

def create_tracklist(tracklist_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tracklists (tracklist_name)
        VALUES (%s)
    ''', (tracklist_name,))
    conn.commit()
    conn.close()

def get_tracklist(tracklist_id):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tracklists WHERE tracklist_id = %s', (tracklist_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_tracklists():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tracklists')
    result = cursor.fetchall()
    conn.close()
    return result

def update_tracklist(tracklist_id, tracklist_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE tracklists SET tracklist_name = %s WHERE tracklist_id = %s', (tracklist_name, tracklist_id))
    conn.commit()
    conn.close()

def delete_tracklist(tracklist_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tracklists WHERE tracklist_id = %s', (tracklist_id,))
    conn.commit()
    conn.close()

def add_track_to_tracklist(tracklist_id, track_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tracklist_tracks (tracklist_id, track_id)
        VALUES (%s, %s)
    ''', (tracklist_id, track_id))
    conn.commit()
    conn.close()

def remove_track_from_tracklist(tracklist_id, track_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM tracklist_tracks WHERE tracklist_id = %s AND track_id = %s
    ''', (tracklist_id, track_id))
    conn.commit()
    conn.close()

def get_tracks_of_tracklist(tracklist_id):
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT t.* FROM tracks t
        JOIN tracklist_tracks tt ON t.track_id = tt.track_id
        WHERE tt.tracklist_id = %s
    ''', (tracklist_id,))
    result = cursor.fetchall()
    conn.close()
    return result
