from fpdf import FPDF

# Initialize FPDF object with specified parameters
pdf = FPDF(
    orientation="P",    # Set orientation to portrait or landscape
    unit="mm",          # Set dimensions unit (e.g., millimeters)
    format="A4"         # Set paper format (e.g., A4, A3, etc.)
)


# Add a new page to the PDF, every configuration beneath it is relative to this page only
pdf.add_page()

# Set font for the PDF content, cells beneath only are affected by this font
pdf.set_font(
    family="Times",     # Set font family (e.g., Times, Arial, etc.)
    style="B",          # Set font style (e.g., bold, italic, etc.)
    size=12             # Set font size in points
)

# Add a cell (text) to the PDF
pdf.cell(
    w=0,                # Set cell width (0 means auto)
    h=12,               # Set cell height
    txt="Hello there!",  # Set text content
    align="L",          # Set text alignment (L=left, R=right, C=center)
    # Set whether to move to the next line after adding the cell (1=yes, 0=no)
    ln=1,
    border=1            # Set border width (0=no border, 1=border)
)

# Output the PDF to a file named "output.pdf"
pdf.output("output.pdf")
