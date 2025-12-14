import pandas as pd # type: ignore
import numpy as np # type: ignore
from datetime import timedelta
from Methods import *

excelFilePath = "Cost Estimate Example.xlsx"

spendProfile = pd.read_excel(excelFilePath, sheet_name = "Spend Profile")
conditions = pd.read_excel(excelFilePath, sheet_name= "Conditions")

timeLine = createTimeline(conditions)
populateTimeLine(timeLine, spendProfile, conditions)
returnTimeLineToExcel(timeLine)

print("test")
print("test 2")
print("test 3")


