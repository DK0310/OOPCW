class MusicPlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def next_track(self):
        if self.model.current_index < len(self.model.tracks) - 1:
            self.model.current_index += 1
        self.display_current_track()

    def previous_track(self):
        if self.model.current_index > 0:
            self.model.current_index -= 1
        self.display_current_track()

    def back_to_home(self):
        self.model.current_index = 0
        self.display_current_track()

    def display_current_track(self):
        track = self.model.get_current_track()
        if track:
            self.view.print(track.track_title, track.artist, track.track_id)

