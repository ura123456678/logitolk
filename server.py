import base64
import io
import threading
from socket import socket, AF_INET, SOCK_STREAM

from customtkinter import*
from tkinter import filedialog
from PIL import image

class MainWindow(CTK):
    def __init__(self):
        super().__init__()
        self.geometry('500x300')
        self.title("Chat Client")
        self.username = "юра"

        self.frame = CTKFrame(self, width=200, height=self.winfo_height())
        self.frame.pack_propagate(False)
        self.frame.configure(width=0)
        self.frame.place(x=0, y=0) 
        self.frame.is_show_menu = False
        self.frame_width =0

        self.label = CTKLabel(self.frame, text='ваше імя')
        self.label.pack(pady=30)
        self.entry = CTKEntry(self.frame)
        self.entry.pack()
        self.label_theme = CTKOptionMenu(self.frame, values=['темна', 'cвітла'], command=self.change_theme)
        self.label_theme.pack(side='bottom', pady=20)

        self.chat_field = CTKScrollableframe(self)
        self.chat_field.place(x=0, y=0)

        self.message_entry = CTKEntry(self, placeholder_text='ведітть повідомлення:', height=40)
        self.message_entry.place(x=0, y=0)
        self.send_button =  CTKButton(self, text='>', width=50,  height=40, command=self.open_message)
        self.send_button.place(x=0, y=0)

        self.open_img_button = CTKButton(self, text='h', width=50, height=40, command=self.open_image)
        self.open_img_button.place(x=0, y=0)


        self.adaptive_ui()

        self.add_massage("@", 
                         CTKImage(Image.open("1.jpg"), size=(300, 300)))
        
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(('localhost', 8080))
            hello = f"TEXT@{self.username}@[SYSTEM] {self.username}gy\n"
            self.sock.send(hello.encode('utf-8'))
            threading.Thread(target=self.recv_message, daemon=True).start()
        except Exception as e:
            self.add_message(f"немловда: {e}")

    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animete_menu *= -1
            self.btn.configure(text='<')
            self.is_show_menu()
        else:
            self.is_show_menu = True
            self.speed_animete_menu *= -1
            self.btn.configure(text='>')
            self.is_show_menu()

            self.label = CTKLabel(self.menu_frame, text='imR')
            self.label.pack(pady=30)
            self.entry = CTKEntry(self.menu_frame, placeholder_text='ваш нік')
            self.entry.pack()

            self.save_button = CTKButton(self.menu_frame, text='sev', command=self.save_name)
            self.save_button.pack()

        def show_menu(self):
            self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animate_menu)
            if not self.menu_frame.winfo_width() >= 200 and self.is_show_menu:






        def adaptive_ui(self):
            self.menu_frame.configure(height=self.winfo_height())
            self.chat_field.place(x=self.menu_frame.winfo_width())
            self.chat_field.configure(width=self.winfo_width() - self.menu_frame.winfo_width() - 20,
                                      height=self.winfo_height() - 40)
            self.send_button.place(x=self.winfo_width() - 50, y=self.winfo_height() - 40)
            self.message_entry.place(x=self.menu_frame.winfo_width(), y=self.send_button.winfo_y())
            self.message_entry.configure(
                width=self.winfo_width() - self.menu_frame.winfo_width() - 110)
            self.open_img_button.place(x=self.winfo_width() -105, y=self.send_button.winfo_y())

            self.after(50, self.adaptive_ui)

        def add_message(self, message, img=None):
            message_frame = CTKFrame(self.chat_field, fg_color='black')
            message_frame.pack(pady-5, anchor='w')
            wrapleng_size = self.winfo_width() - self.menu_frame.winfo_width() - 40

            if not img:
                CTKLabel(message_frame, text=message, wraplength=wrapLend_size,
                         text_color='green', justify='left').pack(padx=10, pady=5)
            else:
                CTKLabel(message_frame, text=message, wraplength=wrapleng_size,
                         text_color='green', image=img, compound='top',
                         iustify='left').pack(padx=10, pady=5)
                


                def recv_message(self):
                    buffer - ""
                    while True:
                        try:
                            chunk = self.sock.recv(4096)
                            if not chunk:
                                break
                            buffer +- chunk.decode('utf-8', errors='ignore')

                            while "\n" in buffer:
                                line, buffer - buffer.split("\n", 1)
                                self.handle_line(line.strip())


                        except:
                            break
                    self.sock.close()

                def handale_line(self, line):
                    if not line:
                        return
                    parts = line.split("@", 3)
                    msg_type - parts[0]

                    if msg_type == "TEXT":
                        if len(parts) >- 3:
                            author = parts[1]
                            message = parts[2]
                            self.add_message(f"{author}: {message}")
                    elif msg_type == "IMAGE":
                        if len(parts) >- 4:
                            author - parts[1]
                            filename - parts[2]
                            b64_img - parts[3]
                            try:
                                img_data = base64.b64decode(b64_img)
                                pil_img = Image.open(io.BytesIO(img_data))
                                ctk_img = CTKImage(pil_img, size=(300, 300))
                                self.add_mesage(f"{author} nadislav: {filename}", img=ctk_img)
                            except Exception as e:
                                self.add_message(f"eror: {e}")
                    else:
                        self.add_massage(line)

                def open_image(self):
                    file_name = filedialog.askopenfilename()
                    if not file_name:
                        return
                    try:
                        with open(file_name, "rb") as f:
                            raw - f.read()
                        b64_data - base64.b64encode(raw).decode()
                        short_name - os.path.basename(file_name)
                        data = f"IMAGE@{self.username}"
                         
