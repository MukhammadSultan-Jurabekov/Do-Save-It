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

def download_tiktok_video(url, save_path):
    try:
        api = TikTokApi()
        video = api.video(url=url)
        video_data = video.bytes()
        video_id = video.id
        file_path = os.path.join(save_path, f'tiktok_{video_id}.mp4')
        with open(file_path, 'wb') as f:
            f.write(video_data)
        print(f'TikTok video downloaded: {file_path}')
    except Exception as e:
        print(f"Error downloading TikTok video: {str(e)}")

