#!/usr/bin/env python

import os
import tkinter as tk
from file_xfer_framework import *

# Necessary for Ubuntu to set environmental display variable
if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')

bg_color = 'black'
fg_color = '#24FF24'
font_style = 'Courier New'

class Main_GUI(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Canvas.__init__(self, master, height=700, width=1000)
        
        # Background image
        self.bg_file = 'geometree.png'
        self.bg_img = tk.PhotoImage(file=self.bg_file)
        self.bg_label = tk.Label(tk_root, image=self.bg_img, anchor='ne')
        self.bg_label.place(relwidth=1,relheight=1)

        # Widget: Welcome banner
        self.text1 = 'File Transfer Time Estimator'
        self.label_title = tk.Label(tk_root, text=self.text1, bg=bg_color, 
                        fg=fg_color, anchor='n', font=(font_style, 26))
        self.label_title.place(relx=.15, relwidth=.63, relheight=.07)

        # Frame: Dataset
        self.frame_dataset = tk.Frame(tk_root, bg=bg_color)
        self.frame_dataset.place(rely=.2, anchor='w')

        # Label: Dataset
        self.text2 = "Dataset Size:"
        self.label_dataset = tk.Label(self.frame_dataset, text=self.text2, 
                        bg=bg_color, fg=fg_color, font=(font_style, 18)
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
                        bg=bg_color, fg=fg_color, selectcolor='#000000',
                        font=(font_style, 16)).pack()

        # Frame 2: Throughput units
        self.frame_units = tk.Frame(tk_root, bg=bg_color)
        self.frame_units.place(rely=.42, anchor='w')

        # Lbel: Throughput units
        self.text3 = "Throughput Units:"
        self.label_units = tk.Label(self.frame_units, text=self.text3, 
                        bg=bg_color, fg=fg_color,font=(font_style, 18)
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
                        value=value,bg=bg_color, fg=fg_color,
                        selectcolor='#000000',font=(font_style, 16)).pack()
                        
        # Frame 3: Data transfer amount total
        self.frame_total = tk.Frame(tk_root, bg=bg_color)
        self.frame_total.place(rely=.59, anchor='w')

        # Label: Data transfer total
        self.text4 = "Data Transfer Total Amount:"
        self.label_total = tk.Label(self.frame_total, text=self.text4, bg=bg_color,
                        fg=fg_color, font=(font_style, 18)).pack(side='top')                

        # Scale Slider: Amount of data
        self.data_total_int = tk.IntVar()
        scale1 = tk.Scale(self.frame_total, bg=bg_color, fg=fg_color, from_=0,
                        to=1000, orient='horizontal', width=20, length=300,
                        variable=self.data_total_int).pack(anchor='w')

        # Frame 4: Data transfer speed
        self.frame_speed = tk.Frame(tk_root, bg=bg_color)
        self.frame_speed.place(rely=.73, anchor='w')

        # Label: Data transfer speed
        self.text5 = "Data Transfer Speed:"
        self.label_speed = tk.Label(self.frame_speed, text=self.text5, 
                        bg=bg_color, fg=fg_color, font=(font_style, 18)
                        ).pack(side='top')                  

        # Scale Slider: Transfer speed
        self.transfer_speed_int = tk.IntVar()
        scale2 = tk.Scale(self.frame_speed, bg=bg_color, fg=fg_color, from_=0, 
                        to=1000, orient='horizontal', width=20, length=300,
                        variable=self.transfer_speed_int).pack(anchor='w')

        # Frame 5: Request results button
        self.frame_button = tk.Frame(tk_root, bg=bg_color)
        self.frame_button.place(relx=.14, rely=.83)

        # Label: Button label 
        self.label_button = tk.Label(self.frame_button, text='Click me!', 
                        bg=bg_color, fg=fg_color, font=(font_style, 10)
                        ).pack(side='top')

        # Button: Get results
        self.text6 = "Calculate Total\nTransfer Time"
        self.button_button = tk.Button(self.frame_button, bg=bg_color, 
                            fg=fg_color, text=self.text6,
                            font=(font_style, 18),  
                            command=lambda: self.button_click(
                                self.dataset_size_init.get(),
                                self.units_init.get(),
                                self.data_total_int.get(),
                                self.transfer_speed_int.get()
                                )).pack(anchor='w')

        # Frame 6: File transfer time results
        self.frame_results = tk.Frame(tk_root, bg=bg_color)
        self.frame_results.place(relx=.41, rely=.85)

        # Label: Heading/Title
        self.text7 = "File Transfer Time:"
        self.label_results = tk.Label(self.frame_results, text=self.text7, 
                        bg=bg_color, fg=fg_color, font=(font_style, 18)
                        ).pack(side='top')

        # Entry: Display results
        self.resultstext = tk.StringVar()
        self.entry_results = tk.Entry(self.frame_results, bg=bg_color, 
                        fg=fg_color, textvariable=self.resultstext, 
                        width=58, font=(font_style,12)).pack()  


    def button_click(self,val1,val2,val3,val4):
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
            self.resultstext.set(self.converted)
            
        except ZeroDivisionError:
            self.error = "   ERROR!! Unable to perform math. Please check values."
            self.resultstext.set(self.error)


if __name__ == '__main__':
    tk_root = tk.Tk()
    GUI = Main_GUI(tk_root).pack()
    tk_root.mainloop()