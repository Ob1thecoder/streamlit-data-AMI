import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
# ______________________________________________________________________________________________________
#Define functions
def overview(title, data):
    st.write(title)
    st.dataframe(data, hide_index=True)
    st.write('Data types')
    st.write(data.dtypes)
    st.write('Tong quan so lieu')
    st.write(merged.describe())
    pass




# ______________________________________________________________________________________________________
# Overview
st.title('DU lIEU TONG HOP TU NGAY 15/12 - 24/12')
st.divider()
st.caption('Chuyen doi du lieu tu file excel sang file CSV')

body = ('''data_xls = pd.read_excel('GA4_tổng hơp dữ liệu từ 15-24 tháng 12.xlsx', sheet_name='15')
data_xls.to_csv('CSVSource/DF_151223.csv', index=False) 
for i in range(15,25):
    data_xls = pd.read_excel('GA4_tổng hơp dữ liệu từ 15-24 tháng 12.xlsx', sheet_name='%2d' %i)
    data_xls.to_csv('CSVSource/DF_%2d1223.csv'%i)''')
st.code(body, language="python", line_numbers=True)
# Difference between each day
st.markdown("<h2>Bien doi tu ngay 15/12-24/12</h2>", unsafe_allow_html=True)
#__________________________CSV reader________________________________________________
df15 = pd.read_csv('CSVsource/DF_151223.csv', sep=',', index_col=0)
df16 = pd.read_csv('CSVsource/DF_161223.csv', sep=',', index_col=0)
df17 = pd.read_csv('CSVsource/DF_171223.csv', sep=',', index_col=0)
df18 = pd.read_csv('CSVsource/DF_181223.csv', sep=',', index_col=0)
df19 = pd.read_csv('CSVsource/DF_191223.csv', sep=',', index_col=0)
df20 = pd.read_csv('CSVsource/DF_201223.csv', sep=',', index_col=0)
df21 = pd.read_csv('CSVsource/DF_211223.csv', sep=',', index_col=0)
df22 = pd.read_csv('CSVsource/DF_221223.csv', sep=',', index_col=0)
df23 = pd.read_csv('CSVsource/DF_231223.csv', sep=',', index_col=0)
df24 = pd.read_csv('CSVsource/DF_241223.csv', sep=',', index_col=0)
# ____________________________________________________________________________________
df15['Date'] = '15/12/23'
df16['Date'] = '16/12/23'
df17['Date'] = '17/12/23'
df18['Date'] = '18/12/23'
df19['Date'] = '19/12/23'
df20['Date'] = '20/12/23'
df21['Date'] = '21/12/23'
df22['Date'] = '22/12/23'
df23['Date'] = '23/12/23'
df24['Date'] = '24/12/23'
# ____________________________________________________________________________________

data_frames = [df15, df16, df17,df18,df19,df20,df21,df22,df23,df24]

# Merging all dataframes
st.subheader('Initial data analysis (IDA)')
merged = pd.concat(data_frames)
with st.expander('Overview'):
    overview('DataFrame tong hop 15/12-24/12',merged)
tab1 ,tab2, tab3= st.tabs(['device_category vs Total raw','platform vs Total Raw','View'])
with tab1:
    mini1, mini2, mini3 = st.tabs(['Desktops and Tablets', 'Mobile','SmartTV'])
    # Device individual analysis
    de = merged.groupby('device_category').get_group('desktop')
    dr = merged.groupby('device_category').get_group('mobile')
    dt = merged.groupby('device_category').get_group('tablet')
    dy = merged.groupby('device_category').get_group('smart tv')
    with mini1:
        fig =plt.figure(figsize=(10, 9), dpi=200)
        plt.plot(de['Date'], de['Total Raw'], label='Desktop')
        # plt.plot(dr['Date'].drop_duplicates(keep='first'),dr.groupby('Date')['Total Raw'].sum(),label='Mobile')
        plt.plot(dt['Date'].drop_duplicates(keep='first'), dt.groupby('Date')['Total Raw'].sum(), label='Tablet')
        # plt.plot(dy['Date'].drop_duplicates(keep='first'),dy.groupby('Date')['Total Raw'].sum(),label='Smart TV')
        plt.legend(loc='upper right')
        plt.xlabel('Ngay')
        plt.ylabel('Luot Su dung')
        st.pyplot(fig)
    with mini2:
        fig =plt.figure(figsize=(10, 9), dpi=200)
        plt.plot(dr['Date'].drop_duplicates(keep='first'),dr.groupby('Date')['Total Raw'].sum(),label='Mobile')
        plt.xlabel('Ngay')
        plt.ylabel('Luot Su dung (Trieu luot)')
        st.pyplot(fig)
    with mini3:
        fig = plt.figure(figsize=(10, 9), dpi=200)
        plt.plot(dy['Date'].drop_duplicates(keep='first'),dy.groupby('Date')['Total Raw'].sum(),label='Smart TV')
        plt.xlabel('Ngay')
        plt.ylabel('Luot Su dung')
        st.pyplot(fig)
