import pandas as pd # type: ignore
import numpy as np # type: ignore
from datetime import timedelta
from Methods import *

excelFilePath = "Cost Estimate Example.xlsx"

SP_dataframe = pd.read_excel(excelFilePath, sheet_name = "Spend Profile")
SP_conditions = pd.read_excel(excelFilePath, sheet_name= "Cost Estimate Conditions")
ProjectConditionsDF = pd.read_excel(excelFilePath, sheet_name= "Project Conditions")

OnstreamDate = pd.to_datetime(ProjectConditionsDF.iloc[0,0]).date()
#constructionDays = ProjectConditionsDF.iloc[0,1]

startDate = startDateM(OnstreamDate)
timeLine = createTimeline(startDate, OnstreamDate)
populateTimeLine(timeLine, SP_dataframe, SP_conditions, OnstreamDate)
returnTimeLineToExcel(timeLine)

print("test")



