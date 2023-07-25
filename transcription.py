import youtube_dl
import speech_recognition as sr
import openai

# Set up your OpenAI API key
openai.api_key = 'apikey'

def download_video(video_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'video.wav',  # name of the audio file
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={video_id}'])  # download video

def transcribe_audio(audio_filename):
    r = sr.Recognizer()
    with sr.AudioFile(audio_filename) as source:
        audio_file = r.record(source)
    return r.recognize_google(audio_file)

def generate_summary(title, description, transcript):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to summarize youtube video titles, descriptions, and transcripts, please summarize each title, description, and transcript."},
            {"role": "user", "content": f"Title: {title}\nDescription: {description}\nTranscript: {transcript}"}
        ],
        max_tokens=100,
        temperature=0.5,
        n=1,
    )
    return response['choices'][0]['message']['content'].strip()
