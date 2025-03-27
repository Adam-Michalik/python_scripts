# python_scripts
This repository contains various Python scripts that have been created to solve a variety of tasks, e.g. log analysis.

## Scripts in repositoriy
### Read_log_file.py
A script for analyzing log files on Windows/Linux, allowing filtering log type and occurrences of a given phrase.<br>Usage (parameters not obligatory):<br>
```
python Read_log_file.py <file_path> [log_type] [phrase] [number_of_last_messages]
```
The source code was generated by ChatGPT.

### Count_lines.py
A script for counting lines in a text file (e.g., a log file). If a phrase is provided as a parameter, only lines containing the phrase will be counted.<br>Usage (parameter not obligatory):<br>
```
python Count_lines.py <file_path> [phrase]
```
 The code was written by me based on the code of the file Read_log_file.py

## How to run
To run the scripts, make sure you have Python installed. You can do this by downloading it from the official website: https://www.python.org/downloads/<br>
Download the file from repository. You can run it in Windows command line, PowerShell or Linux shell (e.g. Bash).
