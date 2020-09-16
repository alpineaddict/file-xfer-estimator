#!/usr/bin/env python

'''
GUI portion of app which provides user with radio buttons and sliders to
calculate how long it will take to transfer a set of data at a particular
transfer speed.
'''

import os
import tkinter as tk
from file_xfer_framework import *

# Necessary for Ubuntu to set environmental display variable
if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')

BG_COLOR   = 'black'
FG_COLOR   = '#24FF24'
FONT_STYLE = 'Courier New'

class GuiWindow(tk.Frame):
    '''Build and display entire GUI'''
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        # Background image
        self.bg_file = 'geometree.png'
        self.bg_img = tk.PhotoImage(file=self.bg_file)
        self.bg_label = tk.Label(tk_root, image=self.bg_img, anchor='ne')
        self.bg_label.place(relwidth=1,relheight=1)

        # Widget: Welcome banner
        self.text1 = 'File Transfer Time Estimator'
        self.label_title = tk.Label(tk_root, text=self.text1, bg=BG_COLOR,
                        fg=FG_COLOR, anchor='n', font=(FONT_STYLE, 26))
        self.label_title.place(relx=.15, relwidth=.63, relheight=.07)

        # Frame: Dataset
        self.frame_dataset = tk.Frame(tk_root, bg=BG_COLOR)
        self.frame_dataset.place(rely=.2, anchor='w')

        # Label: Dataset
        self.text2 = "Dataset Size:"
        self.label_dataset = tk.Label(self.frame_dataset, text=self.text2,
                        bg=BG_COLOR, fg=FG_COLOR, font=(FONT_STYLE, 18)
                        ).pack(side='top')

        # Radiobutton: Dataset size
        self.dataset_optns = [
            ("KB", "KB"),
            ("MB", "MB"),
            ("GB", "GB"),
            ("TB", "TB"),
        ]

        self.dataset_size_init = tk.StringVar()
        self.dataset_size_init.set("KB")

        for text, value in self.dataset_optns:
            tk.Radiobutton(self.frame_dataset,text=text,
                        variable=self.dataset_size_init, value=value,
                        bg=BG_COLOR, fg=FG_COLOR, selectcolor='#000000',
                        font=(FONT_STYLE, 16)).pack()

        # Frame 2: Throughput units
        self.frame_units = tk.Frame(tk_root, bg=BG_COLOR)
        self.frame_units.place(rely=.42, anchor='w')

        # Lbel: Throughput units
        self.text3 = "Throughput Units:"
        self.label_units = tk.Label(self.frame_units, text=self.text3,
                        bg=BG_COLOR, fg=FG_COLOR,font=(FONT_STYLE, 18)
                        ).pack(side='top')

        # Radiobutton: Throughput units
        self.throughput_optns = [
            ("Kbps", "Kbps"),
            ("Mbps", "Mbps"),
            ("Gbps", "Gbps"),
        ]

        self.units_init = tk.StringVar()
        self.units_init.set("Kbps")

        for text, value in self.throughput_optns:
            tk.Radiobutton(self.frame_units,text=text, variable=self.units_init,
                        value=value,bg=BG_COLOR, fg=FG_COLOR,
                        selectcolor='#000000',font=(FONT_STYLE, 16)).pack()

        # Frame 3: Data transfer amount total
        self.frame_total = tk.Frame(tk_root, bg=BG_COLOR)
        self.frame_total.place(rely=.59, anchor='w')

        # Label: Data transfer total
        self.text4 = "Data Transfer Total Amount:"
        self.label_total = tk.Label(self.frame_total, text=self.text4, bg=BG_COLOR,
                        fg=FG_COLOR, font=(FONT_STYLE, 18)).pack(side='top')

        # Scale Slider: Amount of data
        self.data_total_int = tk.IntVar()
        scale1 = tk.Scale(self.frame_total, bg=BG_COLOR, fg=FG_COLOR, from_=0,
                        to=1000, orient='horizontal', width=20, length=300,
                        variable=self.data_total_int).pack(anchor='w')

        # Frame 4: Data transfer speed
        self.frame_speed = tk.Frame(tk_root, bg=BG_COLOR)
        self.frame_speed.place(rely=.73, anchor='w')

        # Label: Data transfer speed
        self.text5 = "Data Transfer Speed:"
        self.label_speed = tk.Label(self.frame_speed, text=self.text5,
                        bg=BG_COLOR, fg=FG_COLOR, font=(FONT_STYLE, 18)
                        ).pack(side='top')

        # Scale Slider: Transfer speed
        self.transfer_speed_int = tk.IntVar()
        scale2 = tk.Scale(self.frame_speed, bg=BG_COLOR, fg=FG_COLOR, from_=0,
                        to=1000, orient='horizontal', width=20, length=300,
                        variable=self.transfer_speed_int).pack(anchor='w')

        # Frame 5: Request results button
        self.frame_button = tk.Frame(tk_root, bg=BG_COLOR)
        self.frame_button.place(relx=.14, rely=.83)

        # Label: Button label
        self.label_button = tk.Label(self.frame_button, text='Click me!',
                        bg=BG_COLOR, fg=FG_COLOR, font=(FONT_STYLE, 10)
                        ).pack(side='top')

        # Button: Get results
        self.text6 = "Calculate Total\nTransfer Time"
        self.button_button = tk.Button(self.frame_button, bg=BG_COLOR,
                            fg=FG_COLOR, text=self.text6,
                            font=(FONT_STYLE, 18),
                            command=lambda: self.button_click(
                                self.dataset_size_init.get(),
                                self.units_init.get(),
                                self.data_total_int.get(),
                                self.transfer_speed_int.get()
                                )).pack(anchor='w')

        # Frame 6: File transfer time results
        self.frame_results = tk.Frame(tk_root, bg=BG_COLOR)
        self.frame_results.place(relx=.41, rely=.85)

        # Label: Heading/Title
        self.text7 = "File Trafile_xfer_gui.pynsfer Time: FIX ME"
        self.label_results = tk.Label(self.frame_results, text=self.text7,
                        bg=BG_COLOR, fg=FG_COLOR, font=(FONT_STYLE, 18)
                        ).pack(side='top')

        # Entry: Display results
        self.results_text = tk.StringVar()
        self.entry_results = tk.Entry(self.frame_results, bg=BG_COLOR,
                        fg=FG_COLOR, textvariable=self.results_text,
                        width=58, font=(FONT_STYLE,12)).pack()

    def button_click(self, val1, val2, val3, val4):
        '''
        Accept values from widgets as input. Plug numbers into functions.
        '''
        self.dataset_size   = val1
        self.units          = val2
        self.data_total     = val3
        self.transfer_speed = val4

        try:
            self.bits = convert_to_bits(self.dataset_size, self.data_total)
            self.seconds = get_transfer_time(self.units, self.bits, self.transfer_speed)
            self.converted = convert_time(self.seconds)
            self.results_text.set(self.converted)

        except ZeroDivisionError:
            self.error = "   ERROR!! Unable to perform math. Please check values."
            self.results_text.set(self.error)


if __name__ == '__main__':
    tk_root = tk.Tk()
    gui = GuiWindow(tk_root).pack()
    tk_root.mainloop()
