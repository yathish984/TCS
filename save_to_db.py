from db_config import engine
import pandas as pd

def save_analysis(company_id, pros, cons):
    df = pd.DataFrame([{
        "company_id": company_id,
        "pros": ", ".join(pros),
        "cons": ", ".join(cons)
    }])

    df.to_sql("ml", con=engine, if_exists="append", index=False)
