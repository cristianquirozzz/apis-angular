import pymysql
#MYSQL
def obtener_conexion():
    return pymysql.connect(host='yid2s6.stackhero-network.com',
                                port=3306,
                                user='root',
                                password='LUXsS81YnVWckEmCFu40RPRlS4lDXtjM',
                                db='contactos',
                                 ssl={'ca': '/isrgrootx1.pem'})
#MariaDB
"""def obtener_conexion():
    return pymysql.connect(host='uu2jl1.stackhero-network.com',
                                port=3306,
                                user='root',
                                password='uJO2Jowjbbie7NTYOYLX13a4kEupmXhz',
                                db='contactos',
                                 ssl={'ca': '/isrgrootx1.pem'})"""