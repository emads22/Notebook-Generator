# Notebook Generator

## Overview
Notebook Generator is a Python script that generates a PDF notebook with customizable topics and page layouts. It simulates a notebook-like appearance with yellow backgrounds and horizontal lines, making it suitable for various educational or note-taking purposes.

## Features
- **Customizable Topics**: Define topics and the number of pages for each topic using a CSV file (`assets/topics.csv`). These topics are features of Python to learn, and users can modify them as needed.
- **Notebook-like Appearance**: Generates PDFs with yellow backgrounds and horizontal lines resembling notebook pages.
- **Printable A4 PDF**: The generated PDF is A4-sized and printable, suitable for use with hard copies.
- **Easy Configuration**: Customize directory paths and layout parameters easily within the script.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as directory paths and layout parameters in `constants.py`.
   - Adjust `ASSETS_DIR` to specify the directory where asset files (e.g., topics.csv) are located.
   - Customize parameters such as `LINE_COLOR`, `HEADER_FONT`, etc., to adjust the appearance of the notebook.
5. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. The script will generate a PDF notebook with topics and pages specified in the `topics.csv` file (`assets/topics.csv`).
3. Each topic will have a customizable number of pages, with a notebook-like appearance including yellow backgrounds and horizontal lines.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.

