# Invoice Data Extraction System

## Overview
The Invoice Data Extraction System is a Python-based solution for extracting key invoice details from PDF documents, such as invoice number, date, customer name, amounts, and tax details. The system uses Gemini API for OCR (Optical Character Recognition) on image-based PDFs and Pdfplumber for text extraction in structured, text-based PDFs. It validates the extracted data and outputs a trust score for each field, ensuring the accuracy and reliability of the extracted information.

This implementation is designed to run on Kaggle, but it can be easily adapted to other environments. The project provides all necessary scripts, modules, and dependencies required to extract data and analyze PDF invoices.


## Key Features

- **Text Extraction**: Extracts data from text-based PDFs using `pdfplumber`.
- **OCR for Scanned PDFs**: OCR for Scanned PDFs: Handles image-based PDFs using Gemini API.
- **Data Validation**: Each extracted field is validated against predefined formats (e.g., invoice number, amounts, dates) to ensure accuracy.
- **Trust Score Calculation**: The system calculates a trust score based on the validity of each extracted field.
- **CSV Report Generation**: Outputs extracted data and trust scores in a CSV format.

## Setup and Installation
Kaggle Environment

This project is designed to run in a Kaggle notebook environment. You can also run it locally, but make sure you have the necessary libraries installed.

Step 1: Clone the Repository
You can clone this GitHub repository into your local system or a Kaggle notebook by running the following command:
```bash
git clone https://github.com/your-username/invoice-data-extraction.git
```

Alternatively, you can upload the project files directly to your Kaggle notebook


## Installation

To install dependencies, run:

```bash
pip install -r requirements.txt
```

## Dependencies

Make sure to install the following dependencies:

- `pdfplumber`: For PDF text extraction.
- `pdf2image`: Converts PDF pages to images (used for OCR).
- `requests`: For making API calls to Gemini.
- `pandas`: For handling CSV outputs.

## Gemini API Configuration
The project uses the Gemini API to handle OCR for image-based PDFs. You will need to configure your API key to use this feature.

- `Step 1:` Get a Gemini API Key
Sign up for the Gemini API and obtain your API key.
- `Step 2:` Configure the API Key
In the project directory, locate the config.py file.
Add your Gemini API key to the configuration:

```bash
GEMINI_API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateCo"
GEMINI_API_KEY = "your_gemini_api_key_here"
```

## Running the Extraction System
Once the environment is set up, you can run the extraction system by executing the main script.

Extracting Data from PDFs:


If your PDFs are inside a zip file (or in a directory), the system will extract data from them and output a CSV file with the extracted fields.
```bash
# Run the script in the Kaggle notebook
!python extract_invoices.py --input path/to/pdf/folder --output output.csv
```

This will extract all PDFs in the input directory and generate a CSV report with the extracted fields and trust scores.

```bash
invoice-data-extraction/
│
├── README.md              # Project overview and instructions
├── requirements.txt       # Python dependencies
├── extract_invoices.py    # Main script for PDF extraction
├── validator.py           # Validation module for extracted fields
├── ocr_handler.py         # OCR module using Gemini API for image-based PDFs
├── config.py              # Configuration settings (API keys, input/output paths, etc.)
└── sample_invoices/       # Sample PDF invoices (optional)
```
- **extract_invoices.py**: The main script for running the extraction. It handles both text-based and image-based PDFs, performs extraction, validation, and outputs a CSV report.
- **validator.py**: Contains the validation logic to check the extracted fields against predefined patterns (e.g., regex for dates, numeric checks for amounts).
- **ocr_handler.py**: Handles OCR processing for scanned/image-based PDFs using the Gemini API.
- **config.py**: Allows you to configure input/output paths, API keys, and other settings.
- **requirements.txt**: Lists all dependencies required to run the project.


## Configuring the System
If you'd like to configure paths or settings (e.g., API keys, input/output directories), you can modify the config.py file. Example configuration:
```bash
# config.py

INPUT_DIR = "../input/sample_invoices/"  # Path to the folder containing PDFs
OUTPUT_CSV = "../output/invoice_report.csv"  # Path to the output CSV

# API key for Gemini OCR
GEMINI_API_KEY = "your_api_key_here"
GEMINI_API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateCo"
```

### Example Output (CSV)

The output will be a CSV file with the following fields:

| File Name       | Invoice Number | Invoice Date | Customer Name   | Total Amount | Trust Score |
|-----------------|----------------|--------------|-----------------|--------------|-------------|
| INV-145.pdf     | INV-145        | 28 Mar 2024  | Indraja Mohite  | 1148.00      | 100%        |
| INV-142.pdf     | INV-142        | 07 Mar 2024  | Urmila Jangam   | 1032.00      | 99%         |
| INV-128.pdf     | INV-128        | 23 Feb 2024  | Atia Latif      | 2450.00      | 100%        |

Each row contains details from a PDF file along with a "Trust Score" indicating how accurate the extracted fields are.


## Accuracy and Trustworthiness
The system uses predefined validation rules (e.g., regular expressions) to ensure the accuracy of the extracted fields. Each field is checked against expected patterns, and a trust score is calculated for each document. The goal is to achieve 99% trust in the extracted data.

- **Validation Rules**: Invoice numbers, dates, amounts, and other fields are validated using regex patterns.
- **Trust Score**: Calculated based on the number of fields that pass validation. A score of 100% indicates all fields are valid.
