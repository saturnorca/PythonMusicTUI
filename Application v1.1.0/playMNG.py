import ApplicationMNG
#from TUI import MyApp, app
class playMNG():
    CURRENTLY_PLAYING = ""
    def __init__(self, val):
        self.play_value = val
    def get_val(self):
        return self.play_value
    def set_val(self, val):
        self.play_value = val
    #def updateTitle(self):
        #app.updateTitle()