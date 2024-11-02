import os
import sys

def get_commands(log_file_path):
    commands = []
    with open(log_file_path, 'r', encoding='utf-8') as fhandle:
        for line in fhandle:
            if line.startswith('* Command:'):
                commands.append(line[line.find(':')+1:].strip())
    return commands

def main(log_file_path):
    commands = get_commands(log_file_path)
    for command in commands:
        exit_code = os.system(command)
        if exit_code != 0:
            sys.exit(f'An error ocurren running {command}')
