def get_new_step():
    step_name = input('Step name: ')
    step_command = input('Command: ')
    return step_name, step_command

def main(pipeline_file_path):
    print('Making new pipeline.\nUse % before a param so it can be changed when running the pipeline.')
    steps = []
    while True:
        steps.append((',').join(get_new_step()))
        if input('Add new step?[y]: ') == 'n':
            break
    with open(pipeline_file_path, 'w', encoding='utf-8') as fhandle:
        fhandle.write(('\n').join(steps))
