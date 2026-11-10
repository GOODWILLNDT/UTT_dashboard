import streamlit as st
import pandas as pd
st.title("UTT DASHBOARD - PETER - P2583")
data = {
"S.No": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
"S": [9.6,8.4,12.4,8.6,7.6,8.4,6.4,5.9,8.9,None,10.6,None,None,None,None],
"N": [9.2,9.1,12.6,8.4,7.4,8.1,6.8,6.1,8.7,None,10.2,None,None,None,None],
"E": [9.8,None,None,8.3,None,8.2,6.9,6.3,8.2,9.6,10.3,7.6,7.4,7.6,9.4],
"W": [9.9,None,None,8.7,None,8.1,6.7,6.4,8.8,9.8,10.1,7.4,7.6,7.4,9.2],
"T": [None,9.0,12.1,None,None,None,None,None,None,10.1,None,7.6,7.3,7.8,9.6],
"B": [None,8.9,12.3,None,None,None,None,None,None,10.0,None,7.8,8.0,7.9,10.0],
"N.T": [10,10,13,9,9,9,8,7,9,11,11,8,8,8,10]
}
df = pd.DataFrame(data)
df["MIN"] = df[["S","N","E","W","T","B"]].min(axis=1)
df["LOSS%"] = (df["N.T"]-df["MIN"])/df["N.T"]*100
df["STATUS"] = df["LOSS%"].apply(lambda x: "OK" if x<12 else ("WATCH" if x<15 else "CHECK!"))
st.dataframe(df)
st.bar_chart(df.set_index("S.No")["LOSS%"])
st.write("CHECK Points:", df[df["STATUS"]=="CHECK!"]["S.No"].tolist())
st.success("S.No 7 - 20% Loss - Danger!")