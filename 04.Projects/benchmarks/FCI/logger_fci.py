# logger_fci.py
import csv
import os

CSV_FILE = "resultados_fci.csv"

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Molecule", "HF Energy (Ha)", "FCI Energy (Ha)", "Comment"])

def log_result(molecule, hf_energy, fci_energy, comment=""):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([molecule, f"{hf_energy:.8f}", f"{fci_energy:.8f}", comment])