with tab2:
    ios = merged.groupby('platform').get_group('IOS')
    andr = merged.groupby('platform').get_group('ANDROID')
    web = merged.groupby('platform').get_group('WEB')
    fig1 = plt.figure(figsize=(10, 6))
    plt.plot(ios['Date'].drop_duplicates(keep='first'), ios.groupby('Date')['Total Raw'].sum(), label='IOS')
    plt.plot(andr['Date'].drop_duplicates(keep='first'), andr.groupby('Date')['Total Raw'].sum(), label='ANDROID')
    plt.plot(web['Date'].drop_duplicates(keep='first'), web.groupby('Date')['Total Raw'].sum(), label='WEB')
    plt.legend(loc='upper right')
    plt.xlabel("Ngay")
    plt.ylabel("Luot dung (Trieu luot)")
    plt.title("So platform truy cap vao cac kenh truyen hinh")
    st.pyplot(fig1)
# __________________________________________________________________________________________________

# Thong tin tung ngay
st.markdown("<h2>Thong tin tung ngay</h2>", unsafe_allow_html=True)
st.markdown('<h3>Du lieu trong ngay 15/12/2023</h3>', unsafe_allow_html=True)
st.divider()
st.markdown('<h5>Initial Data Analysis (IDA)</h5>', unsafe_allow_html=True)
with st.expander('Overview'):
    st.dataframe(df15,hide_index=True)
    st.write("Data types")
    st.write(df15.dtypes)
    st.write("Tong quan thong tin")
    st.write(df15.describe())

#First analysis__________________________________________________________________________________________________-
a=df15[['device_category','Total Raw']].head(7)
s=a.groupby('device_category')[['Total Raw']].sum()
st.markdown('<h3>Thiet bi truy cap tren mau khao sat (Total Raw vs device_category)</h3>', unsafe_allow_html=True)
tab1 ,tab2= st.tabs(['Pie chart','Bar graph'])
with tab1:
    fig = plt.figure(figsize=(4,4), dpi=50)
    plt.pie(s['Total Raw'],startangle=90)
    plt.legend(s.index,loc='upper right')
    st.pyplot(fig=fig)
with tab2:
    fig1=plt.figure()
    plt.bar(s.index,s['Total Raw'])
    plt.ylabel("Nguoi xem (Trieu nguoi)")
    plt.xlabel("Thiet bi")
    st.pyplot(fig=fig1)

#Second analysis___________________________________________________________________________________________________
a=df15[['platform','Total Raw']].head(7).groupby('platform')[['Total Raw']].sum()
st.markdown('<h3>Platform truy cap tren mau khao sat (Total Raw vs platform)</h3>', unsafe_allow_html=True)
tab1 ,tab2= st.tabs(['Pie chart','Bar graph'])
with tab1:
    fig = plt.figure(figsize=(4,4), dpi=50)
    plt.pie(a['Total Raw'],startangle=90)
    plt.legend(s.index,loc='upper right')
    st.pyplot(fig=fig)
with tab2:
    fig1=plt.figure()
    plt.bar(a.index,a['Total Raw'])
    plt.ylabel("Nguoi xem (Trieu nguoi)")
    plt.xlabel("platform")
    st.pyplot(fig=fig1)
#Third analysis_______________________________________________________________________________________________________
#              ________Data__________


b=df15[['device_category','Live Channel','Livestream','Timeshift Channel','Video on Demand']].head(7)
st.markdown('<h3>Luot xem cac loai kenh truyen hinh  tren cac thiet bi</h3>', unsafe_allow_html=True)
bp=b[['device_category','Live Channel']].groupby('device_category').sum()
bv=b[['device_category','Livestream']].groupby('device_category').sum()
bt=b[['device_category','Video on Demand']].groupby('device_category').sum()
bl= b[['device_category','Timeshift Channel']].groupby('device_category').sum()
tab1,tab2 = st.tabs(['Bar graph','Box'])

with tab1:
    x = np.arange(len(bp.index))
    width = 0.2
    fig = plt.figure()
    plt.bar(x - width, bp['Live Channel'], width, label='Live Channel', color='blue')
    plt.bar(x, bv['Livestream'], width, label='Livestream', color='red')
    plt.bar(x+width,bl['Timeshift Channel'], width, label='Timeshift Channel')
    plt.bar(x+2*width,bt['Video on Demand'], width, label='Video on Demand')
    plt.xticks(x, bp.index)
    plt.legend(loc='upper right')
    plt.show()
    st.pyplot(fig)

