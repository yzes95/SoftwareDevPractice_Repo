#we need to define working hours count
#we need to define amount of items produced per min per hr
#we need to define max working hr limit
#we need to define the working mode once the working day commence
    #for now it cant be changed
import sys
from time import perf_counter,sleep
import csv

def main():
    #max of hours a single cycle can work before it need maint
    working_hr_limit = 1850
    #working hours perday
    working_hr_per_day = 10
    #total operating hr var to compare it with working_hr_limit
    t_operating_hrs = 0
    try:    
        #taking the start command from the user
        if len(sys.argv) == 3 and sys.argv[1] == "OpenSesame":
            items_produced_permin,mode = production_rate(mode_selection())
            #commencing into the production process
            #getting the start time of the system per day to start counting/tracking working hours
            process_start_time = perf_counter()
            #scaling the program to match required testing / real life application (avoiding magic numbers)
            scale = 1*60*60 #which is giving production results per hour (sec*secsinmin*minsinhour)
            #a variable used to store data for comparison
            store_0 = 0
            #intiating the amount of items produced
            items_produced_perhr = 0
            match mode:
                case "full production":
                    pass
                case "optomized":
                    while t_operating_hrs <= working_hr_limit:
                        #here it will check time passed with respect to scale decided
                        time_passed = (perf_counter() - process_start_time)*scale
                        time_passed_in_hrs = int(time_passed//scale)
                        if time_passed_in_hrs > store_0:
                            store_0 = time_passed_in_hrs
                            items_produced_perhr += (items_produced_permin*60)*time_passed_in_hrs
                        sleep(0)
                        t_operating_hrs+=time_passed_in_hrs
                        #here even if the file doesnt exist using this command will create the file and append into it
                        with open("production_log_since_commencing.txt", "a") as file: 
                            ...
                        if time_passed_in_hrs > working_hr_per_day:
                            sys.exit("Working Hours for the day Finished!")
                    else:
                        ...
                        sys.exit("Service Required!")
        else:
            print("wrong password!")
    except IndexError:
        print("Wrong Inputs!")


def checking_HR_limit_Pday():
    pass


def mode_selection():
    #wm mean working mode
    while True :
        wm = input("Input one of the working modes (Optomized/Full Production): ").lower()
        if wm == "optomized" or wm == "full production":
            return wm 

      
def production_rate(mode):
    #lets assume it is 10 items/min for optopmized
    #lets assume it is 20 items/min for full production
    if mode == "optomized":
        return [3, mode]
    else:
        return [6, mode]

def check_if_file_existornot():
    try:
        with open("production_log_since_commencing.txt") as file:
            writer= csv.DictReader(file)
    except FileNotFoundError:
        with open("production_log_since_commencing.txt","a") as file:
            writer= csv.DictWriter(file, fieldnames=["Cycle_No", "Total_Items_Produced", "Total_Working_Hours", \
                                                     "Items_Produced_OP_Mode", "Working_HRS_OP_Mode", \
                                                     "Items_Produced_FP_Mode", "Working_HRS_FP_Mode"])
            #later we will add operator name and number of products producded by each operator
            writer.writeheader()


    

if __name__ == "__main__":
    main()