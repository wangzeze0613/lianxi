import pymysql
def chengfa(a,b):
    print(a*b)


def he(a,b,c):
    print(a+b+c)

def chaxun(sql):
    db=pymysql.connect(host="192.144.148.91",user="ljtest",password="123456",db="ljtestdb")
    cursor=db.cursor()
    cursor.execute(sql)
    res=cursor.fetchall()
    db.close()
    print(res)



chaxun("show tables;")