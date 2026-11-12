import streamlit as st
import pandas as pd
st.set_page_config(page_title="UTT Daily Dashboard | PETER", layout="wide")
st.title("UTT DAILY DASHBOARD | PETER | NR-17")
st.write("Project: K-47 - 8 inch OIL LINE | OFFSHORE NR-17 | Client: KJO")
data = [
    ["21-10-2026", 1, "PIPE", 11.1, 12.1, 11.5, 4, "OK"],
    ["21-10-2026", 2, "ELBOW", 10.6, 11.2, 11.0, 3, "OK"],
    ["21-10-2026", 3, "ELBOW", 11.1, 12.6, 12.2, 4, "OK"],
    ["21-10-2026", 4, "PIPE", 9.3, 9.8, 9.7, 5, "WATCH"],
    ["21-10-2026", 5, "PIPE", 9.3, 9.8, 9.6, 5, "WATCH"],
    ["21-10-2026", 6, "ELBOW", 10.8, 11.8, 11.1, 3, "OK"],
]
df = pd.DataFrame(data, columns=["Date","Point","Component","Minimum","Maximum","Average","Readings","Status"])
st.sidebar.title("Daily Filter")
dates = ["ALL"] + sorted(df["Date"].unique().tolist(), reverse=True)
sel = st.sidebar.selectbox("Date Select Pannu", dates)
fdf = df[df["Date"]==sel] if sel != "ALL" else df
total = len(fdf)
ok = len(fdf[fdf["Status"]=="OK"])
watch = len(fdf[fdf["Status"]=="WATCH"])
c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("TOTAL POINTS", total)
c2.metric("TOTAL READINGS", int(fdf["Readings"].sum()))
c3.metric("OK", ok)
c4.metric("WATCH", watch)
c5.metric("OK %", f"{ok/total*100:.1f}%" if total>0 else "0%")
st.subheader("Minimum Thickness - Daily")
st.bar_chart(fdf.set_index("Point")["Minimum"])
st.subheader(f"Daily Report - {sel}")
st.dataframe(fdf, use_container_width=True, hide_index=True)
st.subheader("Daily Summary")
for d in sorted(df["Date"].unique(), reverse=True):
    sub = df[df["Date"]==d]
    st.write(f"**{d}:** {len(sub)} Points | OK: {len(sub[sub['Status']=='OK'])} | WATCH: {len(sub[sub['Status']=='WATCH'])} | Min: {sub['Minimum'].min():.1f}mm")
st.caption("Daily Update System | PETER | QCS / KJO | NR-17")
