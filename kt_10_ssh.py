# Python - SSH
import paramiko
import os

# Define the server and credentials
# Replace with the actual server IP or hostname
hostname = '10.1.1.1'
# Default SSH port
port = 22
# Replace with your SSH username
username = 'admin'
# Replace with your SSH password
password = '******'

# Create an SSH client instance
client = paramiko.SSHClient()

# Automatically add the server's host key (disable this for more security)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.load_system_host_keys()
# client.load_host_keys(os.path.expanduser("~/.ssh/known_hosts"))

try:
    # Connect to the remote server
    # client.connect(hostname, port=port, username=username, password=password)
    client.connect(hostname, port=port, username=username, password=password, timeout=60)
    # client.get_transport().set_keepalive(60)
    transport = client.get_transport()
    transport.set_keepalive(3000)

    # Execute the 'hostnamectl' command
    stdin, stdout, stderr = client.exec_command('pwd && ls -lrt && hostnamectl')

    # Get the output and error (if any)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    sftp_obj = paramiko.SFTPClient.from_transport(transport)
    """ File name: /etc/ssh/sshd_config
    
    PermitRootLogin yes
    # override default of no subsystems
    Subsystem       sftp    /usr/lib/openssh/sftp-server
    """
    # Download
    filepath = "/home/muthu/ReadMe_NDA.txt"
    local_path = os.getcwd()
    sftp_obj.get(filepath, local_path + "\\ReadMe_NDA.txt")
    # Upload
    filepath = "/home/muthu/testfile.txt"
    local_path = os.getcwd()
    sftp_obj.put(local_path + "\\example.txt", filepath)

    # Print the output or errors
    if output:
        print(f"SFTP obj: {sftp_obj}")
        print("Output:\n", output)

        """
        Output:
        SFTP obj: <paramiko.sftp_client.SFTPClient object at 0x0000019CFCF44A90>
        /root
        total 8
        drwx------ 3 root root 4096 May 15  2024 snap
        drwxr-xr-x 4 root root 4096 Nov 18 11:53 pts-automation-tool
         Static hostname: automation-gitea-clone
               Icon name: computer-vm
                 Chassis: vm
              Machine ID: 0927fedab6b14861a70d14fdad78498e
                 Boot ID: 797c13f5c01842a2b350def6ea40c4c2
          Virtualization: vmware
        Operating System: Ubuntu 22.04.4 LTS
                  Kernel: Linux 5.15.0-122-generic
            Architecture: x86-64
        """
    if error:
        print("Error:\n", error)

finally:
    # Close the SSH connection
    client.close()
