import os
import csv
import zipfile
from validator import calculate_score
from ocr_handler import extract_text_from_pdf

def unzip_file(zip_file_path, extract_to):
    """
    Unzips a ZIP file to the specified location.
    
    Parameters:
    - zip_file_path: str: Path to the zip file.
    - extract_to: str: Path where the contents will be extracted.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted zip file to {extract_to}")

def get_pdf_paths(directory):
    """
    Retrieves all PDF files from the given directory.
    
    Parameters:
    - directory: str: Path to the directory containing PDFs.
    
    Returns:
    - list: List of paths to PDF files.
    """
    pdf_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_paths.append(os.path.join(root, file))
    return pdf_paths

def generate_report(invoice_paths, output_csv):
    """
    Generates a CSV report of extracted fields for PDF invoices.

    Parameters:
    - invoice_paths: list: List of paths to the PDF invoices.
    - output_csv: str: Path to the output CSV file.
    """
    with open(output_csv, mode='w', newline='') as csv_file:
        fieldnames = ['file', 'invoice_number', 'invoice_date', 'customer_name', 'due_date',
                      'taxable_amount', 'cgst', 'sgst', 'total_amount', 'total_discount',
                      'amount_in_words', 'account_number', 'ifsc_code', 'trust_score']
        
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for file in invoice_paths:
            text_content = extract_text_from_pdf(file)
            fields = extract_fields(text_content)
            trust_score = calculate_score(fields)
            writer.writerow({
                'file': os.path.basename(file),
                'invoice_number': fields.get('invoice_number'),
                'invoice_date': fields.get('invoice_date'),
                'customer_name': fields.get('customer_name'),
                'due_date': fields.get('due_date'),
                'taxable_amount': fields.get('taxable_amount'),
                'cgst': fields.get('cgst'),
                'sgst': fields.get('sgst'),
                'total_amount': fields.get('total_amount'),
                'total_discount': fields.get('total_discount'),
                'amount_in_words': fields.get('amount_in_words'),
                'account_number': fields.get('account_number'),
                'ifsc_code': fields.get('ifsc_code'),
                'trust_score': trust_score
            })
            print(f"Processed {file} with trust score: {trust_score}%")

if __name__ == "__main__":
    # Input zip file path and the folder where PDFs will be extracted
    zip_file_path = 'path_to_your_zip_file.zip'  # Path to the input zip file
    extract_to = 'extracted_invoices'  # Folder where the PDFs will be extracted

    # Step 1: Unzip the zip file to a folder
    unzip_file(zip_file_path, extract_to)

    # Step 2: Get the list of PDF files from the extracted folder
    invoice_paths = get_pdf_paths(extract_to)

    # Step 3: Generate the CSV report
    csv_output_path = 'invoice_report.csv'  # Path to output CSV file
    generate_report(invoice_paths, csv_output_path)

    print(f"Report generated: {csv_output_path}")
