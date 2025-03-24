import os.path
import os

from calculator_salt_content import calculator_leak_point_by_N, calculator_leak_point_by_wt


def run_leak_point_calcualtor_by_N():
    T_c = float(input("Enter temperature of the material in Celcius: "))
    V_pore = float(input("Enter material pore volume in cm3/g: "))
    salt = str(input("Enter type of salt (CaCl2, LiCl, LiBr): ")).lower()
    initial_N = float(input("Enter initial salt weight percentage (>2 for LiCr and LiBr, >4 for CaCl2): "))
    final_N = float(input("Enter final salt weight percentage (<30): "))
    
    os.makedirs("calculated", exist_ok=True)
    file_path = os.path.join("calculated", f"{salt}.csv")

    if not os.path.isfile(file_path):
        n_f = open(file_path, "w+")
        n_f.write(f"Leak point calculations for {salt}\n")
        n_f.write("\n")
    else:
        n_f = open(file_path, "a")

    n_f.write(f"T [C], V pore [cm3/g]\n")
    n_f.write(f"{T_c}, {V_pore}\n")
    n_f.write("\n")
    n_f.write(f"wt_p [wt%], N [mol/mol]\n")

    N = initial_N
    while N <= final_N:
        calculated_wt = calculator_leak_point_by_N(T_c, V_pore, salt, N)
        calculated_wt_formatted = format(calculated_wt, ".2f")
        n_f.write(f"{calculated_wt_formatted}, {N}\n")
        N += 1.0

    n_f.write("\n")

    print("Calculations are done...\n")
    n_f.close()
    return


def run_leak_point_calcualtor_by_wt():
    T_c = float(input("Enter temperature of the material in Celcius: "))
    V_pore = float(input("Enter material pore volume in cm3/g: "))
    salt = str(input("Enter type of salt (CaCl2, LiCl, LiBr): ")).lower()
    initial_wt = float(input("Enter initial salt weight percentage (>0): "))
    final_wt = float(input("Enter final salt weight percentage (<60): "))
    
    os.makedirs("calculated", exist_ok=True)
    file_path = os.path.join("calculated", f"{salt}.csv")

    if not os.path.isfile(file_path):
        n_f = open(file_path, "w+")
        n_f.write(f"Leak point calculations for {salt}\n")
        n_f.write("\n")
    else:
        n_f = open(file_path, "a")

    n_f.write(f"T [C], V pore [cm3/g]\n")
    n_f.write(f"{T_c}, {V_pore}\n")
    n_f.write("\n")
    n_f.write(f"wt_p [wt%], N [mol/mol]\n")

    wt = initial_wt
    while wt <= final_wt:
        calculated_N = calculator_leak_point_by_wt(T_c, V_pore, salt, wt)
        calculated_N_formatted = format(calculated_N, ".2f")
        n_f.write(f"{wt}, {calculated_N_formatted}\n")
        wt += 1.0

    n_f.write("\n")

    print("Calculations are done...\n")
    n_f.close()
    return


def main():
    print("Welcome to the salt solution density calculator. Available subroutines:")
    print("")
    print("1 - Calculate leak point by weight percentage of dry salt in composite")
    print("2 - Calculate leak point by uptake in mol water per mol salt")
    print("")
    subroutine = input("Enter the desired subroutine (1-2; q - to exit): ")
    print("")
    
    match subroutine.lower():
        case "1":
            run_leak_point_calcualtor_by_wt()
        case "2":
            run_leak_point_calcualtor_by_N()
        case "q":
            print("Thank you for using the sorption calculatior today!\n")
            exit(0)
        case _:
            print("Such subroutine doesn't exist!")
            main()
    
    
    #T_c = 30
    #V_pore = 1.36
    #salt = "LiCl"
    #wt_p = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    #N = []
    
    #for wt in wt_p:
    #    N.append(calculator_leak_point_by_wt(T_c, V_pore, salt, wt))

    #print(N)


main()
