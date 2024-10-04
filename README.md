# Do-Save-It

**Do-Save-It** is a Python application that allows you to download videos and images from YouTube, TikTok, and Instagram.

## Requirements

The application requires the following Python libraries:

- `pytube`
- `TikTokApi`
- `instaloader`

### Installing Dependencies

Ensure that you are in the correct project directory. Follow these steps to install the required dependencies:

1. Create a virtual environment:

```
   python3 -m venv venv
```
2. Activate the virtual environment:

```
source venv/bin/activate
```

- For Windows:


```
venv\Scripts\activate
```
Install the dependencies:


```
pip install pytube TikTokApi instaloade
```

### How to Use
Run the app.py script:


```
python app.py
```
Enter the URL of a video or image from one of the supported platforms (YouTube, TikTok, Instagram) when prompted in the terminal.

The content will automatically be downloaded to the ./downloads folder.

Example Usage
```Please provide the URL (YouTube, TikTok, or Instagram): https://www.youtube.com/watch?v=dQw4w9WgXcQ
YouTube video downloaded: Rick Astley - Never Gonna Give You Up
```

### Project Structure
```
Do-Save-It/
│
├── app.py              # Main script to download content
├── venv/               # Virtual environment (created after running python -m venv)
└── downloads/          # Folder where downloaded files are saved
Supported Platforms
YouTube: Downloads videos in the highest available resolution.
TikTok: Downloads videos using the TikTokApi library.
Instagram: Downloads content from Instagram profiles.```
### Note
Please remember that downloading and using content from social media platforms may violate copyright laws and platform terms of service. Make sure you comply with legal and platform requirements when downloading and using content.