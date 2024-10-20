import re

def validate_fields(fields):
    validation_rules = {
        'invoice_number': lambda x: bool(re.match(r'^INV-\d+$', x)),
        'invoice_date': lambda x: bool(re.match(r'^\d{1,2} \w+ \d{4}$', x)),
        'taxable_amount': lambda x: bool(re.match(r'^\d+(\.\d{1,2})?$', x)),
        'cgst': lambda x: bool(re.match(r'^\d+(\.\d{1,2})?$', x)),
        'sgst': lambda x: bool(re.match(r'^\d+(\.\d{1,2})?$', x)),
        'total_amount': lambda x: bool(re.match(r'^\d+[\d,.]*$', x)),
        'account_number': lambda x: bool(re.match(r'^\d+$', x)),
        'ifsc_code': lambda x: bool(re.match(r'^[A-Za-z]{4}0[A-Za-z0-9]{6}$', x)),
    }

    total_fields = len(validation_rules)
    valid_count = 0

    for field, validator in validation_rules.items():
        value = fields.get(field)
        if value and validator(value):
            valid_count += 1

    score = (valid_count / total_fields) * 100
    return score

def calculate_score(fields):
    return validate_fields(fields)
