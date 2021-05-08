from urllib.request import urlopen
import pyaudio


pyaud = pyaudio.PyAudio()

rate=74100
#22100

stream = pyaud.open(format = pyaud.get_format_from_width(1),
                channels = 1,
                rate = rate,
                output = True)

url = "http://www.music.helsinki.fi/tmt/opetus/uusmedia/esim/a2002011001-e02-ulaw.wav"
#"http://www.music.helsinki.fi/tmt/opetus/uusmedia/esim/a2002011001-e02-16kHz.wav"
#"http://www.music.helsinki.fi/tmt/opetus/uusmedia/esim/a2002011001-e02-ulaw.wav"
#url = "http://www.music.helsinki.fi/tmt/opetus/uusmedia/esim/a2002011001-e02-ulaw.wav"
u = urlopen(url)

data = u.read(4096)

while data:

    stream.write(data)
    data = u.read(4096)
    print (data)   
print ("streaming completed")
