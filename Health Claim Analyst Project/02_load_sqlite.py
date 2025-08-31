import sqlite3, csv

DB = "claims.db"
CLEAN = "data/clean/claims_clean.csv"

conn = sqlite3.connect(DB)
cur = conn.cursor()

# 1) Crear tabla 
cur.executescript("""
DROP TABLE IF EXISTS claims;
CREATE TABLE claims (
  claim_id TEXT PRIMARY KEY,
  patient_id TEXT,
  age INTEGER,
  gender TEXT,
  diagnosis TEXT,
  admission_date TEXT,   -- ISO yyyy-mm-dd
  discharge_date TEXT,   -- ISO yyyy-mm-dd
  cost REAL,
  region TEXT,
  los_days INTEGER,
  cost_per_day REAL,
  month TEXT,
  age_band TEXT
);
""")

# 2) Insertar filas desde el CSV limpio
with open(CLEAN, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = [
        (row["claim_id"], row["patient_id"], int(row["age"]), row["gender"],
         row["diagnosis"], row["admission_date"], row["discharge_date"],
         float(row["cost"]), row["region"], int(row["los_days"]),
         float(row["cost_per_day"]), row["month"], row["age_band"])
        for row in r
    ]

cur.executemany("""
INSERT INTO claims (
  claim_id, patient_id, age, gender, diagnosis,
  admission_date, discharge_date, cost, region,
  los_days, cost_per_day, month, age_band
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", rows)

conn.commit()
print("✅ cargado → claims.db (tabla claims)")

# 3) KPIs  para validar
checks = [
    ("Total cost",        "SELECT ROUND(SUM(cost),2) FROM claims"),
    ("Avg cost",          "SELECT ROUND(AVG(cost),2) FROM claims"),
    ("Avg LOS (days)",    "SELECT ROUND(AVG(los_days),2) FROM claims"),
    ("Claims count",      "SELECT COUNT(*) FROM claims"),
]
print("\nKPIs rápidos:")
for label, q in checks:
    cur.execute(q)
    print(f"- {label}: {cur.fetchone()[0]}")

conn.close()
