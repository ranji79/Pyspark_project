from ydata_profiling import ProfileReport
import pandas as pd

df=pd.read_csv(r"C:\Users\Home\PycharmProjects\pythonProject\Files\Contact_info.csv")
print(df)
Result=ProfileReport(df)
Result.to_file("Profile_Report.html")
