import pymysql
import pandas as pd

class DatabaseAccess():
    def __init__(self):
        self.__db_host = "192.168.2.14"
        self.__db_port = 3306
        self.__db_user = "root"
        self.__db_password = "3301"
        self.__db_database = "guangdong"

    def isConnectionOpen(self):
        self.__db = pymysql.connect(
            host = self.__db_host,
            port = self.__db_port,
            user = self.__db_user,
            password = self.__db_password,
            database = self.__db_database,
            charset = 'utf8'
        )

    # 执行数据库
    def linesinsert(self,post_sql,dic):
        try:
            self.isConnectionOpen()
            global cursor            # 创建游标
            cursor = self.__db.cursor()
            # get_sql = "SELECT * FROM GD511;"  # SQL语句
            # cur.execute(get_sql)  # 执行语句
            # self.post_sql = post_sql
            # self.dic = dic
            # post_sql = "INSERT INTO GD511(pashe,draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05) VALUES (%s,%s,%s,%s,%s,%s);"            # 执行语句
            # cursor.executemany(post_sql,dic)
            cursor.execute(post_sql,dic)
            print("MYSQL @linesinsert 命令执行成功!")

            # get_df = pd.DataFrame(cursor.fetchall())  # 获取结果转为dataframe
            # df = pd.DataFrame()
            # print(post_sql,df)
        except Exception as e:
            print("MYSQL @linesinsert 命令失败!：",e)
        finally:
            cursor.close()            # 关闭游标
            self.__db.commit()            # 提交
            self.__db.close()            # 关闭数据库连接

    # 查询数据库
    def database_check(self,check_sql):
        try:
            self.isConnectionOpen()
            global cursor            # 创建游标
            cursor = self.__db.cursor()
            cursor.execute(check_sql)
            read = cursor.fetchall()
            return read
        except Exception as e:
            print("MYSQL @database_check 执行失败：",e)
        finally:
            cursor.close()            # 关闭游标
            self.__db.commit()            # 提交
            self.__db.close()            # 关闭数据库连接


if __name__ == "__main__":
    DatabaseAccess()    # 创建实例化对象