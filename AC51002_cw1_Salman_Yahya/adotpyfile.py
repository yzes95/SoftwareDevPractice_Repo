import sys
from time import perf_counter, sleep
import csv

# import pandas as pd
from random import choice


def main():
    # max of hours a single cycle can work before it need maint
    working_hr_limit_per_cycle = 50
    # working hours perday
    working_hr_limit_per_day = 10
    # total_production_log_file_name
    tp_l_fn = "total_production_log.txt"
    # single cycle file
    sc_l_fn = "single_cycle_log.txt"
    # rate of items per min for optimized mode ,default value
    items_produced_permin = 3
    # ratio of full production to optimized
    ratio = 2
    try:
        # taking the start command from the user from the arguments when he run the file as sys arguments
        if len(sys.argv) == 2 and sys.argv[1] == "OpenSesame":
            # here it will return the items produced per min rate
            # and mode where mode is either 0 or ratio value
            mode, modeFP, modeOP = production_rate(mode_selection(), ratio)
            # here is a fnc to determine which operator using the system
            # by returning a list of order of names with status of either 1 or 0 for who
            # is operating [Ahmed,Mohammed,Mostafa,Abd_EL_Rahman]
            operator_names = operator_selection()
            # print(operator_names)
            # commencing into the production process
            # getting the start time of the system per day to start counting/tracking working hours
            process_start_time = perf_counter()

            # scaling the program to match required testing / real life application (avoiding magic numbers)
            scale = (
                1 * 100 * 60 * 60
            )  # which is giving production results per hour ((milisec*10)/(10*mili)INsec/secsINmin/minsINhour)

            print("Checking for problems...")
            # here we shall read the data from the file 1st
            # this fnc check if file exist or not,if yes, it will read it and ...
            # if not it will create it with req headers and data and ...
            # and then it return the data of the last line in form of dict
            (
                Cycle_No,
                Day_No,
                Total_Items_Produced,
                Total_Worked_Hours,
                Items_Produced_OP_Mode,
                Worked_HRS_OP_Mode,
                Items_Produced_FP_Mode,
                Worked_HRS_FP_Mode,
                Items_Produced_By_Ahmed,
                Items_Produced_By_Mohammed,
                Items_Produced_By_Mostafa,
                Items_Produced_By_Abd_EL_Rahman,
            ) = map(int, check_exist_to_read_or_creat_and_read(tp_l_fn).values())
            
            Day_No = int(check_exist_to_read_or_creat_and_read(sc_l_fn).get("Day_No"))
            print("Commencing The Process...")
            print("Let the fun begin 🫰")
            process(
                mode,
                modeFP,
                modeOP,
                ratio,
                tp_l_fn,
                sc_l_fn,
                Cycle_No,
                Day_No,
                scale,
                operator_names,
                working_hr_limit_per_cycle,
                process_start_time,
                items_produced_permin,
                working_hr_limit_per_day,
                Total_Items_Produced,
                Total_Worked_Hours,
                Items_Produced_OP_Mode,
                Worked_HRS_OP_Mode,
                Items_Produced_FP_Mode,
                Worked_HRS_FP_Mode,
                Items_Produced_By_Ahmed,
                Items_Produced_By_Mohammed,
                Items_Produced_By_Mostafa,
                Items_Produced_By_Abd_EL_Rahman,
            )

        else:
            print("wrong password!")
    except IndexError:
        print("Wrong Inputs!")


def operator_selection():
    operators_info = [
        {"name": "Ahmed", "id": 1595},
        {"name": "Mohammed", "id": 1474},
        {"name": "Mostafa", "id": 1232},
        {"name": "Abd_EL_Rahman", "id": 1452},
    ]
    while True:
        try:
            id = int(input("Enter your ID: "))
            for operator in operators_info:
                if id == operator["id"]:
                    welcoming_strs = [
                        f"Welcome {operator["name"]}!",
                        f"Nice to see you again {operator["name"]}!",
                        f"Long time no see { operator["name"]}!",
                    ]
                    print(choice(welcoming_strs))
                    return [
                        operator["name"] == "Ahmed",
                        operator["name"] == "Mohammed",
                        operator["name"] == "Mostafa",
                        operator["name"] == "Abd_EL_Rahman",
                    ]
        except ValueError:
            print("Value Must Be Int")


def mode_selection():
    # wm mean working mode
    while True:
        wm = input(
            "Input one of the working modes OP(Optimized) or FP(Full Production): "
        ).lower()
        if wm == "optimized" or wm == "full production" or wm == "op" or wm == "fp":
            return wm


