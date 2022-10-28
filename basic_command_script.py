def run_command_subprocess(commands):
    import subprocess
    print('------------------SUBPROCESS------------------')
    for com in commands:
        run = subprocess.run(com, shell=True, check=True)
        print(run.stdout)
        print(run.stderr)
    print('------------------SUBPROCESS ENDS------------------')


def run_command_os(commands):
    import os
    print('------------------OS------------------')
    for com in commands:
        run = os.system(com)
        print(run)
    print('------------------OS ENDS------------------')


# Run a command
if __name__ == '__main__':
    command_list = []
    first_command = input('Enter the first command: ')
    command_list.append(first_command)
    while True:
        command = input('Enter the next command: ')
        if command == 'end':
            break
        command_list.append(command)
    print(command_list)
    run_command_subprocess(command_list)
    print('------------------')
    print('------------------')
    run_command_os(command_list)
