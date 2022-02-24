import time
from playsound import playsound
import threading
import os

class AudioThread(threading.Thread):
    def run(self):
        playsound("BadApple.mp3")

f = open('BAsource.txt', 'r')
frame_raw = f.read()
f.close()
frames = frame_raw.split('\nSPLIT')
init_time = time.time()
class VideoThread(threading.Thread):
	def run(self):
		while time.time() <= init_time + 5257:
			os.system('cls')
			print(frames[int((time.time()-init_time)*24)])
			time.sleep(0.1)
            
audio_thread = AudioThread(name="Audio Thread")
video_thread = VideoThread(name="Video Thread")
audio_thread.start()
video_thread.start()
