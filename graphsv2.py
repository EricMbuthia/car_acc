import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import sys
import datetime
import seaborn as sb
server = '127.0.0.1' 
database = 'car_acc' 
username = 'root' 
password = 'pass123456'




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

    result = ""
    if typeParam == "Year":

        result = dfUnTimed.loc[dfUnTimed['Date'].dt.year == val]
    if typeParam == "Month":
        result = dfUnTimed.loc[dfUnTimed['Date'].dt.month == val]
    if typeParam == "Date":
        result = dfUnTimed.loc[dfUnTimed['Date'] == val]
    if typeParam == "Week_Day":
        result = dfUnTimed.loc[dfUnTimed['Date'].dt.weekday == val]
    print("Result")
    print(result)
        


def date_time_range(dfUnTimed, begin_date_time_1, end_date_time_1):
    dfUnTimed["Year"] =  pd.to_datetime(dfUnTimed["Year"], format='%Y')
    dfUnTimed["Full_Date"] = pd.to_datetime(dfUnTimed["Full_Date"])
    dfUnTimed["Date"] = pd.to_datetime(dfUnTimed["Date"])
    dfBeginTime = pd.DataFrame({'Beg_t': [begin_date_time_1]})
    dfEndDay = pd.DataFrame({'End_d': ["2016-02-20 23:59:00"]})
    dfBegDay = pd.DataFrame({'Beg_d': ["2016-02-20 00:00:00"]})
    dfEndTime = pd.DataFrame({'End_t': [end_date_time_1]})
    begin_date_time= pd.to_datetime(dfBeginTime['Beg_t']) 
    end_date_time= pd.to_datetime(dfEndTime['End_t'])
    begin_day= pd.to_datetime(dfBegDay['Beg_d']) 
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
    begin_time = dfSorted[dfSorted['Full_Date'] == begin_date_time_1].between_time(begin_date_time_1[-8:], "23:59")
    print("begin_time_sliced")
    print(begin_time)
    end_time = dfSorted[dfSorted['Full_Date'] == end_date_time_1].between_time( "00:00",end_date_time_1[-8:])
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
    print("passed soritng")
    unique_elements  = dfTimed[measure].unique()
    print("List of uniques")
    print(unique_elements)
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
    print(dfRenamed.info())
    ax = dfRenamed.plot(kind = "scatter", x = "ind",y="Number_of_Accidents" )
    plt.show()
def plot_correlation(dfTimed):
    dataplot = sb.heatmap(dfTimed.corr())
    plt.show()




try:
    # dbcon =  pymysql.connect(host=server, user=username, password=password,database= database)
    # get_all_query = "SELECT * FROM clean_acc"
    # sql_query =  pd.read_sql_query(get_all_query, dbcon)
    # dfCleanAcc = pd.DataFrame(sql_query)

    # print(dfCleanAcc.head())
    # print(dfCleanAcc.info())
    # dbcon.close()
    dfCleanAcc= pd.read_csv("car_5000.csv")
    req_date_timed = date_time_range(dfCleanAcc, "2009-01-01 15:11:00", "2009-05-01 10:59:00")
    print("Df req_date_timed Columns")
    print(req_date_timed.columns)


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
