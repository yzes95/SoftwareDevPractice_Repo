# Production Logging System - README

## Overview

This Python script is designed to simulate and track a production system. It logs production cycles, tracks operator activities, and ensures that operational limits (daily and per cycle) are maintained. Data is stored in CSV format in txt files for tracking and future analysis.Also,since the txt files are in csv format they can be opened using excel for better columnshead to data alignment or
you can just change the files extension in the "dotpyfile.py" to xls instead of txt.

## Features

- Tracks production cycles and working hours.
- Logs operator activities.
- Supports both optimized and full-production modes.
- Ensures maintenance requirements are met before continuing a new cycle.
- Automatically creates and updates log files if they do not exist.
- Provides detailed reporting on production performance.

## Requirements

- Python 3.x
- CSV module (built-in)
- `sys` module (built-in)
- `time` module (built-in)
- `random` module (built-in)

## Usage

### 1. Running the Script

To start the production process, use the following command in your terminal:

```sh
python script.py OpenSesame 
```

- `OpenSesame` is a required argument. Without it, the script will not start.
- If an incorrect argument is provided, an error message will be displayed.
- It is case insenstive

### 2. Operator Login

Once the script starts, you will be prompted to enter your **Operator ID**:

```sh
Enter your ID:
```

- The system validates the ID against the predefined operator records.
- If the ID is correct, you will see a welcome message.
- If the ID is incorrect, you will be prompted to enter it again.
- Current IDs Registered are : (1452,1474,1232,1595)

### 3. Selecting Production Mode

After login, you need to choose a **production mode**:

```sh
Input one of the working modes OP (Optimized) or FP (Full Production):
```

- **Optimized Mode (OP)**: Produces items at a base rate.
- **Full Production Mode (FP)**: Produces at a rate multiplied by a defined ratio.

### 4. Tracking Production Progress

- The script will begin tracking production cycles, operator activity, and working hours.
- Production details will be automatically logged.

### 5. Automatic Log Management

- If log files are missing, the script will **create them automatically**.
- If production limits (daily or per cycle) are exceeded, the system **shuts down and requires maintenance**.

## Log Files

- **total\_production\_log.txt**: Stores cumulative production details.
- **single\_cycle\_log.txt**: Stores details of the current production cycle.

## Key Variables and Functions

Refer to `Variables_Functions_Description.txt` for detailed information about variables and functions used in the script.

## Error Handling

- If a log file is missing or corrupted, it is automatically recreated.
- If incorrect inputs are provided, the system prompts the user again.
- If production limits are exceeded, the system shuts down with a message indicating required maintenance.

## Future Enhancements

- Integration with a database for better data persistence.
- GUI for more user-friendly interaction.
- Advanced analytics and reporting features.

## Author
Yahya Zakaria Elyan - Yehia_mnofeh_1995@hotmail.com

## License
This project is licensed under the Dundee University.

