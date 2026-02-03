#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# API Headers (keep if used)
HEADERS = {
	"x-rapidapi-key": "ab233b97admshfd174790c367d6dp11ad4ejsn769273b5232f",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}



def get_connection():

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2806",
            database="cricbuzz",
            port=3306
        )

        if conn.is_connected():
            print("✅ MySQL Connected")
            return conn

    except Exception as e:
        print("❌ Database Connection Failed:", e)
        return None

get_connection()


# In[ ]:




