import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# Configuración
N = 1000
random.seed(42)

diagnoses = ["Diabetes", "Hypertension", "Asthma", "Heart Disease", "Arthritis", "Cancer"]
regions   = ["Northeast", "Midwest", "South", "West"]
genders   = ["M", "F"]

# ✅ Guardar SIEMPRE dentro de la carpeta del proyecto
out_dir = Path("data/raw")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "claims.csv"

def random_date(start_days_ago=365*2, max_stay_days=14):
    admission = datetime.today() - timedelta(days=random.randint(0, start_days_ago))
    discharge = admission + timedelta(days=random.randint(1, max_stay_days))
    return admission.strftime("%Y-%m-%d"), discharge.strftime("%Y-%m-%d")

with open(out_file, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["claim_id","patient_id","age","gender","diagnosis",
                "admission_date","discharge_date","cost","region"])

    for i in range(N):
        claim_id = f"C{100000 + i}"
        patient_id = f"P{random.randint(1000, 1999)}"
        age = random.randint(18, 90)
        gender = random.choice(genders)
        diagnosis = random.choice(diagnoses)
        admission_date, discharge_date = random_date()

        base_cost = {
            "Diabetes": 2500, "Hypertension": 1800, "Asthma": 1600,
            "Heart Disease": 8000, "Arthritis": 2200, "Cancer": 15000
        }[diagnosis]
        cost = base_cost + random.uniform(-0.4, 1.2) * base_cost
        cost = max(200.0, round(cost, 2))
        region = random.choice(regions)

        w.writerow([claim_id, patient_id, age, gender, diagnosis,
                    admission_date, discharge_date, cost, region])

print(f"✅ Generado: {out_file.resolve()} con {N} filas")
