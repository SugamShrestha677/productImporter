# products/services.py
import pandas as pd
from .models import Product

def import_products_from_file(file):
    try:
        # Determine file type and read into a pandas DataFrame
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return {"status": "error", "message": "Unsupported file format."}

        # --- Enhanced Column Validation ---
        required_columns = {'sku', 'name', 'price', 'quantity'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            return {"status": "error", "message": f"Missing required columns: {', '.join(missing)}"}

        created_count = 0
        updated_count = 0
        failed_rows = []

        # Iterate over DataFrame rows
        for index, row in df.iterrows():
            try:
                # --- Enhanced Data Validation ---
                sku = str(row['sku']).strip()
                if not sku:
                    raise ValueError("SKU cannot be empty.")
                
                # Use update_or_create to handle duplication
                _, created = Product.objects.update_or_create(
                    sku=sku,
                    defaults={
                        'name': row['name'],
                        'description': row.get('description', ''),
                        'price': float(row['price']),  # Malformed data will raise ValueError here
                        'quantity': int(row['quantity']), # Malformed data will raise ValueError here
                    }
                )
                if created:
                    created_count += 1
                else:
                    updated_count += 1
            except (ValueError, TypeError) as e:
                # Catch malformed data errors for price/quantity
                failed_rows.append(f"Row {index + 2}: {e} - Data: {row.to_dict()}")

        message = f"Successfully imported data. Created: {created_count}, Updated: {updated_count}."
        if failed_rows:
            message += f" Failed Rows: {len(failed_rows)}. Details: {'; '.join(failed_rows)}"
        
        return {"status": "success", "message": message}

    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {str(e)}"}