from joinmeeting.publicscript import *


def insert_delete(connection, _cursor):
    root = TopWindow(title='添加删除', geometry='350x275', resizex=False, resizey=False)
    root.add_label(text='请输入你要添加或删除的数据名称(class)', font_style=('楷体', 12))
    class_enter = root.add_entry()
    root.add_label(text='输入会议码\n(如果需要删除数据则无需输入会议码)', font_style=('楷体', 12))
    code_enter = root.add_entry()
    root.add_label(text='会议密码(可选)', font_style=('楷体', 12))
    pwd_enter = root.add_entry(show='*')

    def ask_if_continue():
        if not msgbox.askyesno(title='OK', message='是否继续'):
            _cursor.close()
            connection.close()
            msgbox.showinfo(title='OK', message='重启生效')

    def insert_data():
        if pwd_enter.get() != '':
            sql_starter("insert into database.table values('%s', %d, %d)"
                        % (class_enter.get(), int(code_enter.get()), int(pwd_enter.get())), _cursor=_cursor)
        else:
            sql_starter("insert into database.table values('%s', %d, null)"
                        % (class_enter.get(), int(code_enter.get())), _cursor=_cursor)

        ask_if_continue()

    def delete_data():
        sql_starter("delete from database.table where class='%s'" % class_enter.get(), _cursor=_cursor)
        ask_if_continue()

    root.add_button(text='添加', command=insert_data)
    root.add_button(text='删除', command=delete_data)
