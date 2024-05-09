import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle

df = pd.read_csv("C:\\Users\\navee\\Documents\\VSCODE\\medical_history_dataset.csv")

df.head()

def create_pdf_from_dataframe(dataframe, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = ParagraphStyle(name='Normal', fontSize=12)
    
    content = []
    
    for index, row in dataframe.iterrows():
        row_content = []
    for column_name, value in row.items():
        row_content.append(f"{column_name}: {value}")
    
    content.append(Paragraph(", ".join(row_content), styles))
    content.append(Paragraph("<br/><br/>", styles)) 
    doc.build(content)

create_pdf_from_dataframe(df, "output.pdf")







