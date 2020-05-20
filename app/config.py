db = {
    'user': 'admin',
    'password': 'q',
    'host': 'localhost',
    'port': '3306',
    'database': 'commute_book'
}
DB_URL = "mysql+mysqlconnector://" + db['user'] + ":" + db['password'] + "@" + db['host'] + ":" + db['port'] + "/" + db['database'] + "?charset=utf8"
