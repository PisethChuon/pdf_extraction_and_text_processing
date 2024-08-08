import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_customer_info(text):
    info = {}
    
    # Name
    name_pattern = r'Name:\s*(.+)'
    match = re.search(name_pattern, text)
    if match:
        info['Name'] = match.group(1).strip()
    
    # Contact Number
    contact_pattern = r'Contact Number:\s*([\+\d\s-]+)'
    match = re.search(contact_pattern, text)
    if match:
        info['Contact Number'] = match.group(1).strip()
    
    # Email
    email_pattern = r'Email:\s*([\w\.-]+@[\w\.-]+)'
    match = re.search(email_pattern, text)
    if match:
        info['Email'] = match.group(1).strip()
    
    # Address
    address_pattern = r'Address:\s*(.+)'
    match = re.search(address_pattern, text)
    if match:
        info['Address'] = match.group(1).strip()
    
    return info

pdf_path = "Test.pdf"
text = extract_text_from_pdf(pdf_path)
customer_info = extract_customer_info(text)

print("Extracted Customer Information:")
for key, value in customer_info.items():
    print(f"{key}: {value}")
