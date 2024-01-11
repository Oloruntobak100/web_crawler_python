import psycopg2
from prettytable import PrettyTable

hostname = 'localhost'
port_id = '5432'
database = 'mimic'
username = 'postgres'
password = 'pat2echo'
conn = None
cur = None

try:
  conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port_id)
  
  cur = conn.cursor()
  view_admissions = ''' SELECT row_id, subject_id,hadm_id,admission_type
    FROM mimiciii.admissions'''
  cur.execute(view_admissions)

    # Fetch the column names
  col_names = [desc[0] for desc in cur.description]

    # Create a PrettyTable instance
  table = PrettyTable(col_names)

    # Populate the table with data
  table.add_rows(cur.fetchall())

    # Print the table
  print(table)
  
  conn.commit()

except Exception as error:
  print(error)

finally:
    if cur is not None:
      cur.close()
    if conn is not None:
      conn.close()