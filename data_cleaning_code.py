# //get the latest version of pandas_profiling
import pandas_profiling 
import numpy as np
import pandas as pd
import random

accDf=pd.read_csv("copy_accidents.csv")

profile = accDf.profile_report(title="Accidents")
profile.to_file(output_file="report_before_clean13th.html")
unwanted_cols = ['Junction_Detail', 'LSOA_of_Accident_Location']
accDf.drop(columns = unwanted_cols, inplace=True)

# print(accDf.info())
##Handle Location Missing values by drop Na
print("Before Location Drop")
print(accDf['Longitude'].isna().sum())
print(accDf['Latitude'].isna().sum())
print(accDf['Location_Northing_OSGR'].isna().sum())
print(accDf['Location_Easting_OSGR'].isna().sum())
accDf.dropna(axis=0,subset=['Longitude', 'Latitude','Location_Northing_OSGR','Location_Easting_OSGR'], inplace = True)
print("After Location Drop")
print(accDf['Longitude'].isna().sum())
print(accDf['Latitude'].isna().sum())
print(accDf['Location_Northing_OSGR'].isna().sum())
print(accDf['Location_Easting_OSGR'].isna().sum())
###Handle Junction COntrol Missing Values Fill with No_Junction_Control
print("Before FillNa Junction_Control ")
print(accDf['Junction_Control'].isna().sum())
accDf['Junction_Control'].fillna("No_Junction_Control", inplace=True)
print("After FillNa Junction_Control ")
print(accDf['Junction_Control'].isna().sum())

###Handle Time Missing Values Drop Na
print("Before FillNa Time ")
print(accDf['Time'].isna().sum())
accDf.dropna(axis=0,subset=['Time'], inplace = True)
print("After FillNa Time ")
print(accDf['Time'].isna().sum())

###Handle Did_Police_Officer_Attend_Scene_of_Accident by filling with mode
print("Before FillNa Did_Police_Officer_Attend_Scene_of_Accident ")
print(accDf['Did_Police_Officer_Attend_Scene_of_Accident'].isna().sum())
accDf['Did_Police_Officer_Attend_Scene_of_Accident'].fillna(accDf['Did_Police_Officer_Attend_Scene_of_Accident'].mode()[0], inplace=True)
print("After FillNa Did_Police_Officer_Attend_Scene_of_Accident ")
print(accDf['Did_Police_Officer_Attend_Scene_of_Accident'].isna().sum())


def fill_RSC(row):
    # print("ROWROW")
    # print(row['Road_Surface_Conditions'])
    choice_list = ["Wet/Damp","Dry"]
    if row['Road_Surface_Conditions'] != row['Road_Surface_Conditions']:
        # print("IS NA")
        if ['Weather_Conditions'] == "Raining without high winds" or ['Weather_Conditions'] == "Raining with high winds":
            return "Wet/Damp"
        else:
            my_value = random.choice(choice_list)
            # print("return my_value")
            # print(my_value)
            return my_value
    else:
        # print("return row['Road_Surface_Conditions']")
        # print(row['Road_Surface_Conditions'])
        return row['Road_Surface_Conditions']
def fill_WC(row):
    # print("ROWROW")
    # print(row['Road_Surface_Conditions'])
    choice_list_wet = ["Raining without high winds","Raining with high winds"]
    if row['Weather_Conditions'] != row['Weather_Conditions']:
        # print("IS NA")
        if ['Road_Surface_Conditions'] == "Wet/Damp":
            my_value = random.choice(choice_list_wet)
            # print("return my_value")
            # print(my_value)
            return my_value
        elif ['Road_Surface_Conditions'] == "Flood (Over 3cm of water)":
            return choice_list_wet[1]
        elif ['Road_Surface_Conditions'] == "Frost/Ice" or ['Road_Surface_Conditions'] == "Snow":
            return "Other"
        else:
            return "Fine without high winds"
    else:
        # print("return row['Road_Surface_Conditions']")
        # print(row['Road_Surface_Conditions'])
        return row['Weather_Conditions']

