from joinmeeting.publicscript import *


def gen_textarea(*, t_name, expand=tk.YES):
    t_name.pack(expand=expand, fill=tk.BOTH)
    # set scroll
    scroll = tk.Scrollbar(t_name)
    t_name.config(yscrollcommand=scroll.set)
    scroll.config(command=t_name.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)


class TopWindow(MWindow):
    def __init__(self, title: str, geometry: str, resizex=True, resizey=True):
        super().__init__(title, geometry, resizey, resizex)
        self.entry = None
        self.radiobtn = None
        self.radio_var = tk.StringVar()
        self.radio_choice = ['2']
        self.textpad = None

    def add_entry(self, *, method='pack', setx=None, sety=None, show=None):
        self.var = tk.IntVar()
        self.entry = tk.Entry(self.window, show=show, textvariable=self.var)
        if method == 'pack':
            self.entry.pack()
        if method == 'place':
            self.entry.place(x=setx, y=sety)
        return self.entry

    def add_radio(self, *, text, value, save_list: list, method='pack', setx=None, sety=None):
        self.radiobtn = tk.Radiobutton(self.window, text=text, value=value, variable=self.radio_var,
                                       command=lambda: save_list.append(value))
        if method == 'place':
            self.radiobtn.place(x=setx, y=sety)
        if method == 'pack':
            self.radiobtn.pack()

    def add_label(self, *, text='', font_style=('楷体', 14), method='pack', setx=None, sety=None,
                  fground=None, bground=None):
        if method == 'pack':
            tk.Label(self.window, text=text, font=font_style, fg=fground, bg=bground).pack()
        if method == 'place':
            tk.Label(self.window, text=text, font=font_style, fg=fground, bg=bground).place(x=setx, y=sety)

    def add_frame(self, *, height: int, bground=None):
        self.bar = tk.Frame(self.window, height=height, bg=bground)
        self.bar.pack(expand=tk.NO, fill=tk.X)
        return self.bar

    def add_textarea(self, *, height: int, width: int, font_style=('FiraCode NF', 12)):
        self.textpad = tk.Text(self.window, font=font_style, height=height, width=width)
        gen_textarea(t_name=self.textpad)
        return self.textpad
