from database.tracklist_db import create_tracklist, get_all_tracklists, add_track_to_tracklist, get_tracks_of_tracklist, delete_tracklist


class TrackListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
   
    def create_playlist(self, title):
        if not title.strip():
            self.view.show_message("Playlist name cannot be empty!")
            return
        if title in [playlist['tracklist_name'] for playlist in get_all_tracklists()]:
            self.view.show_message("Playlist with this name already exists!")
            return
        create_tracklist(title)
        self.update_playlist_listbox()
        self.view.show_message(f"Created playlist: {title}")

    def update_playlist_listbox(self):
        self.view.playlist_listbox.delete(0, 'end')
        for playlist in get_all_tracklists():
            self.view.playlist_listbox.insert('end', playlist['tracklist_name'])

    def show_add_track_popup(self, all_tracks, current_playlist_index):
        def add_callback(track):
            self.add_track_to_selected_playlist(track, current_playlist_index)
        self.view.show_add_track_popup(all_tracks, add_callback)

    def add_track_to_selected_playlist(self, track, playlist_index):
        if not track:
            self.view.show_message("Please select a track to add!")
            return

        playlists = get_all_tracklists()
        if playlist_index < 0 or playlist_index >= len(playlists):
            self.view.show_message("Invalid playlist selected!")
            return

        playlist_id = playlists[playlist_index]['tracklist_id']
        existing_tracks = get_tracks_of_tracklist(playlist_id)
        track_id = track['track_id'] if isinstance(track, dict) else track.track_id
        existing_ids = [t['track_id'] if isinstance(t, dict) else t.track_id for t in existing_tracks]
        if track_id in existing_ids:
            self.view.show_message("Track already exists in this playlist!")
            return

        add_track_to_tracklist(playlist_id, track_id)
        self.view.show_message("Track added to playlist!")
        self.update_tracks_listbox_by_id(playlist_id)

    def update_tracks_listbox_by_id(self, playlist_id):
        self.view.tracks_listbox.delete(0, 'end')
        tracks = get_tracks_of_tracklist(playlist_id)
        for track in tracks:
            self.view.tracks_listbox.insert('end', f"{track['track_id']}. {track['track_name']} - {track['artist']}")


    def clear_all_playlists(self):
        playlists = get_all_tracklists()
        for playlist in playlists:
            delete_tracklist(playlist['tracklist_id'])
        self.update_playlist_listbox()
        self.view.tracks_listbox.delete(0, 'end')
        self.view.show_message("All playlists have been cleared!")

