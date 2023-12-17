import oracledb

def create_connection() :
    connection = oracledb.connect(user="kosa05", password="kosa2023oraclE", dsn="edudb_high",
                            config_dir="C:\Dev\Python\Wallet_edudb",
                            wallet_location="C:\Dev\Python\Wallet_edudb",
                            wallet_password="pythonoracle21")
    return connection

CURSOR = oracledb.CURSOR

if __name__ == "__main__" :
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM USERS")
    result = cursor.fetchall()
    
    for row in result :
        print(row)
    cursor.close()
    connection.close()
