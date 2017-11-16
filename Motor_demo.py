#!/usr/bin/env python3
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
from gpiozero import PWMOutputDevice
def main():
recognizer = aiy.cloudspeech.get_recognizer()
recognizer.expect_phrase('on')
recognizer.expect_phrase('off')
button = aiy.voicehat.get_button()
aiy.audio.get_recorder().start()
pwm = PWMOutputDevice(4)
while True:
print('Press the button and speak')
button.wait_for_press()
print('Listening...')
text = recognizer.recognize()
if text is None:
print('Sorry, I did not hear you.')
else:
print('You said "', text, '"')
if 'on' in text:
print('Turning motor on')
pwm.on()
elif 'off' in text:
print('Turning motor off')
pwm.off()
if __name__ == '__main__':
main()
