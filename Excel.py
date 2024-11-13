import pdfplumber
import pandas as pd

def pdf_to_excel(pdf_file,excel_file):
    with pdfplumber.open(pdf_file) as pdf:
        all_tables =[]
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if table:
                    df =pd.DataFrame(table)
                    all tables.append(df)
         if 