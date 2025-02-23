import streamlit as st 
from datetime import datetime
from  contract import Sales
from pydantic import ValidationError
from database import save_in_pg

def main():
    st.title("CRM system and Sales")
    email = st.text_input("Insert salesperson e-mail:")
    date = st.date_input("Insert sales date", datetime.now())
    hour = st.time_input("Insert sales time")
    price = st.number_input("Insert sales value", min_value = 0.0, format="%.2f")
    quantity = st.number_input("Insert  product quantity", min_value=1, step=1)
    product = st.selectbox("Select product", ["Luminae - Gemini","Luminae - chatGPT", "Luminae - Llama3"])
    
    if st.button("Save"):
        try: 
            date_hour = datetime.combine(date,hour)
        
            sale = Sales(
                email = email,
                date_hour = date_hour, 
                price = price,
                quantity  = quantity, 
                product = product 
            )
            save_in_pg(sale)
        except ValidationError as e:
            st.error(f"Error {e}")
if __name__ == "__main__":
    main()