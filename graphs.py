import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import mysql.connector
import sys
import datetime
import seaborn as sb

server = '127.0.0.1' 
database = 'car_acc' 
username = 'root' 
password = 'pass123456'

# conn = mysql.connector.connect(
#    user=username, password=password, host=server, database=database
# )
# cur =  conn.cursor()
# cur.execute("SELECT * FROM clean_acc")


# myresult = cur.fetchall()
# print(type(myresult))
# for x in range(10):
#   print(myresult[x])
def specific_time(dfUnTimed, time):
    dfUnTimed["Year"] =  pd.to_datetime(dfUnTimed["Year"], format='%Y')
    dfUnTimed["Full_Date"] = pd.to_datetime(dfUnTimed["Full_Date"])
    dfUnTimed["Date"] = pd.to_datetime(dfUnTimed["Date"])
    dfSorted = dfUnTimed.sort_values(by='Full_Date',ascending=True)
    dfSorted = dfSorted.set_index('Full_Date', drop=False)
    dfTimed = dfSorted.at_time(time)
    print("dfTimed")
    print(dfTimed)
def specific_calender(dfUnTimed,typeParam, val):
        #if year
    result = ""
    if typeParam == "Year":
        # dfUnTimed[dfUnTimed['Full_Date'] == begin_date_time_1]
        # dfUnTimed.loc[dfUnTimed['Date'].dt.weekday == 2]
        result = dfUnTimed.loc[dfUnTimed['Date'].dt.year == val]
    if typeParam == "Month":
        result = dfUnTimed.loc[dfUnTimed['Date'].dt.month == val]
    if typeParam == "Date":
        result = dfUnTimed.loc[dfUnTimed['Date'] == val]
    if typeParam == "Week_Day":
        result = dfUnTimed.loc[dfUnTimed['Date'].dt.weekday == val]
    print("Result")
    print(result)
        

    #if month
    # if date
    # if day
def date_time_range(dfUnTimed, begin_date_time_1, end_date_time_1):
    dfUnTimed["Year"] =  pd.to_datetime(dfUnTimed["Year"], format='%Y')
    dfUnTimed["Full_Date"] = pd.to_datetime(dfUnTimed["Full_Date"])
    dfUnTimed["Date"] = pd.to_datetime(dfUnTimed["Date"])
    dfBeginTime = pd.DataFrame({'Beg_t': [begin_date_time_1]})
    dfEndDay = pd.DataFrame({'End_d': ["2016-02-20 23:59:00"]})
    dfBegDay = pd.DataFrame({'Beg_d': ["2016-02-20 00:00:00"]})
    dfEndTime = pd.DataFrame({'End_t': [end_date_time_1]})
    begin_date_time= pd.to_datetime(dfBeginTime['Beg_t']) #pd.to_datetime([begin_date_time_1])[0]
    end_date_time= pd.to_datetime(dfEndTime['End_t'])
    begin_day= pd.to_datetime(dfBegDay['Beg_d']) #pd.to_datetime([begin_date_time_1])[0]
    end_day= pd.to_datetime(dfEndDay['End_d'])
    print("begin date time")
    print(begin_date_time)
    print("begin date ")
    print(begin_date_time.dt.date)
    print("begin  time")
    print(begin_date_time.dt.time)
    print("end date time")
    print(end_date_time)
    print("end date time by string maipulation")
    print((end_date_time_1[-8:]))

    dfSorted = dfUnTimed.sort_values(by='Full_Date',ascending=True)
    dfSorted = dfSorted.set_index('Full_Date', drop=False)
    end_date_less_one = end_date_time.dt.date - datetime.timedelta(days=1)
    begin_date_plus_one = begin_date_time.dt.date + datetime.timedelta(days=1)
    print("begin_date_plus_one")
    print(begin_date_plus_one)
    print("end_date_less_one")
    print(type(end_date_less_one[0]))
    print("str(begin_date_plus_one[0])")
    print(str(begin_date_plus_one[0]))
    print("str(end_date_less_one)")
    print(str(end_date_less_one))
    print("end_day")
    print(end_day)
    print("dfSorted[dfSorted['Full_Date'] == begin_date_time]")
    print(dfSorted[dfSorted['Full_Date'] == begin_date_time_1])
