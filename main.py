from fpdf import FPDF
import pandas as pd


# Define the directory where the assets (e.g., topics.csv) are located
ASSETS_DIR = "./assets/"


def add_footer(pdf_object, text):
    # add breakline pdf.ln(1) is a breakline of 1 mm so pdf.ln(275) adds breaklines of 275 mm (total height is 297mm of A4 format)
    pdf_object.ln(275)
    # altenatively we can use pdf.set_y(-15) to set the vertical position (units depend on the FPDF instance) -15 means starting from bottom
    pdf_object.set_font(family="Times", style='I', size=8)
    pdf_object.set_text_color(180, 180, 180)
    pdf_object.cell(w=0, h=10, txt=text, align='R')


def main():
    # Create an instance of the FPDF class with specified parameters for the PDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    # Disable automatic page breaks and set margin to 0 for full-page content
    pdf.set_auto_page_break(auto=False, margin=0)

    # Read the data from the topics.csv file into a pandas DataFrame
    df = pd.read_csv(ASSETS_DIR + "topics.csv")

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Add a new page to the PDF for each topic
        pdf.add_page()
        # Set the font for the PDF content
        pdf.set_font(family="Times", style='B', size=20)
        # Set the colorof text to gray rgb number
        pdf.set_text_color(100, 100, 100)
        # Add Header: a cell (text) to the PDF for the current topic
        pdf.cell(w=0, h=12, txt=row['Topic'], align='L')
        # Draw a line below the topic text for visual separation (coordinates are for 2 points of straight line starting from left side border)
        pdf.line(x1=10, y1=21, x2=200, y2=21)
        # Add Footer to this page
        add_footer(pdf, row['Topic'])

        # Iterate through the range of pages specified in the 'Pages' column of the DataFrame for the current topic
        # we already added the first page of this topic
        for _ in range(row['Pages'] - 1):
            pdf.add_page()
            # Add Footer to each page
            add_footer(pdf, row['Topic'])

    # Output the PDF to a file named "notebook.pdf"
    pdf.output(ASSETS_DIR + "notebook.pdf")


if __name__ == "__main__":
    main()