def production_rate(mode, ratio):
    # lets assume it is 3 items/min for optopmized
    # lets assume it is 3*ratio items/min for full production
    if mode == "optimized" or mode == "op":
        return [1, 0, 1]  # Mode , ModeFP , ModeOP
    else:
        return [1 * ratio, 1 * ratio, 0]


def check_exist_to_read_or_creat_and_read(filename):
    try:
        # here it will open it by default in reading mode
        with open(filename) as file:
            header = csv.DictReader(file)
            header_checker = header.fieldnames
            checking_if_empty = file.read(1)
            if not checking_if_empty:
                raise Exception
            elif header_checker != [
                "Cycle_No",
                "Day_No",
                "Total_Items_Produced",
                "Total_Worked_Hours",
                "Items_Produced_OP_Mode",
                "Worked_HRS_OP_Mode",
                "Items_Produced_FP_Mode",
                "Worked_HRS_FP_Mode",
                "Items_Produced_By_Ahmed",
                "Items_Produced_By_Mohammed",
                "Items_Produced_By_Mostafa",
                "Items_Produced_By_Abd_EL_Rahman",
            ]:
                raise Exception
    except FileNotFoundError:
        print(f"Error: No file founded with name : {filename}!\nCreating New File...\nError Solved...")
        create_files(filename)
    except Exception:
        print(f"Error: The file with name {filename} is empty!\nUpdating The File...\nError Solved...")
        create_files(filename)
    return read(filename)


def create_files(filename):
    with open(filename, "w") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Cycle_No",
                "Day_No",
                "Total_Items_Produced",
                "Total_Worked_Hours",
                "Items_Produced_OP_Mode",
                "Worked_HRS_OP_Mode",
                "Items_Produced_FP_Mode",
                "Worked_HRS_FP_Mode",
                "Items_Produced_By_Ahmed",
                "Items_Produced_By_Mohammed",
                "Items_Produced_By_Mostafa",
                "Items_Produced_By_Abd_EL_Rahman",
            ],
        )
        writer.writeheader()
        # csv files store the data you write as string even if you write as int
        # check the commented lines at fnc end for check
        # thats why mapping have been used in main fnc
        writer.writerow(
            {
                "Cycle_No": 1,
                "Day_No": 1,
                "Total_Items_Produced": 0,
                "Total_Worked_Hours": 0,
                "Items_Produced_OP_Mode": 0,
                "Worked_HRS_OP_Mode": 0,
                "Items_Produced_FP_Mode": 0,
                "Worked_HRS_FP_Mode": 0,
                "Items_Produced_By_Ahmed": 0,
                "Items_Produced_By_Mohammed": 0,
                "Items_Produced_By_Mostafa": 0,
                "Items_Produced_By_Abd_EL_Rahman": 0,
            }
        )
    # with open(filename) as file:
    # reader=csv.DictReader(file)
    # for row in reader:
    # print(type(row["Cycle_No"]))


