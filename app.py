import os
from pytube import YouTube
from TikTokApi import TikTokApi
import instaloader

def download_youtube_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(save_path)
        print(f'YouTube video downloaded: {stream.title}')
    except Exception as e:
        print(f"Error downloading YouTube video: {str(e)}")

