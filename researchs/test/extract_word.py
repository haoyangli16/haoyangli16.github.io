# Install the required package first
# pip install PyPDF2

import PyPDF2

def extract_text_from_pdf(pdf_path, output_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ''

        # Loop through each page and extract text
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() + '\n'

    # Save the extracted text to a .txt file
    with open(output_path, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)
    print(f'Text extracted and saved to {output_path}')

# Usage
pdf_path = '/Users/tommy/Projects/personal/haoyangli16.github.io/researchs/test/paper.pdf'  # Path to your PDF file
output_path = '/Users/tommy/Projects/personal/haoyangli16.github.io/researchs/test/output.txt'              # Path to save the extracted text
extract_text_from_pdf(pdf_path, output_path)