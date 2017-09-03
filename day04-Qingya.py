# -*- coding: utf-8 -*-

import codecs
import os

#1. 读取文件
#['aa', 'aaa-bbb-sds'] => ['aa', 'aaa', 'bbb', 'sds']
def word_split(words):
    new_list = []
    for word in words:
        if '-' not in word:
            new_list.append(word)
        else:
            lst = word.split('-')
            new_list.extend(lst)
    return new_list


def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8") #打开文件
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ") #用空格分割
        words = word_split(words) #用-分割
        word_list.extend(words)
    return word_list

def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

#读取多文件里的单词
def read_files(file_paths):
    final_words = []
    for path in file_paths:
        final_words.extend(read_file(path))
    return final_words


#2.获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):
    word_list = []
    for word in words:
        wd = format_word(word)
        if wd:
            word_list.append(wd)
    return word_list

#3. 统计单词数目
# {'aa':4, 'bb':1}
def statictcs_words(words):
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    #排序
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return sorted_dict

#4.输出成csv
def print_to_csv(volcaulay_list, to_file_path):
    nfile = open(to_file_path,'w+')
    for val in volcaulay_list:
        s=''
        for i in xrange(0,len(val)):
            if i==0:
                s=val[i]
            else:
                s=s+","+str(val[i])
        nfile.write(s+"\n")
    nfile.close()

#统计单词所占百分比
def words_rate(word_list,total_num):
    word_list_rate=[]
    for word in word_list:
        num = word[1]
        word_rate = (float(num)/total_num)*100
        word_list_rate.append([word[0], num, word_rate])
    return word_list_rate

#输出固定词频的单词
def words_list_split(word_list_rate,start_and_end):
    word_list_split=[]
    for val in word_list_rate:
        num=val[2]
        if num<start_and_end[1]*100 and num>start_and_end[0]*100:
            word_list_split.append(val)
    return word_list_split



def main():
    #是否输出固定词频的单词表
    fix_frequency= True
    start_and_end = [0.01, 0.7]  # 截取这一部分的单词

    #1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    #2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' %(len(f_words))
    
    #3. 统计单词和排序
    word_list = statictcs_words(f_words)


    #4. 输出文件
    print_to_csv(word_list, 'output/test.csv')

    #输出固定词频的文件
    if fix_frequency:
        word_list_rate=words_rate(word_list,len(f_words))
        word_list_split = words_list_split(word_list_rate,start_and_end)
        print_to_csv(word_list_split,'output/word_fix_frequency.csv')
    else:
        print_to_csv(word_list,'output/word_all.csv')




if __name__ == "__main__":
    main()