import streamlit as st
from pytube import YouTube
import os
import validators

st.title("YouTube Video Downloader ")
video_url = st.text_input("Enter the YouTube video URL:")

if st.button("Get the video"):
    if not validators.url(video_url):
        st.error("Please enter a valid YouTube video URL.")
    else:
        try:
            st.write("Please wait, we are getting your video....")

            yt = YouTube(video_url)

            video_stream = yt.streams.filter(
                adaptive=True, file_extension='mp4', only_video=True).first()

            audio_stream = yt.streams.filter(
                adaptive=True, file_extension='mp4', only_audio=True).first()

            video_stream.download(filename='video.mp4')
            audio_stream.download(filename='audio.mp4')

            # Merging video and audio using ffmpeg
            output_filename = 'YoutubeVideoDownloader.mp4'
            os.system(f'ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac {output_filename}')
            os.remove("video.mp4")
            os.remove("audio.mp4")

            st.success("Your video is ready to be downloaded!")

            # Providing a download link for the merged video
            with open(output_filename, 'rb') as f:
                st.download_button('Download Video', f,file_name=output_filename)

            # Remove the merged video file after download link is provided
            os.remove(output_filename)

        except Exception as e:
            st.error(f"An error occurred: {e}")