import os
from shutil import copy, rmtree
import random


def mk_file(file_path: str):
    if os.path.exists(file_path):
        rmtree(file_path)
    os.makedirs(file_path)


def main():
    # 保证随机可复现
    random.seed(0)
    split_rate = 0.1
    cwd = os.getcwd()
    origin_flower_path = os.path.join(cwd, "data3")
    assert os.path.exists(origin_flower_path), "path '{}' does not exist.".format(origin_flower_path)
    flower_class = [cla for cla in os.listdir(origin_flower_path)
                    if os.path.isdir(os.path.join(origin_flower_path, cla))]

    # 创建训练集train文件夹，并由类名在其目录下创建子目录
    train_root = os.path.join( origin_flower_path, "train")
    mk_file(train_root)
    for cla in flower_class:
        # 建立每个类别对应的文件夹
        mk_file(os.path.join(train_root, cla))


    val_root = os.path.join( origin_flower_path, "val")
    mk_file(val_root)
    for cla in flower_class:
        # 建立每个类别对应的文件夹
        mk_file(os.path.join(val_root, cla))

    # 遍历所有类别的图像并按比例分成训练集和验证集
    for cla in flower_class:
        cla_path = os.path.join(origin_flower_path, cla)
        # iamges列表存储了该目录下所有图像的名称
        images = os.listdir(cla_path)
        num = len(images)
        eval_index = random.sample(images, k=int(num * split_rate))
        for index, image in enumerate(images):
            if image in eval_index:
                # 将分配至验证集中的文件复制到相应目录
                image_path = os.path.join(cla_path, image)
                new_path = os.path.join(val_root, cla)
                copy(image_path, new_path)
            else:
                # 将分配至训练集中的文件复制到相应目录
                image_path = os.path.join(cla_path, image)
                new_path = os.path.join(train_root, cla)
                copy(image_path, new_path)

            print("\r[{}] processing [{}/{}]".format(cla, index + 1, num), end="")
        print()

    print("processing done!")


if __name__ == '__main__':
    main()