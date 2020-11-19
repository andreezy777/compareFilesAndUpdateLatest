#compare and re-writing file

import sys

inputfile1 = str(sys.argv[1])
inputfile2 = str(sys.argv[2])


count_file1 = 0

with open(inputfile1) as file1:
        for line in file1:
            count_file1 += 1
            print("TextFile1 = {}: {}".format(count_file1, line.strip()))
        print("Lines count", count_file1)

count_file2 = 0

with open(inputfile2) as file2:
        for line in file2:
            count_file2 += 1
            print("TextFile2 = {}: {}".format(count_file2, line.strip()))
        print("Lines count", count_file2)

count_file = 0

if count_file1 < count_file2:
    count_file = count_file2
    with open(inputfile1, "a") as file_tmp_1:
        for i in range(count_file1, count_file+1):
            file_tmp_1.writelines("\n")
elif count_file1 == count_file2:
    count_file = count_file2
else:
    count_file = count_file2
    with open(inputfile1, "r") as file_tmp_2:
        lines = file_tmp_2.readlines()
        with open(inputfile1, "w") as file_tmp_2_1:
            for i in range(0, count_file2):
                print(lines[i].replace('\n', ''))
                file_tmp_2_1.writelines(lines[i])

with open(inputfile1) as file1:
    with open(inputfile2) as file2:
        text1 = file1.readlines()
        text2 = file2.readlines()
        for i in range(0, count_file):
            if text1[i] != text2[i]:
                text1[i] = text2[i]
                print(text1[i].replace('\n', ''))
        with open(inputfile1, "w") as filefinal:
            filefinal.writelines(text1)
