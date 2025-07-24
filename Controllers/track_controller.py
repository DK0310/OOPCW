class TrackController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def new_rating(self, rating):
        self.model.set_rating(rating)
        self.view.show_message(f"Rating updated to {rating}")

    def add_track(self, title, artist):
        self.model.track_title = title
        self.model.artist = artist
        self.view.show_message("Track details updated")

    def delete_track(self, track_id):
        self.view.show_message(f"Track {track_id} deleted (dummy placeholder)")

    def add_to_favorite(self, track_id):
        self.view.show_message(f"Track {track_id} added to favorites (dummy placeholder)")

    def print_tracks(self):
        self.view.display_track_info(self.model)

    def show_detail(self, track):
        if isinstance(track, dict):
            detail = (
                f"ID: {track.get('track_id', '')}\n"
                f"Title: {track.get('track_name', track.get('track_title', ''))}\n"
                f"Artist: {track.get('artist', '')}\n"
                f"Rating: {track.get('rating', '')}\n"
                f"Play Count: {track.get('play_count', '')}"
            )
        else:
            detail = (
                f"ID: {track.track_id}\n"
                f"Title: {track.track_title}\n"
                f"Artist: {track.artist}\n"
                f"Rating: {track.rating}\n"
                f"Play Count: {track.play_count}"
            )
        self.view.display_detail(detail)
