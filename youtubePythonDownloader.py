# Program for downloading video or audio from YouTube |Ignacio D.López|

# First install this dependency in this directory: pip install yt-dlp

import yt_dlp

# Enter the URL for the download
url = input("Enter video URL: ")

# Ask the user if they want to download the video or audio
choice = input("Do you want to download the video (V) or audio (A)? ").strip().lower()

if choice == 'v':
    ydl_opts = {
    'format': 'best',  # Download the best quality available
    }
elif choice == 'a':
    ydl_opts = {
        'format': 'bestaudio/best',
    }
else:
    print("Invalid choice. Please choose 'V' for video or 'A' for audio.")
    exit(1)

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed successfully!")
