def analyze_financials(data, company_id):
    pros = []
    cons = []

    # Example values (replace with real API keys)
    roe = data.get("roe", 0)
    sales_growth = data.get("sales_growth", 0)
    dividend = data.get("dividend", 0)
    debt = data.get("debt", 0)

    # PROS
    if roe > 10:
        pros.append(f"Company has good ROE of {roe}%")
    if sales_growth > 10:
        pros.append(f"Company has strong sales growth of {sales_growth}%")
    if dividend > 0:
        pros.append("Company is paying dividend")
    if debt < 1:
        pros.append("Company is almost debt-free")

    # CONS
    if roe < 10:
        cons.append(f"Low ROE of {roe}%")
    if sales_growth < 10:
        cons.append(f"Poor sales growth of {sales_growth}%")
    if dividend == 0:
        cons.append("Company is not paying dividend")

    return pros[:3], cons[:3]
