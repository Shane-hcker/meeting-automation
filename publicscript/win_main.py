from joinmeeting.publicscript import *


conn = pymysql.connect(
    # Manual Configuration
    host='localhost',
    port=3306,
    database='database',
    user='user',
    password='password',
    autocommit=True
)
_cursor = conn.cursor()

# 创建主窗口
mwindow = MWindow('腾讯会议自动化脚本', '350x200', False, False)
mwindow.add_label(text='选择你的课程', font_style=('楷体', 16))

# 设置下拉菜单
start_get_subject = mwindow.get_subject(_cursor=_cursor)
mwindow.add_combobox()
get_value = mwindow.combobox.get()
mwindow.add_label()

mwindow.add_button(text='运行', command=lambda: get_join(get_value, start_get_subject),
                   font_style=('楷体', 12))


menu = tk.Menu(mwindow.window, tearoff=0)
file_menu = menu.add_command(label='导出', command=lambda: export_txt(_cursor=_cursor))
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='编辑', menu=edit_menu)
edit_menu.add_command(label='添加/删除数据', command=lambda: insert_delete(connection=conn, _cursor=_cursor))
edit_menu.add_separator()
edit_menu.add_command(label='修改数据', command=lambda: modify_data(_cursor=_cursor))
edit_menu.add_separator()
edit_menu.add_command(label='查找数据', command=lambda: search_data(_cursor=_cursor))
edit_menu.add_separator()
edit_menu.add_command(label='输入语句', command=lambda: user_input_sql(_cursor=_cursor))
mwindow.window.config(menu=menu)

mwindow.main_loop()
