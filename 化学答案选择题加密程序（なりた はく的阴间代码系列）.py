from random import randint
search={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6 }
key=[]
def key_create(answer):  #每个答案生成专属的密钥
    for i in answer:
        temp1=randint(0,5) #加强复杂性，防止轻松破解
        temp_key=(ord(i)-65)+search[i]+4*temp1
        key.append(temp_key)
def encrypt(answer):  #凯撒加盟
    index_answer=0
    temp_all=''
    for i in answer:
        temp_only=chr((((ord(i)-65)+key[index_answer])%26)+65)
        temp_all+=temp_only
        index_answer+=1
    return temp_all
def change_encrypt(answer,key):  #换位加密
    temp=['' for k in range(len(answer))]
    for i in range(len(answer)):
        index_temp=(i+key)%len(answer)
        temp[index_temp]=answer[i]
    output_temp=''
    for st in temp:
        output_temp+=st
    return output_temp
def unify_all(answer): #格式统一为大写
    temp=''
    for st in answer:
        if 'a'<=st<='z':
            st=chr(ord(st)-97+65)
        temp+=st
    return temp
answer_orignall=input('原本的答案')
answer_orignall=unify_all(answer_orignall)
key_create(answer_orignall)
answer_temp=encrypt(answer_orignall)
for i in range(len(key)): #换位重复加密，密钥采用使用凯撒加密用的生成的全部密钥
    answer_temp=change_encrypt(answer_temp,key[i])
print(answer_temp)
