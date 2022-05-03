# Instruction of Automated script for joining Ten-cent online meeting

### <u>Features and Functions:</u>

##### Brief Description of the Script:

This script is used for auto joining Tencent meeting which you can select a name of the meeting created by yourself from the table and this application can help you directly join the meeting automatically.(**Tencent Meeting ONLY**)

##### Functions:

- Automation  of joining Tencent meeting.
- Users can CRUD(create, read, update, delete) the data they created in the table they created.
- Users may also input their own SQL lines to CRUD their tables or databases.



### <u>Requirements:</u>

- MySQL 5.5 or above
- Python 3.7 or above(above the version of 3.7 may cause some incompatibilities)

### <u>Preparations:</u>

- Install packages listed in **__init__.py**

- Configuring MySQL in **win_main.py**

- Prepare a table in the server for storing data, here is the format below:

- | Field | Type        | Null | Key  | Default | Extra |
  | ----- | ----------- | ---- | ---- | ------- | ----- |
  | class | char(255)   | NO   | PRI  |         |       |
  | code  | bigint(255) | NO   |      | NULL    |       |
  | pwd   | bigint(255) | YES  |      | NULL    |       |

  You can use command `create table tablename()` or even easier create graphically using softwares like [DataGrip](https://www.jetbrains.com.cn/datagrip/) or [Navicat](https://www.navicat.com.cn).

- After finish configuring the MySQL server and the data source(table), then you need to change the name in some source codes to your name of the table, here is an example of where you need to change:![image-20220502170329222](https://s1.ax1x.com/2022/05/02/OiGTuq.png)

After finishing these steps, you can now use the application now by running or packing **win_main.py**
