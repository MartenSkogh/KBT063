
import os
import time
import subprocess
import glob
from pprint import pprint
import numpy as np
from numpy.linalg import norm
import itertools 
import re
import pandas as pd




def run_orca(i_filename, o_filename=''):
    if o_filename == '':
        o_filename = i_filename.replace('.inp', '.out')

    print(f'\nRunning "{i_filename}"')
    p_out = subprocess.run(['orca', i_filename], capture_output=True)
    if p_out.stderr:
        print(p_out.stderr.decode())
    
    
    print(f'Writing to "{o_filename}"')
    with open(o_filename, 'bw') as of:
        of.write(p_out.stdout)


default_search_terms = {'TS': 'Final entropy term',
                        'G': 'Final Gibbs free energy',
                        'G-E(el)': 'G-E(el)',
                        'H': 'Total Enthalpy',
                        'E_therm': 'Total thermal energy',
                        'E_sp': 'FINAL SINGLE POINT ENERGY'}


def parse_orca_output(o_filename, search_terms=None, print_match_lines=False):

    if search_terms == None:
        search_terms = default_search_terms

    terms = {}
    with open(o_filename, 'r') as of:
        for line in of:
            for key in search_terms:
                if search_terms[key] in line:
                    if print_match_lines:
                        print(line.strip())
    
                    p = re.compile(r'[-]?\d+.\d+')
                    matches = p.findall(line)
                    # print(matches)
                    if len(matches) > 0:
                        terms[key] = float(matches[0])

    return terms

def get_scan_energies(o_filename):
    pass

def get_imaginary_modes(o_filename):
    imaginary_modes = []
    with open(o_filename, 'r') as o_file:
        for line in o_file:
            if '***imaginary mode***' in line:
                imaginary_modes.append(line.strip())
    
    return imaginary_modes

    