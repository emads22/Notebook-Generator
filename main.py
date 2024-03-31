from fpdf import FPDF
import pandas as pd


# Define the directory where the assets (e.g., topics.csv) are located
ASSETS_DIR = "./assets/"

# Create an instance of the FPDF class with specified parameters for the PDF
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Read the data from the topics.csv file into a pandas DataFrame
df = pd.read_csv(ASSETS_DIR + "topics.csv")

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Add a new page to the PDF for each topic
    pdf.add_page()
    # Set the font for the PDF content
    pdf.set_font(family="Times", style='B', size=24)
    # Set the colorof text to gray rgb number
    pdf.set_text_color(100, 100, 100)
    # Add a cell (text) to the PDF for the current topic
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L')
    # Draw a line below the topic text for visual separation (coordinates are for 2 points of straight line starting from left side border)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

# Output the PDF to a file named "output.pdf"
pdf.output("output.pdf")
