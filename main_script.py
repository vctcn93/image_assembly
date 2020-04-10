# from threading import Thread, Lock
import configparser
import os, sys, re
from lib.couple import Couple
from lib.config import Config
from lib.converter import Converter


converter = Converter
config = configparser.ConfigParser()
configs = None
couples = None


def load_project():
    global couples
    global configs
    project_path = sys.argv[1]

    print('>>>%15s :' % "正在读取图片通道...")
    set_couples(project_path)
    print('>>>', couples)

    print('>>>%15s :' % "正在读取相关配置...")
    set_configs(project_path)
    print('>>>', configs)


def set_couples(project_path):
    global converter
    global couples

    file_paths = os.listdir(f'{project_path}/images')
    image_channels = list()
    image_paths = list()
    channel_paths = list()

    for file_path in file_paths:
        if re.search(r"(.*)_ch.(.*)", file_path):
            channel_paths.append(file_path)
        else:
            image_paths.append(file_path)

    for img_path in image_paths:
        couple = list()
        img_name = img_path.split('.')[0]

        for cl_path in channel_paths:
            if cl_path.startswith(img_name):
                clp = cl_path
                break
            else:
                clp = None

        couple.append(f'{project_path}/images/{img_path}')
        couple.append(f'{project_path}/images/{clp}')
        image_channels.append(couple)

    couples = [Couple(converter, img, chl) for img, chl in image_channels]


def set_configs(project_path) -> list:
    global configs

    config_path = f'{project_path}/config.ini'
    config.read(config_path)
    configs = [Config(key, value) for key, value in config._sections.items()]


def parse():
    global couples
    global configs

    for i, couple in enumerate(couples):
        for config in configs:
            couple.adjust_by_config(config)
            print('overed 1 config...')
        couple.export()
        print('%50s' % '>>> Finished',  i+1, 'Couple. >>>')


def main():
    load_project()
    parse()


if __name__ == '__main__':
    main()
