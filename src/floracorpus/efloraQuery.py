from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import urllib.parse
params = urllib.parse.quote("Driver={ODBC Driver 13 for SQL Server};Server=tcp:flparser.database.windows.net,1433;Database=flparserefloras;Uid=ggosline@flparser;Pwd=Uvariodendr0n;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

db = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# db = create_engine(r'sqlite:///..\resources\efloras.db3')
Session = sessionmaker(bind=db)
session = Session()
db.echo = False  # Try changing this to True and see what happens
metadata = MetaData()
taxa = Table('alltaxa', metadata, autoload=True, autoload_with=db)
names = Table('acceptednames', metadata, autoload=True, autoload_with=db)

def run(stmt):
    rs = db.execute(stmt)
    return [dict(zip(row.keys(), row)) for row in rs]

def readEflora(searchargs):
    nnargs = {k:v for k,v in searchargs.items() if v}
    q = session.query(taxa).filter_by(**nnargs).all()
    return [dict(zip(row.keys(), row)) for row in q]

def readNames(fieldname, searchargs):
    nnargs = {k: v for k, v in searchargs.items() if v}
    q = session.query(names, fieldname).filter(names.c.rank==fieldname).filter_by(**nnargs)
    return sorted([row[-1] for row in q])

if __name__ == '__main__':
    #conn = db.connect()
    #Perform query and return JSON data
    #query = conn.execute("select flora_code from Floradetails order by flora_code")
    #print ({'floras': [i for i in query.cursor.fetchall()]})
    print(readNames("genus", {"flora_name":"FZ", "family":"Rutaceae"}))