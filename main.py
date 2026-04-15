import os

os.system("python python/data_generator.py")
os.system("python python/data_cleaning.py")
os.system("python python/db_loader.py")
os.system("python python/forecasting.py")
os.system("python python/chart_generator.py")
os.system("python python/report_generator.py")
os.system("python python/pdf_report.py")

print("🚀 FULL PROJECT EXECUTED SUCCESSFULLY")