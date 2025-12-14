from datetime import timedelta
from statistics import mode
import pandas as pd # type: ignore

def startDateM(endDate):
    startDate = endDate - timedelta(days=360)
    return startDate

def createTimeline(startDate, endDate):
    timeLine = {}
    for i in range ((endDate - startDate).days + 1):
        currentDate = startDate + timedelta(days=i)
        timeLine[currentDate] = None
    return timeLine

def populateTimeLine(timeLine, SP_dataframe, SP_conditions, onstream):
    DF = pd.merge(SP_dataframe, SP_conditions, on='Description', how='left')
    for index, row in DF.iterrows():
        if pd.isnull(row['Payment Schedule (days from Onstream)']):
            date = (onstream)
        else:
            date = (onstream - timedelta(days=row['Payment Schedule (days from Onstream)']))
        if date in timeLine:
            updatedValue = row['Cost']
            if timeLine[date] is None:
                timeLine[date] = updatedValue
            else:
                timeLine[date] += updatedValue
    return timeLine

def returnTimeLineToExcel(timeLine):
    dF = pd.DataFrame.from_dict(timeLine, orient ="index")
    with pd.ExcelWriter('output.xlsx', mode ='a', if_sheet_exists='replace') as writer:
        dF.to_excel(writer, index_label="Date", header=["Cost"], sheet_name="Raw Data") 