#     Data = pd.DataFrame({'Date Created': ["2016-02-20 09:26:45", "2016-02-19 19:30:25", "2016-02-19 18:13:39"]})
# Data['Date Created'] = pd.to_datetime(Data['Date Created'])
    # begin_time = dfSorted[dfSorted['Full_Date'] == begin_date_time_1].between_time("18:00", "23:59")
    # print("begin_time")
    # print(begin_time)
    begin_time = dfSorted[dfSorted['Full_Date'] == begin_date_time_1].between_time(begin_date_time_1[-8:], "23:59")
    print("begin_time_sliced")
    print(begin_time)
    # begin_time_dt_time = dfSorted[dfSorted['Full_Date'] == begin_date_time_1].between_time(begin_date_time.dt.time, end_day.dt.time)
    # print("begin_time_dt_time")
    # print(begin_time_dt_time)
    # end_time = dfSorted[dfSorted['Full_Date'] == begin_date_time].between_time("00:00:00" ,end_date_time_1[-8:])
    end_time = dfSorted[dfSorted['Full_Date'] == end_date_time_1].between_time( "00:00",end_date_time_1[-8:])
    
    # filtered_df_date = dfSorted.loc[(dfSorted['Full_Date'] >= '2005-01-01')
    #                  & (dfSorted['Full_Date'] < '2005-31-12 18:00:00')]
    print("begin_time")
    print(begin_time)
    print("end_time")
    print(end_time)
    filtered_df_by_date =dfSorted.loc[(dfSorted['Full_Date'] >= str(begin_date_plus_one[0]))
                     & (dfSorted['Full_Date'] <= str(end_date_less_one[0]))]
    print("filtered_df_by_date")
    print(filtered_df_by_date)
    frames = [begin_time, filtered_df_by_date, end_time]
    result = pd.concat(frames)
    print("result")
    print(result)
    # filtered_df_by_date2 =dfSorted.loc[(dfSorted['Full_Date'] >= begin_date_plus_one[0])
    #                  & (dfSorted['Full_Date'] <= end_date_less_one[0])]
    # frames2 = [begin_time, filtered_df_by_date2, end_time]
    # result2 = pd.concat(frames2)
    # print("result")
    # print(result2)
    return result

def date_range(dfUnTimed, begin_date, end_date):
    dfUnTimed["Year"] =  pd.to_datetime(dfUnTimed["Year"], format='%Y')
    dfUnTimed["Full_Date"] = pd.to_datetime(dfUnTimed["Full_Date"])
    dfUnTimed["Date"] = pd.to_datetime(dfUnTimed["Date"])
    dfBeginDate = pd.DataFrame({'Beg_d': [begin_date]})
    begin_date= pd.to_datetime(dfBeginDate['Beg_d']) #pd.to_datetime([begin_date_time_1])[0]
    dfEndDate = pd.DataFrame({'End_d': [end_date]})
    end_date= pd.to_datetime(dfEndDate['End_d'])
    print("begin date ")
    print(begin_date.dt.date)
    print("End date ")
    print(end_date.dt.date)
    dfSorted = dfUnTimed.sort_values(by='Full_Date',ascending=True)
    dfSorted = dfSorted.set_index('Full_Date', drop=False)
    filtered_df_by_date = dfSorted.loc[(dfSorted['Full_Date'] >= str(begin_date[0]))
                     & (dfSorted['Full_Date'] <= str(end_date[0]))]
    print("Filtered df by date")
    print(filtered_df_by_date)
    return filtered_df_by_date


    
def time_range(dfUnTimed, begin_time, end_time):
    dfUnTimed["Year"] =  pd.to_datetime(dfUnTimed["Year"], format='%Y')
    dfUnTimed["Full_Date"] = pd.to_datetime(dfUnTimed["Full_Date"])
    dfUnTimed["Date"] = pd.to_datetime(dfUnTimed["Date"])
    dfSorted = dfUnTimed.sort_values(by='Full_Date',ascending=True)
    dfSorted = dfSorted.set_index('Full_Date', drop=False)
    filtered_by_time = dfSorted['Full_Date'].between_time(begin_time, end_time)
    print("Filtered df by time")
    print(filtered_by_time)
    return filtered_by_time
