import getpass
import telnetlib

HOST = "192.168.0.1"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"config t\n")
tn.write(b"int lo1\n")
tn.write(b"descri router1\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))