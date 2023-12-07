from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download(url, path, res):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        stream_to_download = streams.get_by_resolution(res)
        if stream_to_download is None:
            print(f"No stream available with resolution {res}")
        else:
            stream_to_download.download(output_path=path)
            print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    url = input("Enter a YouTube url: ")
    res = int(input("Enter resolution - 1.720p 2.480p 3.360p: "))

    if res == 1:
        res = "720p"
    elif res == 2:
        res = "480p"
    elif res == 3:
        res = "360p"
    else:
        print("Select a valid resolution!")
    
    path = open_file_dialog()

    if path:
        print("Starting download..")
        download(url, path, res)
    else:
        print("Please select a valid location to download.")
