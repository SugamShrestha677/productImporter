# products/services.py
import pandas as pd
from .models import Product

def import_products_from_file(file):
    try:
        # Read file into DataFrame
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.name.endswith(".xls") or file.name.endswith(".xlsx"):
            df = pd.read_excel(file)
        else:
            return {"status": "error", "message": "File format not supported"}

        # Basic check for required columns
        required = ["sku", "name", "price", "quantity"]
        for col in required:
            if col not in df.columns:
                return {"status": "error", "message": f"Missing column: {col}"}

        created = 0
        updated = 0
        errors = []

        for i, row in df.iterrows():
            try:
                sku = str(row["sku"]).strip()
                if not sku:
                    continue  # skip rows without sku

                product, is_created = Product.objects.update_or_create(
                    sku=sku,
                    defaults={
                        "name": row["name"],
                        "description": row["description"] if "description" in df.columns else "",
                        "price": float(row["price"]),
                        "quantity": int(row["quantity"]),
                    },
                )
                if is_created:
                    created += 1
                else:
                    updated += 1
            except Exception as e:
                errors.append(f"Row {i+2}: {e}")

        msg = f"Imported. Created: {created}, Updated: {updated}"
        if errors:
            msg += f". Errors: {len(errors)} rows."

        return {"status": "success", "message": msg}

    except Exception as e:
        return {"status": "error", "message": str(e)}
