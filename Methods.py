from datetime import timedelta
import pandas as pd # type: ignore

def createTimeline(conditions):
    timeLine = {}
    onstream = pd.to_datetime(conditions.iloc[0,1]).date()
    endDate = onstream + timedelta(days=30)
    startDate = onstream - timedelta(days= (conditions.iloc[2,1]))
    for i in range ((endDate - startDate).days + 1):
        currentDate = startDate + timedelta(days=i)
        timeLine[currentDate] = 0
    return timeLine

def populateTimeLine(timeLine, spendProfile, conditions):
    onstream = pd.to_datetime(conditions.iloc[0,1]).date()
    for index, row in spendProfile.iterrows():
        ## Need to code to catch when date is not in established timelines
        for i in range(3):
            date = (onstream - timedelta(days=row[i*2+3]))
            if date in timeLine:
                updatedValue = row['Cost'] * row[i*2+4]
                if timeLine[date] is None:
                    timeLine[date] = updatedValue
                else:
                    timeLine[date] += updatedValue
    return timeLine

def returnTimeLineToExcel(timeLine):
    dF = pd.DataFrame.from_dict(timeLine, orient ="index")
    with pd.ExcelWriter('output.xlsx', mode ='a', if_sheet_exists='replace') as writer:
        dF.to_excel(writer, index_label="Date", header=["Cost"], sheet_name="Raw Data") 