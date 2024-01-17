#!/usr/bin/env python3

import os
import subprocess
import tkinter as tk
from tkinter import filedialog

class VideoDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader")
        self.root.configure(bg='#303030')  # Set background color

        self.urls = []

        self.output_folder = os.path.expanduser('~/Projects/')

        self.create_widgets()

    def create_widgets(self):
        # Entry for URLs
        tk.Label(self.root, text="Enter URLs (comma-separated):", fg='white', bg='#303030').grid(row=0, column=0)
        self.url_entry = tk.Entry(self.root, width=50, bg='#404040', fg='white')
        self.url_entry.grid(row=0, column=1)

        # Button to download videos
        tk.Button(self.root, text="Download Videos", command=self.download_videos, bg='#007ACC', fg='white').grid(row=1, column=1)

        # Button to browse output folder
        tk.Button(self.root, text="Browse Output Folder", command=self.browse_output_folder, bg='#007ACC', fg='white').grid(row=2, column=1)

        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = tk.Label(self.root, text="", fg='white', bg='#303030')
        self.progress_bar.grid(row=3, column=1)

        # Percentage label
        self.percentage_label = tk.Label(self.root, text="", fg='white', bg='#303030')
        self.percentage_label.grid(row=4, column=1)

    def browse_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_folder = folder_path

    def download_videos(self):
        urls_input = self.url_entry.get()
        self.urls = [url.strip() for url in urls_input.split(',') if url.strip()]

        if self.urls:
            # Show progress bar
            self.show_progress_bar()

            # Download videos
            for i, url in enumerate(self.urls):
                self.download_single_video(url, self.output_folder)
                self.update_progress(i + 1, len(self.urls))

    def show_progress_bar(self):
        self.progress_var.set(0.0)
        self.root.update()

        colors = ['#009688', '#4CAF50', '#8BC34A', '#CDDC39', '#FFEB3B']  # Color gradient

        for i in range(1, 101):
            color_index = min((i - 1) // 20, 4)
            self.progress_bar.config(text='=' * i, fg=colors[color_index])
            self.progress_var.set(i)
            self.root.update()
            self.root.after(30)

        self.progress_bar.config(text="\n")
        self.root.update()

    def download_single_video(self, url, output_folder):
        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Download video using YT-DLP
        subprocess.run(['C:\\Users\\khari\\yt-dlp.exe', '-o', f'{output_folder}/%(title)s.%(ext)s', url])

    def update_progress(self, current, total):
        percentage = int((current / total) * 100)
        self.percentage_label.config(text=f"Progress: {percentage}%")
        self.root.update()

    def browse_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_folder = folder_path

if __name__ == '__main__':
    root = tk.Tk()
    app = VideoDownloaderGUI(root)
    root.mainloop()

