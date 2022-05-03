from tkinter import ttk
import tkinter.messagebox as msgbox
import tkinter.filedialog as filedia
import tkinter as tk
import pymysql
import pyautogui
import os
import time
import csv
from Mwindow import *
from Topwindow import *
from modify import modify_data
from search import search_data
from insertdelete import insert_delete
from userinpsql import user_input_sql

save_filename = r''


# 启动函数
def join(join_code):
    # 开启软件并且点击操作
    os.startfile(r'X:\xxx\xxx\xxx\xxx.exe')
    time.sleep(7)
    pyautogui.leftClick(816, 318)
    time.sleep(1.6)
    pyautogui.typewrite(join_code)
    time.sleep(0.6)
    pyautogui.leftClick(948, 811)


def export_txt(_cursor):
    global save_filename
    save_result = sql_starter('select * from database.table', _cursor=_cursor)
    file_save = filedia.asksaveasfilename(initialfile='Untitled.csv', defaultextension='.csv')
    save_filename = file_save
    file_write = open(save_filename, 'w', newline='', encoding='gbk')
    csv_writer = csv.writer(file_write)
    for i in save_result:
        csv_writer.writerow([i[0], i[1], i[2]])


# 尝试进入会议
def get_join(get_value, get_subject):
    # get_value = mwindow.combobox.get()
    for i in get_subject:
        if get_value == i[0]:
            # 判断是否存在密码
            if i[2] is None:
                join(str(i[1]))
                # break
            else:
                join(str(i[1]))
                time.sleep(2.4)
                pyautogui.typewrite(str(i[2]))
                time.sleep(0.6)
                pyautogui.leftClick(1011, 598)
                # break
