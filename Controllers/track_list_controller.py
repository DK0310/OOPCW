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
        from Models.track_list import TrackList
        playlist = TrackList.add_playlist(title)
        self.update_playlist_listbox()
        self.view.show_message(f"Created playlist: {title}")
        return playlist

    def update_playlist_listbox(self):
        from Models.track_list import TrackList
        self.view.playlist_listbox.delete(0, 'end')
        for playlist in TrackList.get_all_playlists():
            self.view.playlist_listbox.insert('end', playlist.title)

    def show_add_track_popup(self, all_tracks, current_playlist_index):
        def add_callback(track):
            self.add_track_to_selected_playlist(track, current_playlist_index)
        self.view.show_add_track_popup(all_tracks, add_callback)

    def add_track_to_selected_playlist(self, track, playlist_index):
        from Models.track_list import TrackList
        playlists = TrackList.get_all_playlists()
        if 0 <= playlist_index < len(playlists):
            playlists[playlist_index].tracks.append(track)
            self.update_tracks_listbox(playlists[playlist_index])
            self.view.show_message(f"Added track: {track.track_title} to playlist: {playlists[playlist_index].title}")
        else:
            self.view.show_message("Invalid playlist selection!")

    def update_tracks_listbox(self, playlist):
        self.view.tracks_listbox.delete(0, 'end')
        for track in playlist.get_tracks():
            self.view.tracks_listbox.insert('end', f"{track.track_id}. {track.track_title} - {track.artist}")

    def clear_all_playlists(self):
        from Models.track_list import TrackList
        TrackList.clear_all_playlists()
        self.update_playlist_listbox()
        self.view.tracks_listbox.delete(0, 'end')
        self.view.show_message("All playlists have been cleared!")