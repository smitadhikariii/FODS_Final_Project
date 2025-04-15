import os

# This class handles reading from and writing to files
class FileManager:
    @staticmethod
    def read_file(filename):
        # Read all lines from a file, return empty list if file doesn't exist
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

    @staticmethod
    def write_file(filename, data_lines):
        # Overwrite the file with new lines
        with open(filename, 'w') as file:
            for line in data_lines:
                file.write(line + '\n')

    @staticmethod
    def append_to_file(filename, data_line):
        # Add a single line to the end of a file
        with open(filename, 'a') as file:
            file.write(data_line + '\n')
