from sqlalchemy import create_engine, text
db_con_string="mysql+pymysql://azure_admin:Password123!@flexi-banenz.mysql.database.azure.com/games_banenz"

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
    db_con_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/var/www/html/DigiCertGlobalRootG2.crt.pem"
        }
    }
)



with engine.connect() as conn:
    result=conn.execute(text("select * from gameslist"))
    data1=result.all()[0] 

    #store data into a dictionary

result_dicts = []
for row in result.all():
    result_dicts.append(dict(row))

print(result_dicts) 