def frequency_grouper(dfTimed, freq, measure):
    #Group depending on freq an dmeasure
    # Draw histogram for each category selected
    # dfUnTimed["Year"] =  pd.to_datetime(dfUnTimed["Year"], format='%Y')
    # dfUnTimed["Full_Date"] = pd.to_datetime(dfUnTimed["Full_Date"])
    # dfUnTimed["Date"] = pd.to_datetime(dfUnTimed["Date"])
    # print("Passed initialize")
    # full_date = 
    # dfSorted = dfUnTimed.sort_values(by='Full_Date',ascending=True)
    # dfSorted = dfSorted.set_index('Full_Date', drop=False)
    print("passed soritng")
    unique_elements  = dfTimed[measure].unique()
    print("List of uniques")
    print(unique_elements)
    # dfMonthGroupNOV = dfSorted.groupby(by=[pd.Grouper(key='Number_of_Vehicles', axis=0),pd.Grouper(key='Full_Date', axis=0, 
    #                   freq='M')]).sum()
    dfGrouped = dfTimed.groupby(by=[pd.Grouper(key=measure, axis=0),pd.Grouper(key='Full_Date', axis=0, 
                      freq=freq)]).sum()
    dfRenamed = dfGrouped.rename(columns={'Day_of_Week':'Number_of_Accidents'},inplace=False)
    print("Grpuped in frequency rouper")
    print(dfGrouped)
    print("Grpuped with specific measure :"+str(unique_elements[0]))
    print(dfGrouped.loc[[unique_elements[0]]])
    for i in unique_elements:
        dfGrouped.loc[[i]].plot(kind='hist', bins=12)
    plt.title('Distribution '+str(freq)+'ly')
    plt.xlabel("Accidents number")
    plt.show()

def plot_bar(dfTimed, measure):
    print("Inside plot bar")
    dfGrouped=  dfTimed.groupby([measure]).count()
    dfRenamed = dfGrouped.rename(columns={'Accident_Index':"Number_of_Accidents"},inplace=False)
    dfRenameIndex = dfRenamed.index
    print("Df Grouped index ")
    print(dfRenamed.index)
    print("Df Grouped Columns")
    print(dfRenamed.columns)
    print("Index Derived")
    print(list(dfRenameIndex))
    print("dfRenameINdex type")
    print(type(dfRenameIndex))
    dfRenamed["ind"] = list(dfRenameIndex)
    # print("Sampled")
    # print(dfRenamed[["Number_of_Accidents","Year"]].head(30))
    print(dfRenamed.info())
    ax = dfRenamed.plot(kind = "bar", x = "ind",y="Number_of_Accidents" )
    plt.show()
def plot_line(dfTimed, measure):
    print("Inside plot line")
    dfGrouped=  dfTimed.groupby([measure]).count()
    dfRenamed = dfGrouped.rename(columns={'Accident_Index':"Number_of_Accidents"},inplace=False)
    dfRenameIndex = dfRenamed.index
    print("Df Grouped index ")
    print(dfRenamed.index)
    print("Df Grouped Columns")
    print(dfRenamed.columns)
    print("Index Derived")
    print(list(dfRenameIndex))
    print("dfRenameINdex type")
    print(type(dfRenameIndex))
    dfRenamed["ind"] = list(dfRenameIndex)
    # print("Sampled")
    # print(dfRenamed[["Number_of_Accidents","Year"]].head(30))
    print(dfRenamed.info())
    ax = dfRenamed.plot(kind = "bar", x = "ind",y="Number_of_Accidents" )
    plt.show()
