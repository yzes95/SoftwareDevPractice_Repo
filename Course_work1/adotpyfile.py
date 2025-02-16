# we need to define working hours count
# we need to define amount of items produced per min per hr
# we need to define max working hr limit
# we need to define the working mode once the working day commence
# for now it cant be changed
import sys
from time import perf_counter, sleep
import csv
import pandas as pd


def main():
    # max of hours a single cycle can work before it need maint
    working_hr_limit_per_cycle = 1850
    # working hours perday
    working_hr_limit_per_day = 10
    # total_production_log_file_name
    tp_l_fn = "total_production_log.txt"
    # rate of items per min for optimized mode ,default value
    items_produced_permin = 3
    # ratio of full production to optimized
    ratio = 2
    try:
        # taking the start command from the user
        if len(sys.argv) == 2 and sys.argv[1] == "OpenSesame":
            # here it will return the items produced per min rate
            # and mode where mode is either 0 or ratio value
            modeFP, modeOP = production_rate(mode_selection(), ratio)

            # commencing into the production process
            # getting the start time of the system per day to start counting/tracking working hours
            process_start_time = perf_counter()

            # scaling the program to match required testing / real life application (avoiding magic numbers)
            scale = (
                1 * 60 * 60
            )  # which is giving production results per hour (sec*secsinmin*minsinhour)

            # here we shall read the data from the file 1st
            # this fnc check if file exist or not,if yes, it will read it and ...
            # if not it will create it with req headers and data and ...
            # and then it return the data of the last line in form of dict
            (
                Cycle_No,
                Total_Items_Produced,
                Total_Worked_Hours,
                Items_Produced_OP_Mode,
                Worked_HRS_OP_Mode,
                Items_Produced_FP_Mode,
                Worked_HRS_FP_Mode,
            ) = check_exist_to_read_or_creat_and_read(tp_l_fn).values()

            process(
                modeFP,
                modeOP,
                ratio,
                tp_l_fn,
                Cycle_No,
                scale,
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
            )

        else:
            print("wrong password!")
    except IndexError:
        print("Wrong Inputs!")


def mode_selection():
    # wm mean working mode
    while True:
        wm = input(
            "Input one of the working modes (Optimized/Full Production): "
        ).lower()
        if wm == "optimized" or wm == "full production":
            return wm


def production_rate(mode, ratio):
    # lets assume it is 3 items/min for optopmized
    # lets assume it is 3*ratio items/min for full production
    if mode == "optimized":
        return [0, 1]
    else:
        return [1 * ratio, 0]


def check_exist_to_read_or_creat_and_read(filename):
    try:
        # here it will open it by default in reading mode
        with open(filename) as file:
            pass
    except FileNotFoundError:
        create_total_production_file(filename)
    return read(filename)


def create_total_production_file(filename):
    with open(filename, "a") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Cycle_No",
                "Total_Items_Produced",
                "Total_Worked_Hours",
                "Items_Produced_OP_Mode",
                "Worked_HRS_OP_Mode",
                "Items_Produced_FP_Mode",
                "Worked_HRS_FP_Mode",
            ],
        )
        # later we will add operator name and number of products producded by each operator
        writer.writeheader()
        #since csv files store the data your write as string even if you write as int
        writer.writerow(
            {
                "Cycle_No": 1,
                "Total_Items_Produced": 0,
                "Total_Worked_Hours": 0,
                "Items_Produced_OP_Mode": 0,
                "Worked_HRS_OP_Mode": 0,
                "Items_Produced_FP_Mode": 0,
                "Worked_HRS_FP_Mode": 0,
            }
        )
        print(type(writer["Cycle_No"]))


def read(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        cycle_data = list(reader)
        return cycle_data[-1]


def process(
    modeFP,
    modeOP,
    ratio,
    filename,
    Cycle_No,
    scale,
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
):
    # a variable used to store data for comparison
    store_0 = 0
    Items_Produced = 0
    while (
        (Worked_HRS_FP_Mode * ratio) + Worked_HRS_OP_Mode
    ) <= working_hr_limit_per_cycle:
        # here it will check time passed with respect to scale decided
        time_passed = (perf_counter() - process_start_time) * scale
        time_passed_in_hrs = int(time_passed // scale)
        if time_passed_in_hrs > store_0:
            store_0 = time_passed_in_hrs
            # here it store total items produced at per hour rate
            Items_Produced += (items_produced_permin * 60) * time_passed_in_hrs
        sleep(0)
        time_passed_in_hrs += time_passed_in_hrs
        if time_passed_in_hrs > working_hr_limit_per_day:
            Total_Worked_Hours += time_passed_in_hrs
            Total_Items_Produced += Items_Produced
            Worked_HRS_FP_Mode += time_passed_in_hrs * modeFP
            Worked_HRS_OP_Mode += time_passed_in_hrs * modeOP
            Items_Produced_FP_Mode += Items_Produced * modeFP
            Items_Produced_OP_Mode += Items_Produced * modeOP
            updating = pd.read_csv(filename)
            updating.loc[
                updating["Cycle_No"] == Cycle_No,
                [
                    "Total_Items_Produced",
                    "Total_Worked_Hours",
                    "Items_Produced_OP_Mode",
                    "Worked_HRS_OP_Mode",
                    "Items_Produced_FP_Mode",
                    "Worked_HRS_FP_Mode",
                ],
            ] = [
                Total_Items_Produced,
                Total_Worked_Hours,
                Items_Produced_OP_Mode,
                Worked_HRS_OP_Mode,
                Items_Produced_FP_Mode,
                Worked_HRS_FP_Mode,
            ]
            sys.exit("Working Hours for the day Finished!")
    else:
        ...
        sys.exit("Service Required!")


if __name__ == "__main__":
    main()
