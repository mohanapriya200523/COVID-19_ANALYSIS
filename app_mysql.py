import mysql.connector
import pandas as pd
df = pd.read_csv("covid19.csv")   # make sure file exists


conn = mysql.connector.connect(
    host="####",
    user="####",
    password="####",
    database="covid_analysis"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO covid_data VALUES (%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
print("Data inserted successfully")
