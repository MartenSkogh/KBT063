
'''
According to the lab instructions there will be a certain process to how we structure these calculations

The molecules that I need to calculate are:
  - H2O
  - CH3OH
  - CH2CHOH
  - N2
  - F2

For each of these I need to calculate: 
  - bond strengths (O-H or total X-X for homonuclear diatomic molecules X)
  - bond distance (O-H or X-X for homonuclear diatomic molecules X)
  - bond angles (R-O-H, not applicable to diatomic molecules)
  - Mulliken spin population (on oxygen in OH)
  - Mulliken charge (on oxygen in OH)

Each calculation needs to be repeated with both:
  - HF/Def2-SVP
  - B3LYP/Def2-SVP
'''
import os
from subprocess import Popen 
import itertools


def make_structure_str(mol):
    # Just hardcode this
    structure = []
    if mol == "H":
        structure.append("H1")
    elif mol == "OH":
        structure.append("O1")
        structure.append('H2 O1 1')
    elif mol == "HOH":
        structure.append('O1')
        structure.append('H2 O1 1.20440')
        structure.append('H3 O1 1 H2 120.0')
    elif mol == 'CH3OH':
        structure.append('C1')
        structure.append('O2 C1 1.39826')
        structure.append('H3 C1 1.11160 O2 110.31560')
        structure.append('H4 C1 1.11160 O2 110.31560 H3 237.18507')
        structure.append('H5 C1 1.10942 O2 108.88935 H3 118.59253')
        structure.append('H6 O2 0.99233 C1 105.96624 H3 61.40737')
    elif mol == 'CH2CHOH': 
        structure.append('C1')
        structure.append('C2 C1 1.07000')
        structure.append('O3 C2 1.07000 C1 109.47135')
        structure.append('H4 C1 1.22697 C2 140.46681 O3 28.37927')
        structure.append('H5 C1 1.32123 C2 139.84651 O3 208.37885')
        structure.append('H6 O3 0.91694 C2 144.17850 C1 315.69945')
        structure.append('H7 C2 0.61770 C1 133.19040 O3 193.35237')
    elif mol == 'N2':
        structure.append('N1')
        structure.append('N2 N1 1.99751')
    elif mol == 'F2':
        structure.append('F1')
        structure.append('F2 F1 2.73442')
    else:
        print(f'ERROR: Unknown structure for molecule {mol}!')

    return structure

def make_orca_input(mol, method, prefix='', suffix=''):
    filename = f'{prefix}{mol}_{method}{suffix}'.replace('/','-')
    with open(filename, 'w') as input_file:
        # Write all the lines that we want to write
        pass


def make_calculation_folder(mol, method, prefix='', suffix=''):
    folder_name = f'{prefix}{mol}_{method}{suffix}'.replace('/','-')
    if os.path.exists(folder_name):
        print(f'Path "{folder_name}" already exists')
    else:
        print(f'Making folder: {folder_name}')
        os.makedirs(folder_name)
    return folder_name


def has_oh_bond(mol_str):
    return (mol_str.endswith('OH') and mol_str != 'OH')


molecules = ['H', 'OH', 'HOH', 'CH3OH', 'CH2CHOH', 'N2', 'F2']
methods = ['HF/Def2-SVP', 'B3LYP/Def2-SVP']

n_calcs = len(molecules) * len(methods)
calculations = itertools.product(molecules, methods)

for n, (mol, meth) in enumerate(calculations):
    print(f'\n\nCalculation {n+1} out of {n_calcs}')
    if has_oh_bond(mol):
        print(f'Treating {mol} as a molecule with an OH bond.')
        calc_dir = make_calculation_folder(mol, meth)
        print('Investigating OH bond properties...')
        os.chdir(calc_dir)

    else:
        print(f'Treating {mol} as a molecule without an OH bond.')
        calc_dir = make_calculation_folder(mol, meth)
        print('Investigating bond properties...')
        os.chdir(calc_dir)

    os.chdir('..')


        
