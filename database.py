import psycopg2 
from psycopg2 import sql 
from contract import Sales 
import streamlit as st 
from dotenv import load_dotenv
import os 

load_dotenv()

DB_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
DB_DATABASE = os.getenv("PG_DATABASE")
DB_USER = os.getenv("PG_USER")
DB_PASSWORD = os.getenv("PG_PASSWORD")
DB_SCHEMA = os.getenv("PG_SCHEMA")

def save_in_pg(data: Sales):
    """Function to save data into Postgres"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database = DB_DATABASE,
            user = DB_USER,
            password = DB_PASSWORD,
        )
        cursor = conn.cursor()
        insert_query = sql.SQL(
            "INSERT INTO dw_lcs.sales (email, created_at, value, quantity, product) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            data.email,
            data.date_hour,
            data.price,
            data.quantity,
            data.product
            ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Order saved succesfuly!")
    except Exception as e:
        st.error(f"Error saving order: {e}")
