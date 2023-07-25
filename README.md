# OpenAI GPT 3.5 Turbo YouTube Video Summarization Application

This repository contains a Flask web application for summarizing videos from a given YouTube channel. The application allows users to provide a YouTube channel link, fetch video data, transcribe audio, generate summaries, and store the summarized information in an SQLite database.
 # Demo
 ![image](https://github.com/graylan0/gptyoutube/assets/34530588/45e459ab-36f2-406e-8cdc-58fcec2f150f)

**Features:**

1. **YouTube Channel Data Retrieval**: The app uses the `youtube_dl` library to fetch video titles, descriptions, and IDs from a specified YouTube channel link.

2. **Transcription**: The application downloads the videos from the YouTube channel and transcribes the audio content into text using a speech-to-text system.

3. **Summarization**: The app generates a concise summary for each video by combining its title, description, and transcribed content.

4. **Database Storage**: The summarized video data, including title, description, transcript, and summary, is stored in an SQLite database using a connection obtained from the `database.py` module.

**Endpoints:**

- **/youtube-channel [GET]**: Accepts a query parameter `link` containing the YouTube channel URL. Fetches video data, transcribes audio, generates summaries, and stores the information in the database. Returns a success message upon completion.

- **/summarized-videos [GET]**: Retrieves all the summarized video data from the SQLite database and returns it in JSON format.

**How to Run:**

1. Install the required dependencies 
``` pip install .```

1. Ensure you have a working database connection, as specified in `database.py`.
2. Run by typing `gptyoutube`.
3. Access the backend server endpoints via appropriate HTTP requests.
