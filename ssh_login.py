import paramiko
import sys
import os


def ssh_login(ip, username, password):
    ssh_log = paramiko.SSHClient()
    ssh_log.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_log.connect(ip, username=username, password=password)
    return ssh_log


def ssh_command(ssh_log, command):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_log.exec_command(command)
    return ssh_stdout.read()


def ssh_logout(ssh_log):
    ssh_log.close()


if __name__ == '__main__':
    print(os.name)
    if len(sys.argv) < 3:
        print("Usage: python ssh_login.py <host> <username> <password>")
        sys.exit(1)

    ssh = ssh_login(sys.argv[1], sys.argv[2], sys.argv[3])
    print(ssh_command(ssh, "ls -l"))
    ssh_logout(ssh)
    login = True

    while True:
        action = int(input("""
        1. Login
        2. Command
        3. Logout
        """))
        if action == 1 and login:
            print("Already logged in")
        elif action == 1 and not login:
            ssh = ssh_login(sys.argv[1], sys.argv[2], sys.argv[3])
        elif action == 2:
            print(ssh_command(ssh, input("Enter command: ")))
        elif action == 3:
            ssh_logout(ssh)
            break
