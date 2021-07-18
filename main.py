from tkinter import *
from tkinter.filedialog import *
import moviepy.editor as mp  # pip install moviepy
import os
import threading


class GUI(Tk):
    def __init__(self, title="Window", width=200, height=200, bg="white", resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()


def formatName(fileName):
    if len(fileName) > 20:
        return f"{fileName[:8]}....{fileName[-8:]}"
    else:
        return fileName


def openVideo():
    file = askopenfilename(defaultextension=".mp4", filetypes=[("All Files", "*.*")])
    file_name = formatName(os.path.basename(file))
    if file_name != "":
        openFile.set(file_name)
        openedFile.set(file)


def extracting(file, save):
    clip = mp.VideoFileClip(rf"{file}")
    clip.audio.write_audiofile(rf"{save}")
    extractFile.set("Done...")


def extractAudio():
    file = openedFile.get()
    save = savedFile.get()
    try:
        extractFile.set("Extracting...")
        thread = threading.Thread(target=extracting, args=(file, save))
        thread.daemon = 1
        thread.start()
    except Exception as e:
        extractFile.set("Some Error occurred")


def saveAudio():
    file = asksaveasfilename(initialfile='result.mp3', defaultextension=".mp3", filetypes=[("All Files", "*.*")])
    file_name = formatName(os.path.basename(file))
    if file_name != "":
        saveFile.set(file_name)
        savedFile.set(file)


if __name__ == '__main__':
    BACKGROUND = "#61edc3"

    # Making Window
    root = GUI(title="Audio Extractor", width=370, height=150, bg=BACKGROUND)

    # Open Frame
    open_frame = Frame(root, bg=BACKGROUND)
    open_frame.pack(fill=X, pady=10)
    openBtn = Button(open_frame, text="Open Video", command=openVideo, width=9)
    openFile = StringVar()
    openedFile = StringVar()
    openLabel = Label(open_frame, textvariable=openFile, bg=BACKGROUND, font="lucida 14")
    openBtn.grid(row=0, column=0, padx=10)
    openLabel.grid(row=0, column=1, padx=10)

    # Save Frame
    save_frame = Frame(root, bg=BACKGROUND)
    save_frame.pack(fill=X, pady=10)
    saveBtn = Button(save_frame, text="Save to", command=saveAudio, width=9)
    saveFile = StringVar()
    savedFile = StringVar()
    saveLabel = Label(save_frame, textvariable=saveFile, bg=BACKGROUND, font="lucida 14")
    saveBtn.grid(row=0, column=0, padx=10)
    saveLabel.grid(row=0, column=1, padx=10)

    # Extract Frame
    extract_frame = Frame(root, bg=BACKGROUND)
    extract_frame.pack(fill=X, pady=10)
    extractBtn = Button(extract_frame, text="Extract", command=extractAudio, width=9)
    extractFile = StringVar()
    extractLabel = Label(extract_frame, textvariable=extractFile, bg=BACKGROUND, font="lucida 14")
    extractBtn.grid(row=0, column=0, padx=10)
    extractLabel.grid(row=0, column=1, padx=10)

    # Starting
    root.start()
