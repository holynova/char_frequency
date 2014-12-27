# -*- coding: cp936 -*-
#��Ƶͳ��
import string
import re
def char_freq(file_name,num_of_char):
    txt = open(file_name,"r")
    frq = {}
    delEStr = string.punctuation + ' ' + string.digits  #ASCII �����ţ��ո������   
    delCStr = u"��������&%��#@��{}����������������-��������������"
    while True:
        line = txt.readline().decode('utf-8')
        line = line.encode('utf-8').translate(None,delEStr).decode('utf-8')
        
        for char in delCStr:
            line = line.replace(char,"")
        if len(line) == 0:
            break
        if len(line) >= 6:
            for cnt_word in range(0, len(line)- num_of_char):
                word = line[cnt_word:cnt_word+num_of_char]
                if word in frq:
                    frq[word] += 1
                else:
                    frq[word] = 1
    frq = sorted(frq.iteritems(), key=lambda d:d[1], reverse = True)
    txt.close()
    str_result_name = "%d�ִ�-��Ƶ�������-%s" %(num_of_char,file_name)
    result_file = open(str_result_name,"w")
    cnt = 1
    for key,value in frq:
        str_temp = "%5d %5s %5s\n" %(cnt,key,value)
        result_file.write(str_temp.encode('utf-8'))
        cnt += 1
    #print "�������,�Ѵ���:    " + result_file.tell()

for cnt_char in range(1,5):
    char_freq('�δ�ȫ��.txt',cnt_char)
print u"�������!"
