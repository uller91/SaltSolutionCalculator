import math

# CaCl2 and LiCl - M.R. Conde, Int.J.Therm.Sc., 2003
# LiBr - J. Patek, J. Klomfar, Int.J.Ref., 2006 - here the water denstity at saturetion from Conde is used instead of presented in the sake of consistensy

global T_water_crit 
global ro_water_crit
global M_mol_water
M_mol_water = 18.0146 #g/mol
T_water_crit = 647.096 #K
ro_water_crit = 322 #kg/m3

def get_water_parameters(parameter):
    match parameter.lower():
        case "molar_mass":
            return 18.0146 #g/mol
        case "T_crit":
            return 647.096 #K
        case "ro_crit":
            return 322 #kg/m3

def get_salt_molar_mass(salt):
    match salt.lower():
        case "cacl2":
            return 110.98 #g/mol
        case "licl":
            return 42.39
        case "libr":
            return 86.845
        case _:
            raise Exception("wrong salt request!")


def calcualate_water_density(T_c): #C
    T_k = T_c + 273.15
    theta = T_k / T_water_crit
    tau = 1 - theta
    
    B_i = [1.993771843, 1.0985211604, -0.5094492996, -1.761912427, -44.9005480267, -723692.2618632]
    tau_pow = [1/3, 2/3, 5/3, 16/3, 43/3, 110/3]
    
    ro_water = ro_water_crit
    for i in range(6):
        ro_water += ro_water_crit * B_i[i]*math.pow(tau,(tau_pow[i]))

    return ro_water #kg/m3


def calculate_salt_solution_density(N_mol, T_c, salt):
    match salt.lower():
        case "cacl2" | "licl":
            return calculate_salt_solutiion_density_CaCl2_LiCl(N_mol, T_c, salt)
        case "libr":
            return calculate_salt_solutiion_density_LiBr(N_mol, T_c)
        case _:
            raise Exception("wrong salt request!")


def calculate_salt_solutiion_density_CaCl2_LiCl(N_mol, T_c, salt): 
    # works for CaCl2 for N >= 4 and for LiCl for N >= 2
    # salt coefficients:
    ro_i = []

    if salt.lower() == "cacl2":
        ro_i = [0.836014, -0.4363, 0.105642]
    elif salt.lower() == "licl":
        ro_i = [0.540966, -0.303792, 0.100791]
    else:
        raise Exception("wrong salt request!")

    M_mol = get_salt_molar_mass(salt)
    salt_omega = M_mol/(M_mol + N_mol * M_mol_water) # wt.% salt in the salt/water solution
    ro_water = calcualate_water_density(T_c)
    
    ro_salt_sol = ro_water #kg/m3
    for i in range(3):
        ro_salt_sol += ro_water * ro_i[i]*math.pow((salt_omega/(1-salt_omega)),i+1) 

    return ro_salt_sol/1000 #g/cm3


def calculate_salt_solutiion_density_LiBr(N_mol, T_c):
    T_k = T_c + 273.15
    theta = T_k / T_water_crit
    M_mol = get_salt_molar_mass("libr")
    t_i = [0, 6]
    a_i = [1.746, 4.709]

    salt_molar_ratio = 1/(1 + N_mol)
    ro_salt_sol = (1-salt_molar_ratio) * calcualate_water_density(T_c) * 1000/M_mol_water #mol/m3
    for i in range(2):
        ro_salt_sol += ro_water_crit * 1000/M_mol_water * (a_i[i]*salt_molar_ratio*math.pow(theta, t_i[i]))
    return ro_salt_sol * (salt_molar_ratio*M_mol+(1-salt_molar_ratio)*M_mol_water)/1000/1000


#print(calcualate_water_density(30))
#print(calculate_salt_solution_density(4,30,"cacl2"))
#print(calculate_salt_solutiion_density_CaCl2_LiCl(4,30,"cacl2"))
#print(calculate_salt_solution_density(2,30,"licl"))
#print(calculate_salt_solution_density(2,30,"libr"))