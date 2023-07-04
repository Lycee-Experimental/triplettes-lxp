import ast
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.platypus.flowables import KeepTogether 
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas

data=[
[{'Cléméntine', 'Davy', 'Julie', 'Mika'}, {'Maria', 'Gestionnaire', 'Renaud', 'Enoch'}, {'Benjamin', 'Flora', 'Maude'}, {'Fanny', 'Xavier', 'Nath'}, {'Marie', 'Pauline', 'Valentin'}],
[{'Cléméntine', 'Davy', 'Julie', 'Mika'}, {'Pauline', 'Nath', 'Enoch'}, {'Benjamin', 'Flora', 'Maude'}, {'Maria', 'Gestionnaire', 'Renaud', 'Xavier'}, {'Marie', 'Fanny', 'Valentin'}],
[{'Pauline', 'Benjamin', 'Julie'}, {'Maria', 'Marie', 'Mika'}, {'Gestionnaire', 'Xavier', 'Nath', 'Enoch'}, {'Flora', 'Cléméntine', 'Renaud', 'Davy'}, {'Fanny', 'Valentin', 'Maude'}],
[{'Gestionnaire', 'Valentin', 'Maude', 'Enoch'}, {'Fanny', 'Xavier', 'Nath'}, {'Maria', 'Julie', 'Mika'}, {'Marie', 'Benjamin', 'Pauline'}, {'Cléméntine', 'Renaud', 'Flora', 'Davy'}],
[{'Cléméntine', 'Davy', 'Julie', 'Mika'}, {'Benjamin', 'Flora', 'Maude'}, {'Enoch', 'Gestionnaire', 'Xavier', 'Nath'}, {'Marie', 'Pauline', 'Valentin'}, {'Fanny', 'Maria', 'Renaud'}],
[{'Enoch', 'Pauline', 'Xavier', 'Nath'}, {'Benjamin', 'Flora', 'Maude'}, {'Fanny', 'Marie', 'Valentin'}, {'Cléméntine', 'Davy', 'Julie'}, {'Maria', 'Gestionnaire', 'Renaud', 'Mika'}],
[{'Enoch', 'Pauline', 'Xavier', 'Nath'}, {'Marie', 'Cléméntine', 'Davy'}, {'Maria', 'Julie', 'Mika'}, {'Flora', 'Gestionnaire', 'Renaud', 'Benjamin'}, {'Fanny', 'Valentin', 'Maude'}],
[{'Cléméntine', 'Davy', 'Julie', 'Mika'}, {'Benjamin', 'Gestionnaire', 'Maude', 'Enoch'}, {'Maria', 'Renaud', 'Flora'}, {'Pauline', 'Xavier', 'Nath'}, {'Marie', 'Valentin', 'Fanny'}],
[{'Maria', 'Julie', 'Mika'}, {'Enoch', 'Gestionnaire', 'Xavier', 'Nath'}, {'Marie', 'Pauline', 'Benjamin'}, {'Flora', 'Cléméntine', 'Renaud', 'Davy'}, {'Fanny', 'Valentin', 'Maude'}],
[{'Fanny', 'Gestionnaire', 'Renaud', 'Xavier'}, {'Enoch', 'Pauline', 'Nath'}, {'Maria', 'Marie', 'Mika'}, {'Cléméntine', 'Davy', 'Julie'}, {'Benjamin', 'Valentin', 'Flora', 'Maude'}],
[{'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Valentin', 'Flora', 'Maude'}, {'Pauline', 'Benjamin', 'Julie'}, {'Marie', 'Xavier', 'Nath', 'Enoch'}, {'Fanny', 'Maria', 'Renaud'}],
[{'Cléméntine', 'Maude', 'Enoch'}, {'Marie', 'Pauline', 'Valentin', 'Benjamin'}, {'Fanny', 'Xavier', 'Nath'}, {'Maria', 'Julie', 'Mika'}, {'Flora', 'Gestionnaire', 'Renaud', 'Davy'}],
[{'Marie', 'Nath', 'Enoch'}, {'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Valentin', 'Flora', 'Maude'}, {'Pauline', 'Benjamin', 'Julie'}, {'Fanny', 'Maria', 'Renaud', 'Xavier'}],
[{'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Marie', 'Benjamin', 'Valentin', 'Pauline'}, {'Maria', 'Renaud', 'Flora'}, {'Fanny', 'Xavier', 'Nath'}, {'Julie', 'Maude', 'Enoch'}],
[{'Enoch', 'Pauline', 'Xavier', 'Nath'}, {'Maria', 'Marie', 'Mika'}, {'Flora', 'Benjamin', 'Gestionnaire', 'Renaud'}, {'Cléméntine', 'Davy', 'Julie'}, {'Fanny', 'Valentin', 'Maude'}],
[{'Pauline', 'Xavier', 'Nath', 'Enoch'}, {'Valentin', 'Marie', 'Gestionnaire', 'Davy'}, {'Benjamin', 'Flora', 'Maude'}, {'Cléméntine', 'Julie', 'Mika'}, {'Fanny', 'Maria', 'Renaud'}],
[{'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Benjamin', 'Maude', 'Julie', 'Enoch'}, {'Maria', 'Flora', 'Renaud'}, {'Pauline', 'Xavier', 'Nath'}, {'Marie', 'Fanny', 'Valentin'}],
[{'Enoch', 'Pauline', 'Nath'}, {'Gestionnaire', 'Marie', 'Valentin', 'Davy'}, {'Benjamin', 'Flora', 'Maude'}, {'Cléméntine', 'Julie', 'Mika'}, {'Maria', 'Fanny', 'Renaud', 'Xavier'}],
[{'Marie', 'Cléméntine', 'Davy'}, {'Fanny', 'Xavier', 'Nath'}, {'Pauline', 'Valentin', 'Maude', 'Enoch'}, {'Maria', 'Julie', 'Mika'}, {'Flora', 'Gestionnaire', 'Renaud', 'Benjamin'}],
[{'Fanny', 'Gestionnaire', 'Renaud', 'Xavier'}, {'Marie', 'Cléméntine', 'Davy'}, {'Enoch', 'Pauline', 'Nath'}, {'Maria', 'Julie', 'Mika'}, {'Benjamin', 'Valentin', 'Flora', 'Maude'}],
[{'Cléméntine', 'Davy', 'Julie', 'Mika'}, {'Maria', 'Gestionnaire', 'Renaud', 'Enoch'}, {'Benjamin', 'Flora', 'Maude'}, {'Pauline', 'Xavier', 'Nath'}, {'Marie', 'Valentin', 'Fanny'}],
[{'Gestionnaire', 'Benjamin', 'Valentin', 'Pauline'}, {'Maria', 'Flora', 'Renaud'}, {'Fanny', 'Xavier', 'Nath'}, {'Julie', 'Maude', 'Enoch'}, {'Marie', 'Cléméntine', 'Davy', 'Mika'}],
[{'Pauline', 'Gestionnaire', 'Renaud', 'Enoch'}, {'Marie', 'Maria', 'Mika'}, {'Fanny', 'Xavier', 'Nath'}, {'Cléméntine', 'Davy', 'Julie'}, {'Benjamin', 'Valentin', 'Flora', 'Maude'}],
[{'Enoch', 'Pauline', 'Nath'}, {'Gestionnaire', 'Marie', 'Valentin', 'Davy'}, {'Benjamin', 'Flora', 'Maude'}, {'Maria', 'Julie', 'Mika'}, {'Fanny', 'Cléméntine', 'Renaud', 'Xavier'}],
[{'Gestionnaire', 'Valentin', 'Maude', 'Enoch'}, {'Fanny', 'Xavier', 'Nath'}, {'Maria', 'Marie', 'Mika'}, {'Benjamin', 'Pauline', 'Julie'}, {'Cléméntine', 'Renaud', 'Flora', 'Davy'}],
[{'Pauline', 'Xavier', 'Nath', 'Enoch'}, {'Gestionnaire', 'Marie', 'Valentin', 'Mika'}, {'Benjamin', 'Flora', 'Maude'}, {'Cléméntine', 'Davy', 'Julie'}, {'Fanny', 'Maria', 'Renaud'}],
[{'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Valentin', 'Flora', 'Maude'}, {'Nath', 'Julie', 'Enoch'}, {'Maria', 'Renaud', 'Fanny', 'Xavier'}, {'Marie', 'Pauline', 'Benjamin'}],
[{'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Benjamin', 'Maude', 'Julie', 'Enoch'}, {'Maria', 'Renaud', 'Flora'}, {'Fanny', 'Xavier', 'Nath'}, {'Marie', 'Pauline', 'Valentin'}],
[{'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Marie', 'Valentin', 'Maude', 'Enoch'}, {'Maria', 'Renaud', 'Flora'}, {'Fanny', 'Xavier', 'Nath'}, {'Pauline', 'Benjamin', 'Julie'}],
[{'Cléméntine', 'Davy', 'Julie', 'Mika'}, {'Benjamin', 'Gestionnaire', 'Maude', 'Enoch'}, {'Maria', 'Flora', 'Renaud'}, {'Fanny', 'Xavier', 'Nath'}, {'Marie', 'Pauline', 'Valentin'}],
[{'Enoch', 'Pauline', 'Xavier', 'Nath'}, {'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Maria', 'Renaud', 'Flora'}, {'Marie', 'Valentin', 'Fanny'}, {'Benjamin', 'Maude', 'Julie'}],
[{'Marie', 'Maria', 'Mika'}, {'Fanny', 'Xavier', 'Nath'}, {'Pauline', 'Valentin', 'Maude', 'Enoch'}, {'Benjamin', 'Gestionnaire', 'Renaud', 'Flora'}, {'Cléméntine', 'Davy', 'Julie'}],
[{'Pauline', 'Xavier', 'Nath', 'Enoch'}, {'Valentin', 'Marie', 'Gestionnaire', 'Davy'}, {'Benjamin', 'Flora', 'Maude'}, {'Maria', 'Julie', 'Mika'}, {'Fanny', 'Cléméntine', 'Renaud'}],
[{'Marie', 'Cléméntine', 'Davy'}, {'Pauline', 'Gestionnaire', 'Renaud', 'Enoch'}, {'Fanny', 'Xavier', 'Nath'}, {'Maria', 'Julie', 'Mika'}, {'Benjamin', 'Valentin', 'Flora', 'Maude'}],
[{'Pauline', 'Maude', 'Enoch'}, {'Marie', 'Benjamin', 'Gestionnaire', 'Valentin'}, {'Fanny', 'Xavier', 'Nath'}, {'Maria', 'Julie', 'Mika'}, {'Flora', 'Cléméntine', 'Renaud', 'Davy'}],
[{'Gestionnaire', 'Marie', 'Valentin', 'Mika'}, {'Enoch', 'Pauline', 'Nath'}, {'Benjamin', 'Flora', 'Maude'}, {'Maria', 'Fanny', 'Renaud', 'Xavier'}, {'Cléméntine', 'Davy', 'Julie'}],
[{'Cléméntine', 'Maude', 'Enoch'}, {'Pauline', 'Gestionnaire', 'Valentin', 'Benjamin'}, {'Fanny', 'Xavier', 'Nath'}, {'Maria', 'Julie', 'Mika'}, {'Marie', 'Flora', 'Renaud', 'Davy'}],
[{'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Marie', 'Maria', 'Renaud', 'Enoch'}, {'Valentin', 'Flora', 'Maude'}, {'Fanny', 'Xavier', 'Nath'}, {'Pauline', 'Benjamin', 'Julie'}],
[{'Cléméntine', 'Gestionnaire', 'Davy', 'Mika'}, {'Maria', 'Flora', 'Renaud'}, {'Pauline', 'Benjamin', 'Julie'}, {'Marie', 'Enoch', 'Xavier', 'Nath'}, {'Fanny', 'Valentin', 'Maude'}],
[{'Cléméntine', 'Davy', 'Julie', 'Mika'}, {'Benjamin', 'Gestionnaire', 'Pauline', 'Valentin'}, {'Maria', 'Flora', 'Renaud'}, {'Fanny', 'Xavier', 'Nath'}, {'Marie', 'Maude', 'Enoch'}],
[{'Valentin', 'Marie', 'Gestionnaire', 'Davy'}, {'Benjamin', 'Flora', 'Maude'}, {'Fanny', 'Xavier', 'Nath'}, {'Maria', 'Julie', 'Mika'}, {'Cléméntine', 'Pauline', 'Renaud', 'Enoch'}]
]

