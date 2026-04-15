from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("reports/pdf/report.pdf")
styles = getSampleStyleSheet()

content = []

content.append(Paragraph("AI Sales Forecast Report", styles['Title']))
content.append(Spacer(1, 10))

content.append(Paragraph("This report shows revenue, profit and forecast insights.", styles['Normal']))
content.append(Spacer(1, 10))

content.append(Paragraph("Key Insights:", styles['Heading2']))
content.append(Paragraph("Top product and region identified with highest revenue.", styles['Normal']))

content.append(Spacer(1, 10))

content.append(Paragraph("Business Impact:", styles['Heading2']))
content.append(Paragraph("This analysis helps in improving sales strategy and forecasting future growth.", styles['Normal']))

doc.build(content)

print("✅ PDF Improved")