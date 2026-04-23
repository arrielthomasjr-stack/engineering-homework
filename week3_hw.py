class Track(object):
    total_tracks_created = 0

    def __init__(self, title, duration_minutes, duration_seconds):
        self.title = title
        self._duration_minutes = duration_minutes
        self._duration_seconds = duration_seconds
        self._play_count = 0
        Track.total_tracks_created += 1

    def get_title(self):
        return self.title

    def get_duration(self):
        return f"{self._duration_minutes}:{self._duration_seconds:02d}"

    def get_play_count(self):
        return self._play_count

    def play(self):
        self._play_count += 1
        print(f"▶ Playing: {self.title}")

    def __str__(self):
        return f"{self.title} ({self.get_duration()})"

    def __repr__(self):
        return f"Track({self.title!r}, {self._duration_minutes}, {self._duration_seconds})"

    def __eq__(self, other):
        if not isinstance(other, Track):
            return False
        return self.title == other.title and self.get_duration() == other.get_duration()


class Song(Track):
    def __init__(self, artist, album, title, duration_minutes, duration_seconds):
        super().__init__(title, duration_minutes, duration_seconds)
        self.artist = artist
        self.album = album

    def play(self):
        super().play()
        print(f"♪ Now playing {self}")

    def __str__(self):
        return f"{self.title} — {self.artist} ({self.get_duration()})"


class Podcast(Track):
    def __init__(self, host, episode, title, duration_minutes, duration_seconds):
        super().__init__(title, duration_minutes, duration_seconds)
        self.host = host
        self.episode = int(episode)

    def play(self):
        super().play()
        print(f"🎙 Streaming {self}")

    def __str__(self):
        return f"Ep {self.episode}: {self.title} — hosted by {self.host}"


class Playlist:
    def __init__(self, name, tracks=None):
        self.name = name
        self._tracks = list(tracks) if tracks is not None else []

    def set_List(self, track):
        self._tracks.append(track)

    def set_remove(self, title):
        for track in self._tracks:
            if track.title == title:
                self._tracks.remove(track)
                return
        raise ValueError(f"No track found with title: {title}")

    def total_duration(self):
        total_seconds = 0
        for track in self._tracks:
            total_seconds += track._duration_minutes * 60 + track._duration_seconds

        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}"

    def most_played(self):
        if not self._tracks:
            return None
        return max(self._tracks, key=lambda track: track.get_play_count())

    def __len__(self):
        return len(self._tracks)

    def __contains__(self, title):
        return any(track.title == title for track in self._tracks)

    def __iter__(self):
        return iter(self._tracks)

    def __add__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return Playlist(f"{self.name} + {other.name}", self._tracks + other._tracks)

    def __str__(self):
        lines = [f"{i + 1}. {track}" for i, track in enumerate(self._tracks)]
        lines.append(f"Total: {self.total_duration()}")
        return "\n".join(lines)

def main():
        song1 = Song("John B", "Hot Topic", "Call me Tonight", 3, 60)
        song2 = Song("Shorty T", "The Trip", "We had a Party", 2,50)
        song3 = Song("Sexy Lew", "Meltdown", "Going Streakin", 4, 50)
        podcast1 = Podcast("Curly Moe", 2, "Chivalry", 5, 30)
        playlist1 = Playlist("Lets go", tracks=[song1, song2, song3])
        playlist2 = Playlist("Sexy", tracks=[song1, song2, song3])

        song1.play()
        song2.play()
        song3.play()
        podcast1.play()
        print(len(playlist1))
        print(len(playlist2))
        print(iter(playlist1))
        print(iter(playlist2))
        print(playlist1 + playlist2)
        print(Track.total_tracks_created)
        print(Playlist.most_played(playlist1))

if __name__ == "__main__":
    main()