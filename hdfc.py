import streamlit as st
import pandas as pd
from supabase import create_client
#supabase configuration
SUPABASE_URL="https://rloiriiblntbnjprgmvw.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJsb2lyaWlibG50Ym5qcHJnbXZ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDA4MTIsImV4cCI6MjA4MTYxNjgxMn0.90YL2FQrZsE8NEAItCkE-vFzdZHCRX-F5hsjAWgeFWk"

supabase=create_client(SUPABASE_URL,SUPABASE_KEY)
#STREAMLIT UI
st.title("HDFC BANK (supabase)")
menu=["REGISTER","VIEW"]
choice=st.sidebar.selectbox("Menu",menu)
#register
if choice=="REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("AGE",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE",min_value=500)
    if st.button("Save"):
        supabase.table("users2").insert({
            "name":name,
            "age":age,
            "account":account,
            "balance":bal}).execute()
        st.success("user added successfully")
#view
if choice=="VIEW":
    st.subheader("view users")
    data=supabase.table("users2").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)

    
