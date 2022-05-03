from joinmeeting.publicscript import *

sql_res = ()


def sql_starter(line, *, _cursor, fetch="all"):
    global sql_res
    _cursor.execute(line)
    if fetch == 'all':
        sql_res = _cursor.fetchall()
    if fetch == 'one':
        sql_res = _cursor.fetchone()
    if fetch == 'many':
        sql_res = _cursor.fetchmany()
    return sql_res

def align_center(*, win_length, target_string, fontsize):
    reference = '学科: chinese language'
    refer_l = len(reference)
    new_str = '%s' % target_string
    for i in range(refer_l-len(target_string)):
        new_str += ' '
    return [(win_length-(len(new_str)*(fontsize-1)))/2, new_str]


class MWindow:
    def __init__(self, title: str, geometry: str, resizex=True, resizey=True):
        # window config
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.resizable(resizey, resizex)
        self.ico = r'logo.ico'
        self.window.iconbitmap(self.ico)
        # widget config
        self.var = None
        self.combobox = None
        self.button = None
        self.bar = None
        self.res = []

    def add_label(self, *, text='', font_style=('楷体', 14)):
        tk.Label(self.window, text=text, font=font_style).pack()

    def add_combobox(self):
        self.var = tk.StringVar()
        self.combobox = ttk.Combobox(self.window, textvariable=self.var)
        self.combobox.pack()
        self.combobox['values'] = self.res
        self.combobox.current(11)

    def get_subject(self, *, _cursor):
        exe_result = sql_starter('select * from database.table', _cursor=_cursor)
        for i in exe_result:
            self.res.append(i[0])
        return exe_result

    def add_button(self, *, text, font_style=('楷体', 14), command=None, side=None, padx=None, pady=None, frame=False):
        if not frame:
            self.button = tk.Button(self.window, text=text, font=font_style, command=command)
        if frame:
            self.button = tk.Button(self.bar, text=text, font=font_style, command=command)
        self.button.pack(side=side, padx=padx, pady=pady)

    def main_loop(self):
        self.window.mainloop()
