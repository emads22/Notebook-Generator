from fpdf import FPDF
import pandas as pd


# Define the directory where the assets (e.g., topics.csv) are located
ASSETS_DIR = "./assets/"
# x horizontal positions (coordinates) of the lines in the notebook
X1_POS, X2_POS = 10, 200
# y vertical positions (coordinates) of the lines in the notebook
Y_POS = 22


def add_footer(pdf_object, text):
    # add breakline pdf.ln(1) is a breakline of 1 mm so pdf.ln(275) adds breaklines of 275 mm (total height is 297mm of A4 format)
    pdf_object.ln(275)
    # altenatively we can use pdf.set_y(-15) to set the vertical position (units depend on the FPDF instance) -15 means starting from bottom
    pdf_object.set_font(family="Times", style='I', size=8)
    pdf_object.set_text_color(180, 180, 180)
    pdf_object.cell(w=0, h=10, txt=text, align='R')


def add_lines(pdf_object):
    # first line after Header starts at y 21
    current_y = Y_POS
    # set y pos to this y
    pdf_object.set_y(current_y)
    # Set draw color to Grey to color each line to grey
    pdf_object.set_draw_color(100, 100, 100)
    # A4 has 297 mm vertically, leave some padding at the bottom (e.g., 20mm)
    padding_bottom = 20
    while current_y < (297 - padding_bottom):
        # Draw a line below the topic text for visual separation (coordinates are for 2 points of straight line starting from left side border)
        pdf_object.line(x1=X1_POS, y1=current_y, x2=X2_POS, y2=current_y)
        # increment by 10 (space between lines)
        current_y += 10


def add_yellow_background(pdf_object):
    """
    we cannot directly add a background color to the entire page using built-in methods like set_fill_color() because FPDF does not support background colors for the entire page. However, we can simulate a background color by drawing a rectangle that covers the entire page and setting its fill color. 
    """
    # Set fill color to bright yellow
    pdf_object.set_fill_color(255, 244, 85)
    # Draw a rectangle covering the entire page to simulate background color, 'F' tells FPDF to fill the rectangle with the specified fill color.
    # 210X2_POS97 mm is the size of A4 page
    pdf_object.rect(0, 0, 210, 297, 'F')


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
        # before anythin add yellow background like a notebook then add on top of it other components
        add_yellow_background(pdf)
        # Set the font for the PDF content
        pdf.set_font(family="Times", style='B', size=20)
        # Set the colorof text to gray rgb number
        pdf.set_text_color(100, 100, 100)
        # Add Header: a cell (text) to the PDF for the current topic
        pdf.cell(w=0, h=12, txt=row['Topic'], align='L')
        # Add Footer to this page
        add_footer(pdf, row['Topic'])
        # Add lines like a notebook to this page
        add_lines(pdf)

        # Iterate through the range of pages specified in the 'Pages' column of the DataFrame for the current topic
        # we already added the first page of this topic
        for _ in range(row['Pages'] - 1):
            pdf.add_page()
            # add yellow background first
            add_yellow_background(pdf)
            # Add Footer to each page
            add_footer(pdf, row['Topic'])
            # Add lines like a notebook to each page
            add_lines(pdf)

    # Output the PDF to a file named "notebook.pdf"
    pdf.output(ASSETS_DIR + "notebook.pdf")


if __name__ == "__main__":
    main()
