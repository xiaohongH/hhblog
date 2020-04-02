import mysql.connector
conn = mysql.connector.connect(user='root',password='YES',database='test')
cursor = conn.cursor()
print ("connect mysql...")
# 创建表
#cursor.execute('create table test (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意mysql的占位符是%s
# cursor.execute('insert into test (id, name) values (%s, %s)',['1','huangong'])
print ('cursor.rowcount',cursor.rowcount)
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from test where id = %s',('1',))
values = cursor.fetchall()
print (values)
cursor.close()
conn.close()
