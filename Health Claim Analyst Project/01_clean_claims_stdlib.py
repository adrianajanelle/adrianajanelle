import csv, os
from datetime import datetime

RAW = "data/raw/claims.csv"
CLEAN = "data/clean/claims_clean.csv"
os.makedirs("data/clean", exist_ok=True)

# Parámetros de validación
MIN_AGE, MAX_AGE = 18, 100
VALID_GENDERS = {"M", "F"}
VALID_REGIONS = {"Northeast", "Midwest", "South", "West"}

def parse_date(s): 
    return datetime.strptime(s, "%Y-%m-%d")

def month_str(dt: datetime) -> str:
    return dt.strftime("%Y-%m")

def age_band(age: int) -> str:
    if age < 30: return "<30"
    if age <= 44: return "30-44"
    if age <= 59: return "45-59"
    if age <= 74: return "60-74"
    return "75+"

seen_claims = set()
stats = {
    "in_rows": 0,
    "kept": 0,
    "dup_claim_id": 0,
    "bad_age": 0,
    "bad_gender": 0,
    "bad_region": 0,
    "bad_cost_or_dates": 0,
    "parse_errors": 0
}

with open(RAW, newline="", encoding="utf-8") as fin, \
     open(CLEAN, "w", newline="", encoding="utf-8") as fout:

    reader = csv.DictReader(fin)
    fieldnames = [
        "claim_id","patient_id","age","gender","diagnosis",
        "admission_date","discharge_date","cost","region",
        "los_days","cost_per_day","month","age_band"
    ]
    writer = csv.DictWriter(fout, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        stats["in_rows"] += 1

        # Duplicado
        cid = (row.get("claim_id") or "").strip()
        if not cid or cid in seen_claims:
            stats["dup_claim_id"] += 1
            continue
        seen_claims.add(cid)

        # Parseos y campos requeridos
        try:
            age = int(row["age"])
            cost = float(row["cost"])
            ad = parse_date(row["admission_date"])
            dc = parse_date(row["discharge_date"])
        except Exception:
            stats["parse_errors"] += 1
            continue

        # Validaciones
        if not (MIN_AGE <= age <= MAX_AGE):
            stats["bad_age"] += 1
            continue

        gender = (row.get("gender") or "").strip()
        if gender not in VALID_GENDERS:
            stats["bad_gender"] += 1
            continue

        region = (row.get("region") or "").strip()
        if region not in VALID_REGIONS:
            stats["bad_region"] += 1
            continue

        if cost <= 0 or dc < ad:
            stats["bad_cost_or_dates"] += 1
            continue

        # Derivadas
        los = (dc - ad).days or 1
        cpd = round(cost / los, 2)
        mon = month_str(ad)
        band = age_band(age)

        # Escribir limpio
        writer.writerow({
            "claim_id": cid,
            "patient_id": (row.get("patient_id") or "").strip(),
            "age": age,
            "gender": gender,
            "diagnosis": (row.get("diagnosis") or "").strip(),
            "admission_date": ad.strftime("%Y-%m-%d"),
            "discharge_date": dc.strftime("%Y-%m-%d"),
            "cost": round(cost, 2),
            "region": region,
            "los_days": los,
            "cost_per_day": cpd,
            "month": mon,
            "age_band": band
        })
        stats["kept"] += 1

# Reporte de calidad
print("✅ Limpieza completa →", CLEAN)
print("--- Data Quality Report ---")
for k, v in stats.items():
    print(f"{k}: {v}")
