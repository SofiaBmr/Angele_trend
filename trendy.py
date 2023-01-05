import pandas as pd 
import streamlit as st                       
from pytrends.request import TrendReq

st.title('Angèle trend')
st.markdown("**Sofia Boumahrat P2023**")
st.image("https://media.ngroup.be/IMAGE/IMAGE-S1-00024/236831-angele.jpg",caption="VIVRE LIBRE")
pytrend = TrendReq()
print(pytrend)

st.markdown("Let's see the Angèle's trend on Google over the years.")
pytrend.build_payload(["Angèle"])
# Interest by Region
df= pytrend.interest_over_time()
st.line_chart(data=df.Angèle)
st.markdown("Data :")
df.Angèle


