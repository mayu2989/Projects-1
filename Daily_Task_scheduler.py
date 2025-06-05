import os,csv,datetime
def create_csv():
    cwd = os.getcwd()
    path = os.path.join(cwd,"task.csv")
    if os.path.exists(path):
        print("Welcome Back")
        print("Data is stored in the following path")
        print("Data File Path:",path)
    else:
        print("Welcome To Task Scheduler")
        fp = open(path,mode='w')
        csv_write = csv.DictWriter(fp,fieldnames=["Task","Date","Time"])
        csv_write.writeheader()
        fp.close()


def task_add():
    try:
        with open("task.csv", mode='a', newline='') as fp:
            csv_write = csv.DictWriter(fp, fieldnames=["Task", "Date", "Time"], lineterminator='\r\n')

            try:
                inputs = int(input("Enter the number of tasks you want to add: "))
            except ValueError:
                print("Error: Please enter a valid integer for the number of tasks.")
                return

            for i in range(inputs):
                print(f"Input {i+1}:")

                try:
                    input_dt = input("Enter the Date and time (dd mm yyyy):")
                    dt = datetime.datetime.strptime(input_dt, "%d %m %Y").date()
                except ValueError:
                    print("Error: Invalid date format. Please enter the date in 'dd mm yyyy' format.")
                    continue

                try:
                    input_ti = input("Enter the Time (12-hour format, hh mm ss):")
                    ti = datetime.datetime.strptime(input_ti, "%I %M %S").time()
                except ValueError:
                    print("Error: Invalid time format. Please enter the time in 'hh mm ss' format.")
                    continue

                task = input("Enter the task:")
                csv_write.writerow({"Task": task, "Date": dt, "Time": ti})
                print("Task added successfully.")

        print("All tasks added successfully.")

    except IOError:
        print("Error: Could not access 'task.csv'. Please check file permissions or path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def display_task():
    with open("task.csv",mode = "r",newline='') as fp:
        csv_read = csv.DictReader(fp)
        for i in csv_read:
            print(i)

def running_task():
    with open("task.csv", mode="r", newline='') as fp:
        csv_read = csv.DictReader(fp)
        current_time = datetime.datetime.now()

        for i in csv_read:
            i_csv_datetime = datetime.datetime.strptime(i["Date"] + " " + i["Time"], "%Y-%m-%d %H:%M:%S")
            
            if i_csv_datetime > current_time:
                print(i)



def delete_past_tasks():
    current_time = datetime.datetime.now()
    updated_tasks = []

    
    with open("task.csv", mode="r", newline='') as fp:
        csv_read = csv.DictReader(fp)
        fieldnames = csv_read.fieldnames  

        for i in csv_read:
            i_csv_datetime = datetime.datetime.strptime(i["Date"] + " " + i["Time"], "%Y-%m-%d %H:%M:%S")
            
            if i_csv_datetime > current_time:
                updated_tasks.append(i)  

    
    with open("task.csv", mode="w", newline='') as fp:
        csv_write = csv.DictWriter(fp, fieldnames=["Task","Date","Time"])
        csv_write.writeheader()
        csv_write.writerows(updated_tasks)  

    print("Past tasks have been deleted successfully!")

create_csv()
print("List of Operation\n1)Add task - add_task\n2)Delete outdated task - del_out\n3)Display all task - disp_task\n4)Display running task - disp_run\n5)Exit from program - exit")
while True:
    input_operation = input("Enter the Operation you want to perform:")
    match input_operation:
        case "add_task":
            task_add()
        case "del_out":
            delete_past_tasks()
        case "disp_task":
            display_task()
        case "disp_run":
            running_task()
        case "exit":
            break
        case _:
            print("Invalid operation")
        






    
    
        