# Define the custom canvas class for page numbering
class PageNumCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.page_number = 0

    def showPage(self):
        self.page_number += 1
        self.saveState()
        self.setFont('Helvetica', 10)
        self.drawCentredString(letter[0] / 2.0, 0.75 * inch, f'Page {self.page_number}')
        self.restoreState()
        canvas.Canvas.showPage(self)

# Get the maximum length of any set in the data
max_len = max(len(s) for row in data for s in row)

# Create a list of empty lists for the column data, with the headers
col_data = [['g1', 'g2', 'g3', 'g4', 'g5']]
col_data += [[] for _ in range(max_len)]

# Create a list of tables
tables = []


# Define the PDF document
doc = SimpleDocTemplate("output.pdf", pagesize=A4)

style = ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12, leading=14)

# Define the paragraph text
text = """
Ensemble des triplettes compatibles avec les paramètres suivants :<br/><br/>

- Mixité de genre des triplettes (2+2 dans les quadruplettes)<br/>

- Brassage des triplettes (jusqu'en 2020)<br/>

- Le/la gestionnaire dans une quadriplette.<br/>

- Tou.te.s les MEEs de chaque groupes de SPé sont dispos ensemble sur au moins 2 gestions (pour éviter que les ateliers d'une spé tombent 2 fois sur la même gestion).<br/><br/>
"""
# Create the paragraph
paragraph = Paragraph(text, style)
tables.append(KeepTogether(paragraph))
# Loop through each row in the data
for row in data:
    # Create a list of empty lists for the column data, with the headers
    col_data = [['G1', 'G2', 'G3', 'G4', 'G5']]
    col_data += [[] for _ in range(max_len)]
    # Loop through each set in the row and add its items to the corresponding column
    for i, s in enumerate(row):
        for j in range(max_len):
            if j < len(s):
                col_data[j+1].append(list(s)[j])
            else:
                col_data[j+1].append('')

    # Create a table from the column data
    table = Table(col_data, colWidths=A4[0]/6, repeatRows=1)
    # Define the table style
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.white),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 20),
    ('RIGHTPADDING', (0,0), (-1,-1), 20),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ]))

    # Add the table to the list
    tables.append(KeepTogether(table))

# Build the PDF document
doc.build(tables)

