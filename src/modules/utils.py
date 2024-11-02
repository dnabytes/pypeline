import os
import sys
from modules.make_pipeline import main as make_pipeline
from modules.replay_pipeline import main as replay_pipeline

def get_pipeline_path():

    def check_file_exists_extension(file_path, file_ext):
        if not os.path.isfile(file_path):
            sys.exit(f'{file_path} not found')
        if not file_path.endswith(file_ext):
            sys.exit(f'{file_path} in wrong file type (has to be a {file_ext} file)')

    if len(sys.argv) < 3 or sys.argv[1] not in ['run', 'make', 'replay']:
        sys.exit(f'usage:\n  pypeline run/make/replay pipeline_file')
    option = sys.argv[1]
    if option == 'run':
        pipeline_file_path = sys.argv[2]
        check_file_exists_extension(pipeline_file_path, '.csv')
        return pipeline_file_path
    if option == 'make':
        pipeline_file_path = sys.argv[2] if sys.argv[2].endswith('.csv') else f'{sys.argv[2]}.csv'
        make_pipeline(pipeline_file_path)
        sys.exit(0)
    if option == 'replay':
        log_file_path = sys.argv[2]
        check_file_exists_extension(log_file_path, '.md')
        replay_pipeline(log_file_path)
        sys.exit(0)

def ask_files_to_delete(files_at_start):
    created_files = [xfile for xfile in os.listdir(os.curdir) if os.path.isfile(xfile) and xfile not in files_at_start]
    if created_files:
        print_w_format('Delete created files?', 'yellow')
        for xfile in created_files:
            if input(f'Delete {xfile}?[n]: ').lower() == 'y':
                os.remove(xfile)

def print_w_format(text, *formats_list):
    formats = {
        'bold': '\x1b[1m',
        'green': '\033[92m',
        'red':  '\033[91m',
        'yellow':  '\033[33m',
        'end': '\x1b[0m'
    }
    print(f'{("").join([formats[format] for format in formats_list])}{text}{formats["end"]}')
