# 1.hydrogen.py
from pyscf import gto, scf, fci
from logger_fci import init_csv, log_result

# Inicia o CSV se ainda não existir
init_csv()

# Define molécula de H2
mol = gto.Mole()
mol.atom = 'H 0 0 0; H 0 0 0.74'
mol.basis = 'sto-3g'
mol.spin = 0
mol.charge = 0
mol.build()

# Hartree-Fock
mf = scf.RHF(mol)
hf_energy = mf.kernel()

# FCI
cisolver = fci.FCI(mol, mf.mo_coeff)
fci_energy, _ = cisolver.kernel()

# Loga os resultados
log_result("H2", hf_energy, fci_energy)