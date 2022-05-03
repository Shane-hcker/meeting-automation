from joinmeeting.publicscript import *


def search_data(_cursor):
    root = TopWindow(title='查询数据', geometry='400x600', resizex=False, resizey=True)
    root.add_label(text='选择查询的数据', font_style=('楷体', 12))
    root.add_radio(text='class', value='1', save_list=root.radio_choice)
    root.add_radio(text='code', value='2', save_list=root.radio_choice)
    root.add_label(text='输入查询数据', font_style=('楷体', 12))
    search_val_enter = root.add_entry()

    def get_and_search():
        """
        :variable cpe:  check if password exists
        """
        if len(root.radio_choice) == 0:
            msgbox.showerror(title='错误！', message='请先选择按钮')
        else:
            get_radio = root.radio_choice[-1]
            get_entry = search_val_enter.get()

            def display_cpe_data(name):
                if name is not None:
                    subject = f'学科: {name[0]}'
                    align_value = align_center(win_length=400, fontsize=11, target_string=subject)
                    addlabel = lambda appendstring: root.add_label(text=align_value[1] + appendstring,
                                                                   font_style=('楷体', 11), fground='red',
                                                                   bground='white', method='place',
                                                                   setx=align_value[0], sety=170)
                    if name[2] is None:
                        addlabel(f'\n 会议码: {name[1]}')
                    else:
                        addlabel(f'\n 会议码: {name[1]}\n 密码: {name[2]}')
                else:
                    msgbox.showerror(title='错误', message='输入有误 请重新输入')

            if get_radio == '1':
                cpe = sql_starter("select * from database.table where class='%s'" % str(get_entry),
                                  _cursor=_cursor, fetch='one')
                display_cpe_data(cpe)

            if get_radio == '2':
                try:
                    cpe = sql_starter("select * from database.table where code='%d'" % int(get_entry),
                                      _cursor=_cursor, fetch='one')
                    display_cpe_data(cpe)
                except Exception:
                    msgbox.showerror(title='错误', message='输入有误 请重新输入')

    root.add_button(text='查询', command=get_and_search)
