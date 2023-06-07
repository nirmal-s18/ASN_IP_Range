import os
from subprocess import PIPE, Popen
string1 = 'YOUTUBE'


def write_to_file(content, IPv):
    text_file = open("IP_Results/" + string1 + "_" + IPv, "w")
    text_file.write(content)
    text_file.close()


def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


# opening a text file
file1 = open("ASN_List.txt", "r")

# setting flag and index to 0
flag = 0
index = 0
res_string = ""

# Loop through the file line by line
for line in file1:
    index += 1

    # checking string is present in line or not
    if string1 in line:
        #print(line)
        res_string += line

# closing text file
file1.close()

# Extracting ASN separately
print(res_string)
asn_list = ""

for line in res_string.splitlines():
    #print(type(line))
    #print(line)
    temp = line.split(" ",1)
    asn_list += temp[0] + "\n"


#print(asn_list)
content = ""
for line in asn_list.splitlines():
    print(line)
    temp = cmdline("whois -h whois.radb.net -- -i origin -T route "+ line + " | grep route:")
    content += str(temp) + "\n"


write_to_file(content, "IPv4")


content = ""
for line in asn_list.splitlines():
    print(line)
    temp = cmdline("whois -h whois.radb.net -- -i origin -T route6 "+ line + " | grep route6:")
    content += str(temp) + "\n"


write_to_file(content, "IPv6")







temp = cmdline("whois -h whois.radb.net -- -i origin -T route AS32934 | grep route:")
print(type(temp))