def plot_scatter(dfTimed,measure):
    print("Inside plot scatter")
    dfGrouped=  dfTimed.groupby([measure]).count()
    dfRenamed = dfGrouped.rename(columns={'Accident_Index':"Number_of_Accidents"},inplace=False)
    dfRenameIndex = dfRenamed.index
    print("Df Grouped index ")
    print(dfRenamed.index)
    print("Df Grouped Columns")
    print(dfRenamed.columns)
    print("Index Derived")
    print(list(dfRenameIndex))
    print("dfRenameINdex type")
    print(type(dfRenameIndex))
    dfRenamed["ind"] = list(dfRenameIndex)
    # print("Sampled")
    # print(dfRenamed[["Number_of_Accidents","Year"]].head(30))
    print(dfRenamed.info())
    ax = dfRenamed.plot(kind = "scatter", x = "ind",y="Number_of_Accidents" )
    plt.show()
def plot_correlation(dfTimed):
    dataplot = sb.heatmap(dfTimed.corr())
    plt.show()
    

def na_vs_nv(dfPat):
    print("Df ind")
    print(dfPat["ind"])
    print("Df Number_of_Accidents")
    print(dfPat["Number_of_Accidents"])
    # dfPat["ind2"] = int(dfPat["ind"])

    ax = dfPat.plot(kind = "scatter", x = "ind",y="Number_of_Accidents" )
    plt.show()
    # ax2 = df.plot.scatter(x='length',y='width', c='species', colormap='viridis')
    print("nav_vs_nv")

