import multiprocessing
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from cam_det import cam_det


def gui_mainloop(the_q, the_e):
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

        def show_frames(self, the_q, the_e):
            img = the_q.get()
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)
            self.camera_label.after(10, self.show_frames, the_q, the_e)

    root = tk.Tk()
    root.title("LEGO sorter")
    main = MainFrame(root)
    main.show_frames(the_q, the_e)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x600")
    root.mainloop()


def cam_loop(the_q, event):
    width, height = 64, 64
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


    while True:
        cam_det(cap)
        _, img = cap.read()
        if img is not None:
            img = cv2.flip(img, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
            the_q.put(img)
            event.set()


if __name__ == "__main__":
    q_frame = multiprocessing.Queue(1)
    e_frame = multiprocessing.Event()

    p_cap = multiprocessing.Process(target=cam_loop, args=(q_frame, e_frame))
    p_gui = multiprocessing.Process(target=gui_mainloop, args=(q_frame, e_frame))

    try:
        p_cap.start()
        p_gui.start()


        p_cap.join()
        p_gui.join()


    except KeyboardInterrupt:
        p_cap.terminate()
        p_gui.terminate()

