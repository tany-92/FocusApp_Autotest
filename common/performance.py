# coding=utf-8

import re
import os
from common.readConfig import Readconfig

conf = Readconfig()


class Performance:

    def __init__(self):

        """
            从config配置文件中获取adb命令
        """
        self.cpu = conf.getcmdValue('cpu')
        self.men = conf.getcmdValue('men')
        self.fps = conf.getcmdValue('fps')

    def get_cpu(self):

        """
            获取CPU
        """
        get_cpu = os.popen(self.cpu).readlines()
        for info in get_cpu:
            cpu_info = float(info.split()[2].split("%")[0])
            return cpu_info

    def get_men(self):

        """
            内存泄漏
        """
        total = "TOTAL"
        get_men = os.popen(self.men).readlines()
        for info in get_men:
            info_sp = info.strip().split()
            for item in range(len(info_sp)):
                if info_sp[item] == total:
                    men_info = int(info_sp[item+1])
                    return men_info
        return 0

    def get_fps(self):

        """
            获取帧率
        """
        results = os.popen(self.fps).read().strip()
        frames = [x for x in results.split('\n')]
        frame_count = len(frames[1:121])
        jank_count = 0
        vsync_overtime = 0
        for frame in frames[1:121]:
            time_block = re.split(r'\s+', frame.strip())
            if len(time_block) == 4:
                try:
                    render_time = float(time_block[0]) + float(time_block[1]) + float(time_block[2]) + float(time_block[3])
                except:
                    render_time = 0
                if render_time > 16.67:
                    jank_count += 1
                    if render_time % 16.67 == 0:
                        vsync_overtime += int(render_time / 16.67) - 1
                    else:
                        vsync_overtime += int(render_time / 16.67)
                fps = int(frame_count * 60 / (frame_count + vsync_overtime))
                return frame_count, jank_count, fps


if __name__ == '__main__':
    per = Performance()
    print(per.get_cpu())
    print(per.get_men())
    print(per.get_fps())