def sort_in_time(dfUnTimed):
    ##Year
    dfUnTimed["Year"] =  pd.to_datetime(dfUnTimed["Year"], format='%Y')
    dfUnTimed["Full_Date"] = pd.to_datetime(dfUnTimed["Full_Date"])
    dfUnTimed["Date"] = pd.to_datetime(dfUnTimed["Date"])

    
    dfSorted = dfUnTimed.sort_values(by='Full_Date',ascending=True)
    dfSorted = dfSorted.set_index('Full_Date', drop=False)
    print("-------------------------------------------------------------------------------------------------")
    # date_time_range(dfUnTimed, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    # date_range(dfUnTimed, "2009-01-01", "2009-05-01")
    time_range(dfUnTimed, "16:00", "23:00")
    print("-------------------------------------------------------------------------------------------------")
    
    print("Df SOrted and INdexed")
    print(dfSorted[["Year", "Full_Date"]])
    print(dfSorted.info())
    print("dfSorted Index")
    print(dfSorted.index)
    # value_to_check = pd.Timestamp(datetime.time.hour)
    # filter_mask_from_time = dfSorted['Full_Date'] < value_to_check
    # filtered_df_from_time = dfSorted[filter_mask_from_time]

    filtered_df_date = dfSorted.loc[(dfSorted['Full_Date'] >= '2005-09-01')
                     & (dfSorted['Full_Date'] < '2008-09-15')]
    dfSorted['Day_of_Week']= dfSorted['Full_Date'].dt.weekday
    print("filtered_df_date")
    print(filtered_df_date[["Year", "Full_Date"]])
    print(filtered_df_date.info())
    

    
    filtered_df_day = dfSorted.loc[dfSorted['Full_Date'].dt.weekday == 2]
    print("filtered_df_day")
    print(filtered_df_day[["Year", "Full_Date","Day_of_Week"]])
    print(filtered_df_day.info())
    filtered_df_day2 = dfSorted.loc[dfSorted['Day_of_Week'] == 2]
    print("filtered_df_day_sorted by Day_of_Week")
    print(filtered_df_day2[["Year", "Full_Date","Day_of_Week"]])
    print(filtered_df_day2.info())
   
    
    s = pd.to_datetime('08:00:00', format='%H:%M:%S')
    e = pd.to_datetime('20:00:00', format='%H:%M:%S')


    # df[(df.index.hour >= 18) | (df.index.hour <= 5)]
    # filtered_df_time = dfSorted.loc[(dfSorted['Full_Date'].dt.time >= s)
    #                 & (dfSorted.Full_Date.dt.time <e) ]
    # filtered_df_time2 = dfSorted[(dfSorted["Full_Date"].dt.time >= 18) | (dfSorted.Full_Date.dt.time <= 5)]

    ##Plot Time Ranges
    filtered_df_time2  = dfSorted.between_time('18:00', '5:00')
    print("filtered_df_time2")
    print(filtered_df_time2[["Year", "Full_Date"]])
    print(filtered_df_time2.info())

    ### DAte
    
    # print("filtered_df_from_time")
    # print(filtered_df_from_time[["Year", "Full_Date"]])
    # print(filtered_df_from_time.info())


    dfDateIn = dfSorted.reset_index(drop=True)
    dfDateIn = dfDateIn.set_index('Date', drop=False)
    print(" dfDateIn INDEXXXX")
    print(dfDateIn.index)
    # dfRD  = dfSorted.asfreq('D')
    # print(" dfRD Datadata")
    # print(dfRD[["Year", "Full_Date","Day_of_Week"]])
    filtered_df_day3 = dfDateIn.loc[dfDateIn['Date'].dt.weekday == 2]
    print("filtered_df_day_sorted by Day_of_Week")
    print(filtered_df_day3[["Year", "Full_Date","Day_of_Week"]])
    print(filtered_df_day3.info())

    dfMonthGroup = dfSorted.groupby(pd.Grouper(key='Full_Date', axis=0, 
                      freq='M')).sum()
    
    print("dfMonthGroup by Monthk")
    print(dfMonthGroup)
    print(dfMonthGroup.info())
    dfMonthGroupNOV = dfSorted.groupby(by=[pd.Grouper(key='Number_of_Vehicles', axis=0),pd.Grouper(key='Full_Date', axis=0, 
                      freq='M')]).sum()
    dfMonthGroupNOV2 = dfSorted.groupby(by=[pd.Grouper(key='Weather_Conditions', axis=0),pd.Grouper(key='Full_Date', axis=0, 
                      freq='M')]).sum()
    # dfMonthGroupNOV["Month"] = dfMonthGroupNOV["Full_Date"].dt.month
    print("dfMonthGroupNOV by Monthk")

    print(dfMonthGroupNOV)
    print(dfMonthGroupNOV.info())
    print("dfMonthGroupNOV Weather COditions by Monthk")

    print(dfMonthGroupNOV2)
    print(dfMonthGroupNOV2.info())
    # print("dfMonthGroupNOV by Monthk")
    # print(type(dfMonthGroupNOV.index[0][1]))
    # print(dfMonthGroupNOV.index)
    date_month_list =[i[1].month for i in dfMonthGroupNOV.index] 
    number_of_vehicles_list =[i[0] for i in dfMonthGroupNOV.index] 
    sum_list = list(dfMonthGroupNOV["Day_of_Week"])
    dfMonI = pd.DataFrame({"nov":number_of_vehicles_list, "datemonth":date_month_list, "sumlist":sum_list})
    dfMonI = dfMonI.set_index(['nov', 'datemonth'])
    dfMonIGr = dfMonI.groupby(level=[0,1]).sum()
    # dfMonthGroupNOV["Month"] = date_time_list
    print("dfMonI")
    print(dfMonI)
    print("dfMonI index")
    print(dfMonI.index)
    print("dfMonI info")
    print(dfMonI.info())
    print("dfMonIGr")
    print(dfMonIGr)
    print("dfMonIGr index")
    print(dfMonIGr.index)
    print("dfMonIGr info")
    print(dfMonIGr.info())

    # ax = dfMonthGroupNOV.head(36).plot(kind="bar")
    ax2 = dfMonIGr.unstack().plot(kind="bar", align='center', width=2)
    plt.tick_params(rotation=45)
    plt.show()
    return filtered_df_date
    
    
    