###Handle Road_Surface_Conditions by filling depending on Weather conditions
print("Before FillNa Road_Surface_Conditions")
print(accDf['Road_Surface_Conditions'].isna().sum())
print(accDf["Road_Surface_Conditions"].iloc[39811])
print(accDf["Road_Surface_Conditions"].iloc[46541])
print(accDf["Road_Surface_Conditions"].iloc[82326])
print(accDf["Road_Surface_Conditions"].iloc[82339])
accDf['Road_Surface_Conditions'] = accDf.apply(fill_RSC, axis=1)
print("After FillNa Road_Surface_Conditions ")
print(accDf['Road_Surface_Conditions'].isna().sum())
print(accDf["Road_Surface_Conditions"].iloc[39811])
print(accDf["Road_Surface_Conditions"].iloc[46541])
print(accDf["Road_Surface_Conditions"].iloc[82326])
print(accDf["Road_Surface_Conditions"].iloc[82339])

###Handle Weather_Conditions by filling depending on Weather conditions
print("Before FillNa Weather_Conditions")
print(accDf['Weather_Conditions'].isna().sum())
print(accDf["Weather_Conditions"].iloc[39811])
print(accDf["Weather_Conditions"].iloc[46541])
print(accDf["Weather_Conditions"].iloc[82326])
print(accDf["Weather_Conditions"].iloc[82339])
accDf['Weather_Conditions'] = accDf.apply(fill_WC, axis=1)
print("After FillNa Weather_Conditions ")
print(accDf['Weather_Conditions'].isna().sum())

###Handle Pedestrian_Crossing-Physical_Facilities Missing Values Fill with No physical crossing within 50 meters
print("Before FillNa Pedestrian_Crossing-Physical_Facilities ")
print(accDf['Pedestrian_Crossing-Physical_Facilities'].isna().sum())
accDf['Pedestrian_Crossing-Physical_Facilities'].fillna("No physical crossing within 50 meters", inplace=True)
print("After FillNa Pedestrian_Crossing-Physical_Facilities ")
print(accDf['Pedestrian_Crossing-Physical_Facilities'].isna().sum())

###Handle Carriageway_HazardsMissing Values Fill with NOne
print("Before FillNa Carriageway_Hazards")
print(accDf['Carriageway_Hazards'].isna().sum())
accDf['Carriageway_Hazards'].fillna("None", inplace=True)
print("After Carriageway_Hazards ")
print(accDf['Carriageway_Hazards'].isna().sum())


###Handle Pedestrian_Crossing-Human_Control missing Values Fill with None within 50 metres
print("Before FillNa Pedestrian_Crossing-Human_Control")
print(accDf['Pedestrian_Crossing-Human_Control'].isna().sum())
accDf['Pedestrian_Crossing-Human_Control'].fillna("None within 50 metres", inplace=True)
print("After Pedestrian_Crossing-Human_Control ")
print(accDf['Pedestrian_Crossing-Human_Control'].isna().sum())


###Handle Special_Conditions_at_Site missing Values Fill with NOne
print("Before FillNa Special_Conditions_at_Site")
print(accDf['Special_Conditions_at_Site'].isna().sum())
accDf['Special_Conditions_at_Site'].fillna("None", inplace=True)
print("After Special_Conditions_at_Site ")
print(accDf['Special_Conditions_at_Site'].isna().sum())


##HANDLE DUBLICATES
print(accDf.loc[accDf.duplicated( keep=False), ["Accident_Index",'Date','Day_of_Week']])
print("Before Drop Dublicates")
print(accDf.duplicated( keep=False).sum())
accDf.drop_duplicates(keep="first", inplace=True, ignore_index=True)
print("After Drop Dblicates ")
print(accDf.duplicated( keep=False).sum())
accDf.to_csv('accident_clean13th.csv', index=False)
profile = accDf.profile_report(title="Accidents")
profile.to_file(output_file="report_after_clean13th.html")


