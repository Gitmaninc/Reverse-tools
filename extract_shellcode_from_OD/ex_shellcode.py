#coding:utf-8
# extract shellcode from OD result
# Usage:
#   copy OD table into shellcode.txt

import os

current_dir = os.getcwd()

def extract_to_str():
    fp = open('shellcode.txt','r')
    sc_list = []
    sc_content = fp.readlines()
    fp.close()
    for i in sc_content:
        sc_list.append(i[14:26].replace('00','')) 
    sc_str = ''.join(sc_list).replace(' ','').replace(':','')
    return sc_str

def format_shellcode(sc_str):	
    op = open('out_sc.txt','a+')
    for i in range(0,len(sc_str)):
        if i == 0:
            op.write('"')
        elif i % 32 == 0:
            op.write('"\n"')
        if i % 2 == 0:
            op.write('\\x') 
            op.write(sc_str[i])
        else:
            op.write(sc_str[i])
    op.write('"')
    op.close()

def direct_shellcode(sc_str):
    op = open('out_sc.txt','a+')
    op.write('\n\n\n')
    for i in range(0,len(sc_str)):
        if i % 2 == 0:
            op.write('\\x') 
            op.write(sc_str[i])
        else:
            op.write(sc_str[i])
    op.close()    

def main():
    sc_str = extract_to_str()
    format_shellcode(sc_str)
    direct_shellcode(sc_str)

if __name__ == '__main__':
    main()



