from moviepy.editor import VideoFileClip
import warnings
import whisper
import csv
from bow import BagOfWords

video_path = "D:/Capstone_Project/Videos/testing3.mp4"
cvt_video = VideoFileClip(video_path)
ext_audio = cvt_video.audio
ext_audio.write_audiofile("Audio_ext/audio_ext2.mp3")

print("Audio extracted successfully!")




# import os
# os.environ["FFMPEG_BINARY"] = "C:/ProgramData/chocolatey/lib/ffmpeg/tools/ffmpeg/bin/ffmpeg.exe"


warnings.filterwarnings("ignore", message="Failed to launch Triton kernels")


model = whisper.load_model("small")
result = model.transcribe("D:/Capstone_Project/Audio_ext/audio_ext2.mp3",word_timestamps=True)


file_path = "D:/Capstone_Project/text_time/text3.csv"

bows=BagOfWords()

# Function to write word-level transcriptions to CSV
def write_to_csv(result, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["start_time", "end_time", "word"])

        writer.writeheader()

        # Iterate over the segments and words
        for segment in result['segments']:
            for word_info in segment['words']:
                word = word_info['word']
                if bows.check_word(word) is True:
                    start_time = word_info['start']
                    end_time = word_info['end']
                    start_time = round(start_time,2)
                    end_time= round(end_time,2)

                    writer.writerow({"start_time": start_time, "end_time": end_time, "word": word})
                else:
                    continue


write_to_csv(result, file_path)

print("Word-level transcription with timestamps has been saved to 'text3.csv'.")