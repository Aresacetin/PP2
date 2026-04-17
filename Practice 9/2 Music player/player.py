from pathlib import Path
from tinytag import TinyTag
import pygame as pg
import json

class Player:

    def __init__(self):
        self.current_track = 1
        self.is_playing = False
        self.tracks = []
        self.playlist_name = ""
        self.current_track_name = ""
        self.current_track_path = ""
        self.current_track_duration = 0
        self.current_track_tag = None
        self.playback_seconds = 0.0

    def load_playlist(self, path):
        print(f"load_playlist: {path}")
        self.playlist_name = path
        
        # scanning for music files
        for p in Path(path).rglob('*'):
            if p.is_file():
                if p.suffix in [".mp3", ".wav", ".opus"]:
                    self.tracks.append(str(p))

        print(f"{len(self.tracks)} tracks are currently loaded")

        # try to load previous track
        try:
            with open("playlist_data.json", "r") as f:
                data = json.load(f)
                current_track_name = data[path]["current_track_name"]
                try:
                    self.current_track = self.tracks.index(current_track_name) + 1
                except ValueError:
                    pass
        except FileNotFoundError:
            pass

        self.load_track(self.current_track)

    def load_track(self, position):
        # reset playback
        self.playback_seconds = 0.0

        # check position
        self.current_track = position
        if self.current_track > len(self.tracks):
            self.current_track = len(self.tracks)
        elif self.current_track <= 0:
            self.current_track = 1

        # load track
        print(f"load_track: {self.current_track}: {self.tracks[self.current_track - 1]}")
        self.current_track_path = str(self.tracks[self.current_track - 1])
        self.current_track_name = self.current_track_path.lstrip(self.playlist_name + "/").rstrip(".opus").rstrip(".mp3").rstrip(".wav")
        self.current_track_tag = TinyTag.get(self.current_track_path)
        self.current_track_duration = self.current_track_tag.duration

        pg.mixer.music.load(self.current_track_path)
        # if playing then play track after load
        if self.is_playing:
            pg.mixer.music.play(start=self.playback_seconds)

    def pause(self):
        print("pause")
        self.is_playing = False
        pg.mixer.music.stop()

    def resume(self):
        print("resume")
        self.is_playing = True
        pg.mixer.music.play(start=self.playback_seconds) 


    def play_at(self, seconds):
        if seconds < 0:
            seconds = 0
        print(f"playing at: {seconds} seconds")
        self.playback_seconds = seconds
        # if playing then update pg module
        if self.is_playing:
            pg.mixer.music.play(start=self.playback_seconds)

    def skip_forward(self):
        print("skip_forward")
        self.load_track(self.current_track + 1)

    def skip_back(self):
        print("skip_back")
        self.load_track(self.current_track - 1)

    def forward(self):
        print("forward")
        self.play_at(self.playback_seconds + 10)

    def back(self):
        print("back")
        self.play_at(self.playback_seconds - 10)

    def update(self, delta):
        if self.is_playing:
            self.playback_seconds += delta / 1000.0

        # check if track finished
        if self.playback_seconds > self.current_track_duration:
            self.skip_forward()

    def quit(self):
        # save current track on quit
        with open("playlist_data.json", "w") as f:
            data = json.dumps({self.playlist_name: {"current_track_name": self.current_track_path}})
            f.write(data)

