import pandas as pd
from fetch_data import fetch_company_data
from ml_analysis import analyze_financials
from save_to_db import save_analysis

# Load company list
companies = pd.read_csv("companies.csv")



for company_id in companies["CompanyID"]:
    print(f"\nAnalyzing {company_id}...")

    data = fetch_company_data(company_id)

    if data:
        pros, cons = analyze_financials(data, company_id)

        print("PROS:")
        for p in pros:
            print("-", p)

        print("CONS:")
        for c in cons:
            print("-", c)

        save_analysis(company_id, pros, cons)

print("\n✅ Analysis completed!")
