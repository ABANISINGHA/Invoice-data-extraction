# Invoice Data Extraction System

## Overview
The Invoice Data Extraction System is a Python-based solution for extracting key invoice details from PDF documents, such as invoice number, date, customer name, amounts, and tax details. The system uses OCR (Optical Character Recognition) for image-based PDFs and text extraction libraries for structured, text-based PDFs. It validates the extracted data and outputs a trust score for each field, ensuring the accuracy and reliability of the extracted information.

This implementation is designed to run on Kaggle, but it can be easily adapted to other environments. The project provides all necessary scripts, modules, and dependencies required to extract data and analyze PDF invoices.


## Key Features

- **Text Extraction**: Extracts data from text-based PDFs using `pdfplumber`.
- **OCR for Scanned PDFs**: Handles image-based PDFs using `pdf2image` and `Tesseract OCR` to extract text from scanned documents.
- **Data Validation**: Each extracted field is validated against predefined formats (e.g., invoice number, amounts, dates) to ensure accuracy.
- **Trust Score Calculation**: The system calculates a trust score based on the validity of each extracted field.
- **CSV Report Generation**: Outputs extracted data and trust scores in a CSV format.

## Installation

To install dependencies, run:

```bash
pip install -r requirements.txt
```
