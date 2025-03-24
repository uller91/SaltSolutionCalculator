import calculator_solution_density as csd
from auxiliary_functions import find_value_from_function


def calculator_leak_point_by_N(T_c, V_pore, salt, N_mol): 
    sol_volume_per_g_salt = calculator_solution_volume_per_g_salt(N_mol, T_c, salt)
    m_matrix = find_value_from_function(sol_volume_per_g_salt, lambda m_matrix: V_pore * m_matrix, increment = 0.1, start_value = 0.1)
    return 1/(1+m_matrix) * 100 #dry salt wt.%

def calculator_leak_point_by_wt(T_c, V_pore, salt, wt_percent):
    V_pore_available = V_pore * (100-wt_percent)/wt_percent  #per 1 g of salt
    #print(V_pore_available)
    N_calculated = find_value_from_function(V_pore_available, lambda N: calculator_solution_volume_per_g_salt(N, T_c, salt), increment = 1, start_value = 1)
    return N_calculated

def calculator_solution_volume_per_g_salt(N_mol, T_c, salt):
    salt_solution_density = csd.calculate_salt_solution_density(N_mol, T_c, salt)
    salt_molar_mass = csd.get_salt_molar_mass(salt)
    water_molar_mass = csd.get_water_parameters("molar_mass")
    salt_volume_per_g_salt = (N_mol*water_molar_mass + 1*salt_molar_mass)/salt_molar_mass/salt_solution_density #cm3/g
    return salt_volume_per_g_salt

#print(calculator_solution_volume(4, 30, "cacl2"))
#print(calculator_solution_volume(2, 30, "licl"))
#print(calculator_solution_volume(4, 30, "libr"))
#print(calculator_leak_point_by_N(30, 1.36, "cacl2", 10.5))
#print(calculator_leak_point_by_N(30, 1.05, "cacl2", 14.4))
#print(calculator_leak_point_by_N(30, 1.36, "cacl2", 12))
#print(calculator_leak_point_by_wt(30, 1.36, "cacl2", 40.55))
#print(calculator_leak_point_by_wt(30, 1.05, "cacl2", 28.72))
#print(calculator_leak_point_by_wt(30, 1.36, "cacl2", 37.91))