try:
    dbcon =  pymysql.connect(host=server, user=username, password=password,database= database)
    get_all_query = "SELECT * FROM clean_acc"
    sql_query =  pd.read_sql_query(get_all_query, dbcon)
    dfCleanAcc = pd.DataFrame(sql_query)

    print(dfCleanAcc.head())
    print(dfCleanAcc.info())
    dbcon.close()
    # filtered_df_date_ex = sort_in_time(dfCleanAcc)

    # dfGrouped=  dfCleanAcc.groupby(["Number_of_Vehicles"]).count()
    # dfRenamed = dfGrouped.rename(columns={'Accident_Index':'Number_of_Accidents'},inplace=False)
    # dfRenameIndex = dfRenamed.index
    # print("Df Grouped index ")
    # print(dfRenamed.index)
    # print("Df Grouped Columns")
    # print(dfRenamed.columns)
    # print("Index Derived")
    # print(list(dfRenameIndex))
    # print("dfRenameINdex type")
    # print(type(dfRenameIndex))
    # dfRenamed["ind"] = list(dfRenameIndex)
    # print("Sampled")
    # print(dfRenamed[["Number_of_Accidents","Year"]].head(30))
    # print(dfRenamed.info())
    # na_vs_nv(dfRenamed)
    # na_vs_nv(dfRenamed)
    req_date_timed = date_time_range(dfCleanAcc, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    print("Df req_date_timed Columns")
    print(req_date_timed.columns)

    # plot_bar(req_date_timed[['Number_of_Vehicles','Accident_Index']],"Number_of_Vehicles")
    print("--------------------------------------------Specific Time 1511----------------------------------------------------")
    # date_time_range(dfUnTimed, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    # date_range(dfUnTimed, "2009-01-01", "2009-05-01")
 
    # frequency_grouper(req_date_timed, 'M', 'Number_of_Vehicles')
    specific_time(dfCleanAcc, "15:11")
    print("-------------------------------------------------------------------------------------------------")
    print("--------------------------------------Specific Calender Year 2009-----------------------------------------------------------")
    # date_time_range(dfUnTimed, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    # date_range(dfUnTimed, "2009-01-01", "2009-05-01")
    # frequency_grouper(req_date_timed, 'M', 'Weather_Conditions')
    specific_calender(dfCleanAcc,"Year", '2009')
    print("-------------------------------------------------------------------------------------------------")
    print("--------------------------------------Specific Calender MOnth 1-----------------------------------------------------------")
    # date_time_range(dfUnTimed, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    # date_range(dfUnTimed, "2009-01-01", "2009-05-01")
    # frequency_grouper(req_date_timed, 'M', 'Weather_Conditions')
    specific_calender(dfCleanAcc,"Month", 1)
    print("-------------------------------------------------------------------------------------------------")
    print("--------------------------------------Specific Calender Date 2009-01-01 -----------------------------------------------------------")
    # date_time_range(dfUnTimed, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    # date_range(dfUnTimed, "2009-01-01", "2009-05-01")
    # frequency_grouper(req_date_timed, 'M', 'Weather_Conditions')
    specific_calender(dfCleanAcc,"Date", "2009-01-01")
    print("-------------------------------------------------------------------------------------------------")
    print("--------------------------------------Specific Calender Week Day 4-----------------------------------------------------------")
    # date_time_range(dfUnTimed, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    # date_range(dfUnTimed, "2009-01-01", "2009-05-01")
    # frequency_grouper(req_date_timed, 'M', 'Weather_Conditions')
    specific_calender(dfCleanAcc,"Week_Day", 4)
    print("-------------------------------------------------------------------------------------------------")
    print("--------------------------------------Correlation-----------------------------------------------------------")
    # date_time_range(dfUnTimed, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    # date_range(dfUnTimed, "2009-01-01", "2009-05-01")
    # frequency_grouper(req_date_timed, 'M', 'Weather_Conditions')
    plot_correlation(req_date_timed)
    plot_correlation(dfCleanAcc)
    print("-------------------------------------------------------------------------------------------------")
except:
    print("Error: unable to convert the data")
    print(sys.exc_info())



### NUmber of accidents vs no of venhicles
def time_sort(dfUnTimed):
    ##Plot Time Ranges
    dfSorted = dfUnTimed.sort_values(by='Full_Date',ascending=True)
    dfSorted = dfSorted.set_index('Full_Date', drop=False)
    filtered_df_time2  = dfSorted.between_time('18:00', '5:00')



def freq_time(dfUntimed):
    pass

def plot_freq(timedData):
    pass
def plot_range(timedData):
    pass