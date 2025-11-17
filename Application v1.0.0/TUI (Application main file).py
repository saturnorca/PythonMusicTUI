import os

import ApplicationMNG


from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll, Center
from textual.widgets import Button, Static
from textual import on
from textual.widgets import Header, Select
from textual.widgets import Input
from textual.screen import Screen
import threading
import time
amg = ApplicationMNG.applicationManager()
current_playlist = 0
class Create(Screen):
    def __init__(self):
        super().__init__()
        self.playlist_name = 'Unnamed'
    def compose(self):
        yield Horizontal(
                VerticalScroll(
                    Static("Music.Py  >  Create Playlist", classes="header", id="title"),
                ),
                id = "F55"
            )
        yield Horizontal(
            Input(
                    placeholder="Playlist Name", id="create_plist_input"
                ),
                id="create_plist_input_container"
        )
        yield Horizontal(
            Button("Create Playlist", id="create_confirm"),
            id = "create_confirm_container"
        )
    @on(Input.Changed, "#create_plist_input")
    def get_playlist_name(self, event: Input.Changed):
        self.playlist_name = event.value

    @on(Button.Pressed, "#create_confirm")
    def create_new_playlist(self):
        amg.create(self.playlist_name)
        self.app.pop_screen()
class Add(Screen):

    def __init__(self):
        super().__init__()
        self.path_add = ""
        self.playlist_add = ""
    def compose(self):
        
        yield Horizontal(
            
                VerticalScroll(
                    Static("Music.Py  >  Add to Playlist", classes="header", id="title"),
                ),
                id = "F55"
            )
        yield Horizontal(
            Select(
            ((line, line) for line in amg.all_playlists), id='plist_select_add'
            ),
            id = "select_container_add"
        )
        yield Horizontal(
            Input(
                    placeholder="Playlist Name", id="plist_name_add"
                ),
                id="plist_name_add_container"
        )
        yield Horizontal(
            Button("Add Music", id="add_confirm"),
            id = "add_confirm_container"
        )
    @on(Button.Pressed, "#add_confirm")
    def add_confirm_press(self):
        amg.add(self.path_add, self.playlist_add)
        self.app.pop_screen()
    @on(Input.Changed, "#plist_name_add")
    def path_input_add(self, event: Input.Changed):
        self.path_add = event.value
    @on(Select.Changed, "#plist_select_add")
    def playlist_select_add(self, event: Select.Changed):
        self.playlist_add = amg.all_playlists.index(event.value)
class MyApp(App):

    CSS_PATH = "styles.css"
    SCREENS = {"add": Add, "create": Create}
    def __init__(self):
        super().__init__()
        self.current_playlist = 0
        self.createValue = ''
        self.shuffle_thread = None
        self.play_thread = None
        self.currently_playing = amg.getCurrentlyPlaying()
    
    def compose(self): 

        yield Horizontal(
            VerticalScroll(
                Static("Music.Py", classes="header", id="title"),
            ),
            id = "F55"
        )
        yield Horizontal(
            Select(
            ((line, line) for line in amg.all_playlists), id='plist_select'
            ),
            id = "select_container"
        )
        yield Horizontal(

            Button("Shuffle", id="shuffle"),
            Button("Play", id="play"),
            id="play_container"
        
        )
        
        yield Horizontal(
            Button("Add Music", id="add_music", classes='edit'),
            Button("Create Playlist", id="create_playlist", classes='edit'),
            id = "edit_container"
        )
        yield Horizontal(
            Static(self.currently_playing, id="playing_title")
        )
        """
        yield Horizontal(
            Input(
                placeholder="Playlist Name", id="plistName"
            ),
            id = "plistContainer"
        )
        """

        
        
    @on(Button.Pressed, "#shuffle")
    
    def on_shuffle(self):
        
        self.shuffle_thread = threading.Thread(target=amg.shuffle, args=(self.current_playlist,))
        self.shuffle_thread.start()
        #amg.shuffle(self.current_playlist)
        self.currently_playing = amg.getCurrentlyPlaying()
        time.sleep(0.01)
        update_title = self.query_one("#playing_title")
        update_title.update(amg.getCurrentlyPlaying())
    @on(Button.Pressed, "#play")
    def on_play(self):
        self.play_thread = threading.Thread(target=amg.play, args=(self.current_playlist,) )
        self.play_thread.start()
        self.currently_playing = amg.getCurrentlyPlaying()
        time.sleep(0.01)
        update_title = self.query_one("#playing_title")
        update_title.update(amg.getCurrentlyPlaying())
        #amg.play(self.current_playlist)
    @on(Button.Pressed, "#add_music")
    def on_add(self):
        #amg.create(self.createValue)
        self.push_screen('add')
    @on(Button.Pressed, "#create_playlist")
    def on_create(self):
        self.push_screen('create')
    @on(Select.Changed, "#plist_select")
    def on_plist_select(self, event: Select.Changed):
        self.current_playlist = amg.all_playlists.index(event.value)
    @on(Input.Changed, "#plistName")
    def plist_create(self, event: Input.Changed):
        self.createValue = event.value

        """
    @on(Button.Pressed, '#add')
    def on_add(self):
        amg.add(self.createValue, self.current_playlist)
    """

if __name__ == "__main__":
    app = MyApp()
    app.run()


