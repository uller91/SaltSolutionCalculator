import os.path
import os

from calculator_salt_content import calculator_leak_point_by_N, calculator_leak_point_by_wt


def run_leak_point_calcualtor_by_wt_and_V(increment_1 = 0.1, increment_2 = 1.0):
    salt = str(input("Enter type of salt (CaCl2, LiCl, LiBr): ")).lower()
    T_c = float(input("Enter temperature of the material in Celcius: "))
    
    initial_V_pore = round(float(input("Enter initial pore volume in cm3/g: ")),2)
    final_V_pore = round(float(input("Enter final pore volume in cm3/g: ")),2)
    if final_V_pore < initial_V_pore:
            raise Exception("final weight pore volume should be bigger than the initial")

    initial_wt = round(float(input("Enter initial salt weight percentage: ")),1)
    final_wt = round(float(input("Enter final salt weight percentage: ")),1)
    if final_wt < initial_wt:
            raise Exception("final weight percentage should be bigger than the initial")

    output_data = []
    V_pore = initial_V_pore
    wt = initial_wt
    while round(V_pore,2) <= final_V_pore:    
        while wt <= final_wt:
            calculated_N = round(calculator_leak_point_by_wt(T_c, V_pore, salt, wt),2)
            output_data.append(f"{round(V_pore,2)}, {wt}, {calculated_N}\n")
            wt += increment_2
        V_pore += increment_1
        wt = initial_wt

    write_data(salt, T_c, output_data, multiple=True)
    repeat_or_abort(3)


def run_leak_point_calcualtor_by_N_and_V(increment_1 = 0.1, increment_2 = 1.0):
    salt = str(input("Enter type of salt (CaCl2, LiCl, LiBr): ")).lower()
    T_c = float(input("Enter temperature of the material in Celcius: "))
    
    initial_V_pore = round(float(input("Enter initial pore volume in cm3/g: ")),2)
    final_V_pore = round(float(input("Enter final pore volume in cm3/g: ")),2)
    if final_V_pore < initial_V_pore:
            raise Exception("final weight pore volume should be bigger than the initial")

    initial_N = round(float(input("Enter initial uptake in mol/mol (>=2 for LiCr and LiBr, >=4 for CaCl2): ")),2)
    final_N = round(float(input("Enter final uptake in mol/mol: ")),2)
    if final_N < initial_N:
        raise Exception("final uptake should be bigger than the initial")

    output_data = []
    V_pore = initial_V_pore
    N = initial_N
    while round(V_pore,2) <= final_V_pore:    
        N = initial_N
        while N <= final_N:
            calculated_wt = round(calculator_leak_point_by_N(T_c, V_pore, salt, N),2)
            output_data.append(f"{V_pore}, {calculated_wt}, {N}\n")
            N += increment_2
        V_pore += increment_1
        N = initial_N

    write_data(salt, T_c, output_data, multiple=True)
    repeat_or_abort(4)


def run_leak_point_calcualtor_by_wt(increment = 1.0):
    salt = str(input("Enter type of salt (CaCl2, LiCl, LiBr): ")).lower()
    T_c = float(input("Enter temperature of the material in Celcius: "))
    V_pore = round(float(input("Enter material pore volume in cm3/g: ")),2)

    initial_wt = round(float(input("Enter initial salt weight percentage: ")),1)
    final_wt = round(float(input("Enter final salt weight percentage: ")),1)
    if final_wt < initial_wt:
            raise Exception("final weight percentage should be bigger than the initial")

    output_data = []
    wt = initial_wt
    while wt <= final_wt:
        calculated_N = round(calculator_leak_point_by_wt(T_c, V_pore, salt, wt),2)
        output_data.append(f"{V_pore}, {wt}, {calculated_N}\n")
        wt += increment

    write_data(salt, T_c, output_data)
    repeat_or_abort(1)
    return


def run_leak_point_calcualtor_by_N(increment = 1.0):
    salt = str(input("Enter type of salt (CaCl2, LiCl, LiBr): ")).lower()
    T_c = float(input("Enter temperature of the material in Celcius: "))
    V_pore = round(float(input("Enter material pore volume in cm3/g: ")),2)

    initial_N = round(float(input("Enter initial uptake in mol/mol (>=2 for LiCr and LiBr, >=4 for CaCl2): ")),2)
    final_N = round(float(input("Enter final uptake in mol/mol: ")),2)
    if final_N < initial_N:
        raise Exception("final uptake should be bigger than the initial")
            
    output_data = []
    N = initial_N
    while N <= final_N:
        calculated_wt = round(calculator_leak_point_by_N(T_c, V_pore, salt, N),2)
        output_data.append(f"{V_pore}, {calculated_wt}, {N}\n")
        N += increment

    write_data(salt, T_c, output_data)
    repeat_or_abort(2)
    return


def write_data(salt, T_c, data_set, multiple=False):
    os.makedirs("calculated", exist_ok=True)

    if not multiple:
        file_path = os.path.join("calculated", f"{salt}_{T_c}.csv")
        if not os.path.isfile(file_path):
            n_f = open(file_path, "w+")
            n_f.write(f"Leak point calculations for {salt} at {T_c} C\n")
            n_f.write("\n")
            n_f.write(f"V pore [cm3/g], wt_p [wt%], N [mol/mol]\n")
        else:
            n_f = open(file_path, "a")
    else:
        i = 1
        file_path = os.path.join("calculated", f"{salt}_{T_c}_{i}.csv")
        while os.path.isfile(file_path):
            i += 1
            file_path = os.path.join("calculated", f"{salt}_{T_c}_{i}.csv")
        n_f = open(file_path, "w+")
        n_f.write(f"Leak point calculations for {salt} at {T_c} C\n")
        n_f.write("\n")
        n_f.write(f"V pore [cm3/g], wt_p [wt%], N [mol/mol]\n")

    for data in data_set:
        n_f.write(data)
        
    n_f.write("\n")
    n_f.close()
    return


def repeat_or_abort(n):
    print("")
    subroutine = input("Repeat (r), Quit (q) or Restart (anything else)? ")
    match subroutine.lower():
        case "r":
            if n == 1:
                run_leak_point_calcualtor_by_wt()
            if n == 2:
                run_leak_point_calcualtor_by_N()
            if n == 3:
                run_leak_point_calcualtor_by_wt_and_V()
            if n == 4:
                run_leak_point_calcualtor_by_N_and_V()
        case "q":
            print("Thank you for using the salt solution density calculatior today!\n")
            exit(0)
        case _:
            main()


def main():
    print("Welcome to the salt solution density calculator. Available subroutines:")
    print("")
    print("1 - Calculate leak point by weight percentage of dry salt in composite (range)")
    print("2 - Calculate leak point by uptake in mol water per mol salt (range)")
    print("3 - Calculate leak point by weight percentage for a range of pore volumes")
    print("4 - Calculate leak point by uptake for a range of pore volumes")
    print("")
    subroutine = input("Enter the desired subroutine (1-2; q - to exit): ")
    print("")

    match subroutine.lower():
        case "1":
            run_leak_point_calcualtor_by_wt()
        case "2":
            run_leak_point_calcualtor_by_N()
        case "3":
            run_leak_point_calcualtor_by_wt_and_V()
        case "4":
            run_leak_point_calcualtor_by_N_and_V()
            return
        case "q":
            print("Thank you for using the sorption calculatior today!\n")
            exit(0)
        case _:
            print("Such subroutine doesn't exist!")
            main()


main()
