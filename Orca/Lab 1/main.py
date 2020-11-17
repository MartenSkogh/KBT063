
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
from subprocess import Popen, PIPE
import itertools


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


molecules = ['H', 'HOH', 'HO', 'CH3OH', 'CH3O', 'CH2CHOH', 'CH2CHO', 'N2', 'N', 'F2', 'F']
methods = ['HF/Def2-SVP', 'B3LYP/Def2-SVP']

n_calcs = len(molecules) * len(methods)
calculations = itertools.product(molecules, methods)



for n, (mol, meth) in enumerate(calculations):
    print(f'\n\nCalculation {n+1} out of {n_calcs}')
    if has_oh_bond(mol):
        print(f'Treating {mol} as a molecule with an OH bond.')
        print('Investigating OH bond properties...')
    else:
        print(f'Treating {mol} as a molecule without an OH bond.')
        print('Investigating bond properties...')
    
    os.chdir('Results')
    calc_dir = make_calculation_folder(mol, meth)
    #os.chdir('Inputs')
    #input_filename = make_orca_input(mol, meth, overwrite=True)
    #os.chdir('../' + calc_dir)
    #with open(input_filename.replace('.inp','.out'), 'w') as output_file:
    #    pipe1 = Popen(['/Users/skoghm/Library/Orca401/orca', input_filename], stdout=output_file)
    
    os.chdir('..')
        
