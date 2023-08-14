from sqlalchemy import create_engine, text
#db_con_string="mysql+pymysql://Password123!:azure_admin@banenz.mysql.database.azure.com:3306/gameslist"

connection_string = (
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=flexi-banenz.mysql.database.azure.com;'
    'PORT=3307;'
    'DATABASE=games_banenz;'
    'UID=azure_admin;'
    'PWD=Password123!;'
    'charset=utf8mb4;'
)


#engine=create_engine("mysql+pymysql://azure_admin:Password123!@flexi-banenz.mysql.database.azure.com?charset=utf8mb4")



engine = create_engine(
    "mysql+pymysql://azure_admin:Password123!@flexi-banenz.mysql.database.azure.com/games_banenz",
    connect_args={
        "ssl": {
            "ssl_ca": "/var/www/html/DigiCertGlobalRootG2.crt.pem"
        }
    }
)



with engine.connect() as conn:
    result=conn.execute(text("select * from gameslist"))
    print(result.all())