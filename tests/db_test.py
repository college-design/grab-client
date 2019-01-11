
import grab.db.db_mysql as db_mysql

if __name__ == '__main__':
    # list = db_mysql.execute_sql_by_params('select * from web_site where status=1 ',[])
    # count = db_mysql.execute_sql_count_by_params('select * from web_site where status=1',[])
    # print(list)
    # print(count)
    # db_mysql.modify_sql_by_params("insert into match_data(data,grab_rule_id) value (%s,%s)",('ttt',11))
    # db_mysql.modify_sql_by_params("delete from match_data where 1=1",())
    db_mysql.modify_sql_by_params(r"update grap_rule set status=0 where id=%s",[1])
    print(db_mysql.execute_sql_count_by_params('select * from match_data ',[]))