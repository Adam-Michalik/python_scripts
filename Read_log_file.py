
import sys

def read_file(filename, log_type=None, keyword=None, last_n=None):

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines() # Reading all lines to the variable 'lines'

        # Filtering by log type (ERROR, WARNING, INFO)
        if log_type:
            lines = [line for line in lines if log_type.upper() in line]

        # Phrase searching
        if keyword:
            lines = [line for line in lines if keyword.lower() in line.lower()]

        # Displaying last n messages
        if last_n:
            lines = lines[-last_n:]

        # Displaying result
        for line in lines:
            print(line.strip())

    except FileNotFoundError:
        print(f"File '{filename}' does not exist!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Read_log_file.py <file_path> [log_type] [phrase] [number of messages]")
    else:
        filename = sys.argv[1]
        log_type = sys.argv[2] if len(sys.argv) > 2 else None
        keyword = sys.argv[3] if len(sys.argv) > 3 else None
        last_n = int(sys.argv[4]) if len(sys.argv) > 4 else None

        read_file(filename, log_type, keyword, last_n)