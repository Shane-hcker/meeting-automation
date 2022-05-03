from joinmeeting.publicscript import *


def user_input_sql(_cursor):
    root = TopWindow(title='MySQL 8.0 语句输入', geometry='700x800')
    root.add_frame(height=25, bground='skyblue')

    def run_sql():
        try:
            sqlines = str(input_tpad.get(1.0, tk.END)).lower()
            sqlines = sqlines.strip('\n').rstrip(';').split(';')
            for i in range(len(sqlines)):
                execution = sql_starter(sqlines[i], _cursor=_cursor)
                for j in execution:
                    return_tpad.insert('end', f'{j}\n')
        except Exception:
            msgbox.showerror(title='错误', message='小错误')

    root.add_button(text='执行', command=run_sql, side=tk.LEFT, padx=25, pady=10, frame=True)

    input_tpad = root.add_textarea(height=20, width=100)
    gen_textarea(t_name=input_tpad)

    return_tpad = root.add_textarea(height=15, width=100)
    gen_textarea(t_name=return_tpad)
