import cv2
import os
import glob
character1=[]
character2=[]
n=0
# folder_path = 'resnet\\Tripitaka_Koreana_in_Han\\Class_label'  # 文件夹路径
file_pattern = os.path.join("Class_label_new", '*.txt')  # 文件匹配模式
file_list = glob.glob(file_pattern)  # 获取所有符合模式的文件列表
# print("char"+file_list[0][15:-3]+"jpg")
# print("22".zfill(3))
# cv2.imread("char"+file_list[0][15:-4]+"_001."+"jpg")
for i in range(len(file_list)):
    file_path=file_list[i]
# for file_path in file_list:
    with open(file_path, 'r',encoding='utf-8') as f:
        content = f.read().strip()
        lines = content.split('\n')
        # print(len(content))
        for i in(lines):
            # print(i)
            character1.append(i)
print(character1[1])
print(len(character1))
for i in character1:
    k=0
    for j in character2:
        if i==j:
            k=1
    if k!=1 and i!='?'and i!='*' and i!='/' and i!='<' and i!='>' and i!=',' and i!='|':
        # print("fal")
        character2.append(i)
# print(len(character2))
values= [0 for i in range(len(character2))]
my_dict = dict(zip(character2,values))
for i in character1:
    for key in my_dict:
        if(i==key):
            my_dict[key] += 1
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
for key, value in sorted_dict:
    print(key, value)
#     os.makedirs("{}".format(key))
# for i in range(len(character2)):
#     os.makedirs("{}".format(character2[i]))
#




def read_files(file1, file2, file3):
    with open(file1, 'r',encoding='utf-8') as f1, open(file2, 'r') as f2:
        img = cv2.imread(file3)
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i in range(len(lines1)):
            # print(lines1[i])
            lines2[i]=lines2[i][2:-1]
            lines2[i]=lines2[i].split(',')
            x= int(lines2[i][0])
            y = int(lines2[i][1])
            w = int(lines2[i][2])
            h = int(lines2[i][3])
            # (x, y, w, h)=lines2[i][2:]
            # text_region = img[y:h, x:w]   //好条件下的坐标
            text_region = img[y:y + h, x:x + w]
            # print(text_region)
            # print(lines1[i]+"/"+str(i)+".jpg")
            # if text_region!=[]:
            a=lines1[i].rstrip()
            if a!='?'and a!='*' and a!='/' and a!='<' and a!='>' and a!=',' and a!='|':
                if my_dict[lines1[i].rstrip()]>=150:

                    folder_name = "u" + str(ord(lines1[i].rstrip()))
                    folder_path = os.path.join(".", folder_name)
                    file_name = str(i) + ".jpg"
                    file_path = os.path.join(folder_path, file_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    cv2.imwrite(file_path, text_region)
#
def read_files2(cha,file3):
        img = cv2.imread(file3)
        a= cha.rstrip()
        if a!='?'and a!='*' and a!='/' and a!='<' and a!='>' and a!=',' and a!='|':
            if my_dict[a]>=200:
                folder_name = "u" + str(ord(a.rstrip()))
                folder_path = os.path.join(".", folder_name)
                file_name = str(i) + ".jpg"
                file_path = os.path.join(folder_path, file_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                cv2.imwrite(file_path, img)

#
#
#
#
folder_path1= "Multiple_Tripitaka_in_Han\\new annotation"
folder_path2 = "Multiple_Tripitaka_in_Han\\new class lable"
folder_path3 = "char"
file_pattern1 = os.path.join(folder_path1, '*.txt')
file_pattern2 = os.path.join(folder_path2,'*.txt')
file_pattern3 = os.path.join(folder_path3, '*.jpg')
file_list1 = glob.glob(file_pattern1)
file_list2 = glob.glob(file_pattern2)
file_list3 = glob.glob(file_pattern3)
# for i in range(len(character1)):
#     print(i)
# #     if(i!=124):
# #     read_files(file_list2[i],file_list1[i],file_list3[i])
# #
#     read_files2(character1[i],file_list3[i])
file_pattern = os.path.join("Class_label_new", '*.txt')  # 文件匹配模式
file_list = glob.glob(file_pattern)  # 获取所有符合模式的文件列表
print("char"+file_list[0][15:-3]+"jpg")
print("22".zfill(3))
cv2.imread("char"+file_list[0][15:-4]+"_001."+"jpg")
for j in range(len(file_list)):
    file_path=file_list[j]
# for file_path in file_list:
    with open(file_path, 'r',encoding='utf-8') as f:
        content = f.read().strip()
        lines = content.split('\n')
        # print(len(content))
        for i in range(len(lines)):
            # print(i)
         read_files2(lines[i],"char" + file_list[j][15:-4] + "_"+str(i+1).zfill(3)+"." + "jpg")


# test
# img = cv2.imread("changed word\\01-V001P000D.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 提取文本区域
#
# # with open('Tripitaka_Koreana_in_Han\\Annotations\\0001_001_26_01.txt', 'r') as f:
# #     lines = f.readlines()
# #     for line in lines:
# #         print(line[1:])  # 去掉行末的换行符
#
# (x, y, w, h) = (1209,482,61,69)
# text_region = img[y:y+h,x:x+w]
# folder_name = "u"+str(ord("大"))
# folder_path = os.path.join(".", folder_name)
# file_name = "2" + ".jpg"
# file_path = os.path.join(folder_path, file_name)
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
# cv2.imwrite(file_path,text_region)
