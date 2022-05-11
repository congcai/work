import pymysql
#连接数据库 登录 指定数据库
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='mydb')
#创建游标
cursor=conn.cursor()
#创建游标   显示字段名称
cursor1=conn.cursor(pymysql.cursors.DictCursor)
#执行sql 返回受影响数行
effect_row=cursor.excute("update hosts set host='1.1.1.2'")
effect_row1=cursor.execute("select * from sef")

#打印条数
print(effect_row1)
#打印所有数据
print(cursor.fetchall())

#游标移动
cursor.scroll(3,mode='relative')    #相对位置移动3行
cursor.scroll(3,mode='absolute')    #相对位置移动3行

#提交
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()