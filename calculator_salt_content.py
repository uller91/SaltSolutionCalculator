import calculator_solution_density as csd

#def calculator_leak_point(T_c, V_pore, salt, wt_percent):
#    salt_solution_density = calculate_salt_solution_density()
#    return


def calculator_solution_volume(N_mol, T_c, salt):
    salt_solution_density = csd.calculate_salt_solution_density(N_mol, T_c, salt)
    salt_molar_mass = csd.get_salt_molar_mass(salt)
    water_molar_mass = csd.get_water_parameters("molar_mass")
    salt_volume_per_g_salt = (N_mol*water_molar_mass + 1*salt_molar_mass)/salt_molar_mass/salt_solution_density #cm3/g
    return salt_volume_per_g_salt

#print(calculator_solution_volume(4, 30, "cacl2"))
#print(calculator_solution_volume(2, 30, "licl"))
#print(calculator_solution_volume(4, 30, "libr"))