from joinmeeting.publicscript import *


def modify_data(_cursor):
    root = TopWindow(title='Modify', geometry='600x500', resizey=False, resizex=False)
    root.add_label(text='修改对象：')
    class_, code, pwd = 'class', 'code', 'pwd'
    radchoice_save = ['class']
    root.add_radio(text='class', value=class_, save_list=radchoice_save)
    root.add_radio(text='code', value=code, save_list=radchoice_save)
    root.add_radio(text='password', value=pwd, save_list=radchoice_save)

    root.add_label(text='target value')
    target_entry = root.add_entry()

    root.add_label(text='clue in class')
    modify_clue = root.add_entry()

    def begin_mod():
        radvar = radchoice_save[-1]
        if radvar != class_:
            sql_starter(f"update database.table set {radvar}='{int(target_entry.get())}' "
                        f"where class='{str(modify_clue.get())}'", _cursor=_cursor)
        else:
            sql_starter(f"update database.table set class='{str(target_entry.get())}' "
                        f"where class='{str(modify_clue.get())}'", _cursor=_cursor)

    root.add_button(text='运行', command=begin_mod)
    # "update tencentmeeting set xxx='' where class=''"
