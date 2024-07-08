# YouTube Video Downloader
This is a simple Streamlit application that downloads YouTube videos by merging video and audio streams into a single MP4 file.

## Code Analysis
The provided code is a Streamlit application that downloads a YouTube video and merges its video and audio streams into a single MP4 file. Here's a breakdown of the code:

1. **Imports:**
- streamlit for the web interface.
- pytube for downloading YouTube videos.
- os for interacting with the operating system.
- validators for validating the URL.

2. **Streamlit Interface:**

- The title of the app is set to `YouTube Video Downloader`.
- A text input is provided for the user to enter the YouTube video URL.
- A button is provided to trigger the video download.

3. **Download Logic:**
- he URL is validated to ensure it's a valid YouTube link.
- If valid, it fetches the video and audio streams using pytube.
- The streams are downloaded separately as video.mp4 and audio.mp4.
- The ffmpeg command is used to merge the video and audio streams into a single file.
- The merged file is provided as a download link.
- Temporary files are cleaned up after the process.

## Features
- Enter a YouTube video URL to download.
- Downloads video and audio streams separately.
- Merges the streams into a single MP4 file using `ffmpeg`.
- Provides a download link for the merged video file.

## Requirements
To run this application, you need to have the following dependencies installed:

- `streamlit`
- `pytube`
- `validators`
You can install the dependencies using the provided `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## Installation
1. **Clone the repository:**
```sh
git clone https://github.com/im-yjoshua/Youtube-Video-Downloader.git
cd youtube-video-downloader

```

2. **Install the required Python packages:**
```sh
pip install -r requirements.txt
```
3. Ensure `ffmpeg` is installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

## Usage
To run the Streamlit application, use the following command:
```sh
streamlit run youtubeDownloader.py
```
This will start a local server. Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

# How It Works
1. Enter the YouTube video URL in the provided input box.
2. Click the "Get the video" button.
3. The app validates the URL and starts downloading the video and audio streams.
4. The streams are merged into a single MP4 file using `ffmpeg`.
5. A download link for the merged video file is provided.
6. Temporary files are cleaned up after the download link is generated.

# Error Handling
- The app checks if the provided URL is a valid YouTube link.
- If any error occurs during the download or merging process, an error message is displayed.

# License
This project is licensed under the MIT License.

# Contributing
Contributions are welcome! Please open an issue or submit a pull request.

# Acknowledgements
[Streamlit](https://streamlit.io/)

[Pytube](https://pytube.io/en/latest/)

[FFmpeg](https://ffmpeg.org/)