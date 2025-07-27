class TrackListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def add_track_to_list(self, track):
        self.model.add_track(track)
        self.view.show_message("Track added to playlist")

    def remove_track_from_list(self, track_id):
        self.model.remove_track(track_id)
        self.view.show_message(f"Track {track_id} removed from playlist")

    def print_tracks(self):
        tracks = self.model.get_all_tracks()
        self.view.display_track_list(tracks)

    def clear_playlist(self):
        self.model.clear_playlist()
        self.view.show_message("Playlist cleared")

    def create_playlist(self, title):
        if not title.strip():
            self.view.show_message("Playlist name cannot be empty!")
            return
        from database.tracklist_db import create_tracklist
        create_tracklist(title)
        self.update_playlist_listbox()
        self.view.show_message(f"Created playlist: {title}")

    def update_playlist_listbox(self):
        from database.tracklist_db import get_all_tracklists
        self.view.playlist_listbox.delete(0, 'end')
        for playlist in get_all_tracklists():
            self.view.playlist_listbox.insert('end', playlist['tracklist_name'])

    def show_add_track_popup(self, all_tracks, current_playlist_index):
        def add_callback(track):
            self.add_track_to_selected_playlist(track, current_playlist_index)
        self.view.show_add_track_popup(all_tracks, add_callback)

    def add_track_to_selected_playlist(self, track, playlist_index):
        from database.tracklist_db import get_all_tracklists, add_track_to_tracklist
        playlists = get_all_tracklists()
        if 0 <= playlist_index < len(playlists):
            playlist_id = playlists[playlist_index]['tracklist_id']
            add_track_to_tracklist(playlist_id, track['track_id'] if isinstance(track, dict) else track.track_id)
            self.update_tracks_listbox_by_id(playlist_id)
            self.view.show_message(f"Added track: {track['track_name'] if isinstance(track, dict) else track.track_title} to playlist: {playlists[playlist_index]['tracklist_name']}")
            # Tự động chọn lại playlist vừa thao tác và hiển thị track
            self.view.playlist_listbox.selection_clear(0, 'end')
            self.view.playlist_listbox.selection_set(playlist_index)
            self.view.playlist_listbox.activate(playlist_index)
        else:
            self.view.show_message("Invalid playlist selection!")

    def update_tracks_listbox_by_id(self, playlist_id):
        from database.tracklist_db import get_tracks_of_tracklist
        self.view.tracks_listbox.delete(0, 'end')
        tracks = get_tracks_of_tracklist(playlist_id)
        for track in tracks:
            self.view.tracks_listbox.insert('end', f"{track['track_id']}. {track['track_name']} - {track['artist']}")

    # Không dùng nữa, đã thay bằng update_tracks_listbox_by_id
    def update_tracks_listbox(self, playlist):
        pass

    def clear_all_playlists(self):
        from database.tracklist_db import get_all_tracklists, delete_tracklist
        playlists = get_all_tracklists()
        for playlist in playlists:
            delete_tracklist(playlist['tracklist_id'])
        self.update_playlist_listbox()
        self.view.tracks_listbox.delete(0, 'end')
        self.view.show_message("All playlists have been cleared!")