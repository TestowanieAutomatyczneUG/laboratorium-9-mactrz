from src.sample.Env import Env

class Checker:
    def __init__(self):
        self.tmp = Env()

    def remainder(self, file):
        time = self.tmp.getTime()

        if time > 17:
            return self.tmp.playWavFile(file)
        else:
            return self.tmp.resetWav(file)
