import calculator_solution_density as csd
from auxiliary_functions import find_value_from_function


def calculator_leak_point_by_N(T_c, V_pore, salt, N_mol): 
    sol_density = csd.calculate_salt_solution_density(N_mol, T_c, salt)
    salt_molar_mass = csd.get_salt_molar_mass(salt)
    water_molar_mass = csd.get_water_parameters("molar_mass")
    K = sol_density / (1+N_mol*(water_molar_mass/salt_molar_mass))
    wt_p = 1 - 1/(1+K*V_pore)
    return wt_p*100

def calculator_leak_point_by_wt(T_c, V_pore, salt, wt_percent):
    V_pore_available = V_pore * (100-wt_percent)/wt_percent  #per 1 g of salt
    N_calculated = find_value_from_function(V_pore_available, lambda N: calculator_solution_volume_per_g_salt(N, T_c, salt), increment = 1, start_value = 1)
    return N_calculated

def calculator_solution_volume_per_g_salt(N_mol, T_c, salt):
    salt_solution_density = csd.calculate_salt_solution_density(N_mol, T_c, salt)
    salt_molar_mass = csd.get_salt_molar_mass(salt)
    water_molar_mass = csd.get_water_parameters("molar_mass")
    salt_volume_per_g_salt = (N_mol*water_molar_mass + 1*salt_molar_mass)/salt_molar_mass/salt_solution_density #cm3/g
    return salt_volume_per_g_salt


#print(calculator_solution_volume(4,s 30, "libr"))
#print(calculator_leak_point_by_N(30, 1.0, "cacl2", 8))
#print(calculator_leak_point_by_wt(30, 0.4, "cacl2", 15))
#print(calculator_leak_point_by_wt(30, 0.4, "cacl2", 20))