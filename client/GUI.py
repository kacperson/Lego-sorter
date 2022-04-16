import tkinter as tk
import cv2
from PIL import Image, ImageTk


class MainFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.camera_container = tk.Canvas(self, width=64, height=64)
        self.info_container = tk.Frame(self)

        self.camera_container.pack(side=tk.LEFT)
        self.info_container.pack(side=tk.RIGHT)

        self.model_label = tk.Label(self.info_container, text="Model")
        self.case_label = tk.Label(self.info_container, text="Case")
        self.number_label = tk.Label(self.info_container, text="Number of bricks")
        self.model_label.grid(column=0, row=0, columnspan=1)
        self.case_label.grid(column=0, row=1, columnspan=1)
        self.number_label.grid(column=0, row=2, columnspan=1)

        self.model_text = tk.Text(self.info_container, height=1, width=40)
        self.case_text = tk.Text(self.info_container, height=1, width=40)
        self.number_text = tk.Text(self.info_container, height=1, width=40)
        self.model_text.grid(column=1, row=0, columnspan=1)
        self.case_text.grid(column=1, row=1, columnspan=1)
        self.number_text.grid(column=1, row=2, columnspan=1)
        self.add_button = tk.Button(self.info_container, text="Add to database")
        self.add_button.grid(column=1, row=3, columnspan=1)

        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 64)
        self.camera_label = tk.Label(self.camera_container)
        self.camera_label.grid()
        #self.show_frames()

    def show_frames(self):
        while True:
            ret, frame = self.camera.read()
            if ret:
                cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = ImageTk.PhotoImage(Image.fromarray(cv2img))
                self.camera_container.create_image(0, 0, image=img, anchor=tk.NW)
                self.camera_container.update()
        #self.camera_container.after(1, self.show_frames())


if __name__ == "__main__":
    root = tk.Tk()
    root.title("LEGO sorter")
    main = MainFrame(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x600")
    root.mainloop()
