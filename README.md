# Please change the file paths according to your system paths.


# For Windows and Linux
FFMPEG should be installed for Whsiper AI to run properly. 

# For Linux
If using Linux, can download triton for better gpu-acceleration.


# Working
## 1) audio_text_both.py
i) First part extracts the audio and stores it in a folder.
ii) The next part uses Whisper Ai to get the words spoken and their time stamps.
iii) Before storing these words in a .csv file with timestamps, the bow file is called to check if the word is present in the bag of words. If yes, the word is added to the csv else no.

## 2) bow.py
i) This file contains the Bag Of Words which we will be using to check the word. 
ii) Stemming is done to reduce  the word to its root word.
iii) returns True if the word is present else False.