def read(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        cycle_data = list(reader)
        return cycle_data[-1]


def process(
    mode,
    modeFP,
    modeOP,
    ratio,
    filename,
    filename2,
    Cycle_No,
    Day_No,
    scale,
    operator_names,
    working_hr_limit_per_cycle,
    process_start_time,
    items_produced_permin,
    working_hr_limit_per_day,
    Total_Items_Produced,
    Total_Worked_Hours,
    Items_Produced_OP_Mode,
    Worked_HRS_OP_Mode,
    Items_Produced_FP_Mode,
    Worked_HRS_FP_Mode,
    Items_Produced_By_Ahmed,
    Items_Produced_By_Mohammed,
    Items_Produced_By_Mostafa,
    Items_Produced_By_Abd_EL_Rahman,
):
    # a variable used to store data for comparison
    store_0 = 0.11
    # a variable used to store data for produced items
    Items_Produced = 0
    # a variable used to store data for time passed
    time_passed_in_hrs = 0
    while int(time_passed_in_hrs * 10) <= working_hr_limit_per_day:
        # here it will check time passed
        # and to make it work with respect
        # to Real Time Hourse apply the scele commentted
        time_passed = perf_counter() - process_start_time
        time_passed_in_hrs = round(time_passed, 5)  # // scale
        # print(store_0)
        # print(time_passed_in_hrs)
        if int(time_passed_in_hrs * 10) > int(store_0 * 10):
            # print(int(time_passed_in_hrs*10))
            store_0 = time_passed_in_hrs
            # here it store total items produced at per hour rate
            Items_Produced = items_produced_permin * 60
            Worked_HRS_FP_Mode += 1 * (not modeOP)
            Worked_HRS_OP_Mode += 1 * modeOP
            if (
                (Worked_HRS_FP_Mode * ratio) + Worked_HRS_OP_Mode
            ) <= working_hr_limit_per_cycle:
                Total_Worked_Hours += 1
                Total_Items_Produced += Items_Produced * mode
                Items_Produced_FP_Mode += Items_Produced * modeFP
                Items_Produced_OP_Mode += Items_Produced * modeOP
                Items_Produced_By_Ahmed += Items_Produced * mode * operator_names[0]
                Items_Produced_By_Mohammed += Items_Produced * mode * operator_names[1]
                Items_Produced_By_Mostafa += Items_Produced * mode * operator_names[2]
                Items_Produced_By_Abd_EL_Rahman += (
                    Items_Produced * mode * operator_names[3]
                )

                updatedrow = {
                    "Cycle_No": Cycle_No,
                    "Day_No": Day_No,
                    "Total_Items_Produced": Total_Items_Produced,
                    "Total_Worked_Hours": Total_Worked_Hours,
                    "Items_Produced_OP_Mode": Items_Produced_OP_Mode,
                    "Worked_HRS_OP_Mode": Worked_HRS_OP_Mode,
                    "Items_Produced_FP_Mode": Items_Produced_FP_Mode,
                    "Worked_HRS_FP_Mode": Worked_HRS_FP_Mode,
                    "Items_Produced_By_Ahmed": Items_Produced_By_Ahmed,
                    "Items_Produced_By_Mohammed": Items_Produced_By_Mohammed,
                    "Items_Produced_By_Mostafa": Items_Produced_By_Mostafa,
                    "Items_Produced_By_Abd_EL_Rahman": Items_Produced_By_Abd_EL_Rahman,
                }
                updating_sc(updatedrow, filename2, Day_No)
                updating(updatedrow, filename, Cycle_No)
            else:
                appending(filename, Cycle_No)
                for _ in range(5):
                    print("System is Terminating!!!")
                    sleep(1)
                printing(updatedrow)
                with open(filename2, "w") as file:
                    pass
                sys.exit("Service Required!")
    else:
        appending_sc(filename2, Cycle_No, Day_No)
        sys.exit("Working Hours for the day Finished!")


def printing(updatedrow):
    print()
    print("=" * 60)
    print(f"{'Metric':<35} | {'Value':>10}")
    print("=" * 60)
    # Print table rows
    for header, value in zip(updatedrow.keys(), updatedrow.values()):
        print(f"{header:<35} | {value:>10}")
    print("=" * 60)


def updating(updatedrow, filename, Cycle_No):
    updated_rows = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        # print(fieldnames)
        for row in reader:
            if int(row["Cycle_No"]) == Cycle_No:
                row.update(updatedrow)
            updated_rows.append(row)

    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)


def updating_sc(updatedrow, filename, No):
    updated_rows = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        # print(fieldnames)
        for row in reader:
            if int(row["Day_No"]) == No:
                row.update(updatedrow)
            updated_rows.append(row)

    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)


def appending_sc(filename2, Cycle_No,Day_No):
    nextrow = {
        "Cycle_No": Cycle_No,
        "Day_No": Day_No + 1,
        "Total_Items_Produced": 0,
        "Total_Worked_Hours": 0,
        "Items_Produced_OP_Mode": 0,
        "Worked_HRS_OP_Mode": 0,
        "Items_Produced_FP_Mode": 0,
        "Worked_HRS_FP_Mode": 0,
        "Items_Produced_By_Ahmed": 0,
        "Items_Produced_By_Mohammed": 0,
        "Items_Produced_By_Mostafa": 0,
        "Items_Produced_By_Abd_EL_Rahman": 0,
    }
    with open(filename2, "a") as file:
        appending = csv.DictWriter(file, fieldnames=nextrow.keys())
        appending.writerow(nextrow)


def appending(filename, Cycle_No):
    nextrow = {
        "Cycle_No": Cycle_No + 1,
        "Day_No": 1,
        "Total_Items_Produced": 0,
        "Total_Worked_Hours": 0,
        "Items_Produced_OP_Mode": 0,
        "Worked_HRS_OP_Mode": 0,
        "Items_Produced_FP_Mode": 0,
        "Worked_HRS_FP_Mode": 0,
        "Items_Produced_By_Ahmed": 0,
        "Items_Produced_By_Mohammed": 0,
        "Items_Produced_By_Mostafa": 0,
        "Items_Produced_By_Abd_EL_Rahman": 0,
    }
    with open(filename, "a") as file:
        appending = csv.DictWriter(file, fieldnames=nextrow.keys())
        appending.writerow(nextrow)


if __name__ == "__main__":
    main()
