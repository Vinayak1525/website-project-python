from sqlalchemy import create_engine, text

db_con_string = "mysql+pymysql://azure_admin:Password123!@flexi-banenz.mysql.database.azure.com/games_banenz"

connection_string = (
    "DRIVER=MySQL ODBC 8.0 ANSI Driver;"
    "SERVER=flexi-banenz.mysql.database.azure.com;"
    "PORT=3307;"
    "DATABASE=games_banenz;"
    "UID=azure_admin;"
    "PWD=Password123!;"
    "charset=utf8mb4;"
)


# engine=create_engine("mysql+pymysql://azure_admin:Password123!@flexi-banenz.mysql.database.azure.com?charset=utf8mb4")


engine = create_engine(
    db_con_string,
    connect_args={"ssl": {"ssl_ca": "/var/www/html/DigiCertGlobalRootG2.crt.pem"}},
)


def load_gameslist_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from games_banenz.gameslist"))
    key_dicts = result.keys()
    Games_list = []
    for row in result.all():
        Games_list.append(dict(zip(key_dicts, row)))
    return Games_list


# with engine.connect() as conn:
#     result = conn.execute(text("select * from games_banenz.gameslist"))

# key_dicts = result.keys()

# result_dicts = []
# for row in result.all():
#     result_dicts.append(dict(zip(key_dicts, row)))
# print(result_dicts)
# print(type(result_all))
# for row in result_all:


#   print(dict(row))
# print(dict(row))

# result_dicts.append(dict(row))
# first_result_dicts = dict(str(result_all[]))
# print(result_dicts)
# print(result_all)
