from flask import Flask, request, jsonify
import youtube_dl
from .database import get_db_connection
from .transcription import download_video, transcribe_audio, generate_summary

app = Flask(__name__)

@app.route('/youtube-channel', methods=['GET'])
def youtube_channel():
    # Get YouTube channel link from query parameters
    youtube_channel_link = request.args.get('link')

    # Fetch video titles, descriptions, and download videos
    ydl_opts = {
        'ignoreerrors': True,
        'extract_flat': 'in_playlist',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_channel_link, download=False)
        videos = [(entry['title'], entry['description'], entry['id']) for entry in info_dict['entries'] if entry is not None]

    # Get database connection
    conn, c = get_db_connection()

    # Transcribe audio, generate summaries, and store data in SQLite database
    for title, description, video_id in videos:
        download_video(video_id)  # download video
        transcript = transcribe_audio('video.wav')  # transcribe audio
        summary = generate_summary(title, description, transcript)
        c.execute('INSERT INTO videos (title, description, transcript, summary) VALUES (?, ?, ?, ?)', (title, description, transcript, summary))
    conn.commit()

    return 'Data fetched and stored successfully.'

@app.route('/summarized-videos', methods=['GET'])
def summarized_videos():
    conn, c = get_db_connection()
    c.execute('SELECT * FROM videos')
    videos = c.fetchall()
    return jsonify(videos)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
