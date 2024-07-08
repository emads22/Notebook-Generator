from fpdf import FPDF
import pandas as pd
import traceback
from constants import *


class NoteBook(FPDF):
    """
    Class representing a PDF notebook, inheriting from FPDF for PDF generation.
    """

    def __init__(self):
        """
        Constructor method for initializing the notebook.
        """
        super().__init__(orientation=ORIENTATION, unit=UNIT, format=FORMAT)
        # Disable automatic page breaks and set margin to 0 for full-page content
        # This ensures that the content will be placed at exact positions specified by set_xy() or set_x() and set_y(), and no automatic page breaks will occur.
        self.set_auto_page_break(auto=False, margin=0)

        self.topics = self.load_topics()

    def load_topics(self):
        """
        Method for loading topics and their corresponding number of pages from a CSV file.
        """
        df = pd.read_csv(TOPICS_FILE)
        # Iterates over each row in the DataFrame and extracts 'Topic' and 'Pages' columns and use Generator expression to yield tuples containing topic and corresponding pages
        topics_generator = ((row['Topic'], row['Pages'])
                            for _, row in df.iterrows())
        return topics_generator

    def add_yellow_background(self):
        """
        Method for adding a yellow background to the entire page.
        """
        self.set_fill_color(255, 244, 85)  # Set fill color to yellow
        # Draw a rectangle covering the entire page and fill it with the specified color
        self.rect(x=0, y=0, w=self.w, h=self.h, style='F')

    def add_lines(self):
        """
        Method for adding horizontal lines across the page.
        """
        self.set_draw_color(
            *LINE_COLOR)  # Set draw color to specified line color
        current_y = LINES_Y_START  # Start drawing lines from the specified y-coordinate
        # Draw lines until reaching the bottom of the page
        while current_y < (self.h - PADDING_BOTTOM):
            self.set_y(current_y)  # Set the current y-position
            # Draw a line across the page
            self.line(x1=0, y1=current_y, x2=self.w, y2=current_y)
            current_y += LINE_SPACING  # Increment y-coordinate for the next line

    def add_margin_line(self):
        """
        Method for adding a vertical margin line.
        """
        self.set_draw_color(
            *MARGIN_COLOR)  # Set color to specified margin color
        self.line(x1=MARGIN_X_START, y1=0, x2=MARGIN_X_START,
                  y2=self.h)  # Draw a vertical line

    def add_header(self, text):
        """
        Method for adding a header to the page.
        """
        self.set_font(*HEADER_FONT)  # Set font for the header
        self.set_text_color(*HEADER_COLOR)  # Set text color for the header
        self.set_y(HEADER_Y)  # Set y-position for the header
        # Add header text centered horizontally
        self.cell(w=0, h=10, txt=text, align='C')

    def add_footer(self, page_number):
        """
        Method for adding a footer with page number.
        """
        self.set_font(*FOOTER_FONT)  # Set font for the footer
        self.set_text_color(*HEADER_COLOR)  # Set text color for the footer
        self.set_y(self.h - FOOTER_Y)  # Set y-position for the footer
        # Add page number aligned to the right
        self.cell(w=0, h=10, txt=str(page_number), align='R')

    def create_page(self, header, footer):
        """
        Method for creating a new page with specified header and footer.
        """
        self.add_page()  # Add a new page
        self.add_yellow_background()  # Add yellow background to the page
        self.add_lines()  # Add horizontal lines
        self.add_margin_line()  # Add margin line
        self.add_header(header)  # Add header
        self.add_footer(footer)  # Add footer

    def generate(self):
        """
        Method for generating the PDF notebook.
        """
        for topic, pages in self.topics:  # Iterate through topics and their corresponding pages
            for page_i in range(1, pages+1):  # Iterate through pages for each topic
                # Create a new page for the topic
                self.create_page(header=topic, footer=page_i)
        self.save_output()  # Save the generated PDF

    def save_output(self):
        """
        Method for saving the generated PDF.
        """
        self.output(OUTPUT_FILE)  # Output the generated PDF to a file


def main():
    """
    Main function for executing the PDF notebook generation.
    """
    # Display logo
    print("\n\n\n\n", ASCII_ART, "\n\n")
    
    notebook = NoteBook()  # Create a new instance of the NoteBook class
    notebook.generate()  # Generate the PDF notebook


if __name__ == "__main__":
    try:
        main()  # Execute the main function
        print("\n\n--- PDF notebook generated successfully. ---\n\n")
    except Exception as e:
        # Print error message if generation fails
        print(f"\n\n- PDF notebook generation failed:\n\n{str(e)}\n\n")
        traceback.print_exc()  # Print traceback for debugging
        print("\n\n")  # Print newline for clarity
