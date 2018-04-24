#!/bin/python
# -*- coding: utf-8 -*-

import subprocess
import time
import random

abdpath="/bin/adb";# adb所在路径
readTime = 8*60*60;
startTime = int(time.time());
endTime = startTime+readTime;
nowTime = int(time.time());

print("开始阅读:"+str(readTime)+"秒") 

class ReadWeiXin(object):
    
    def __init__(self):
        pass
    # sleep 5 s
    def getSwipeMark(self):
        #随机 0.03可能性添加书签
        r_add=random.randint(1,100);
        if(r_add < 3):
            #        700+（570-1800）
            indexs = self.getSwipeMarkIndex();
            baseshell = abdpath+" shell input swipe %d %d %d %d"%indexs;
            self.calladb(baseshell);
            pass
    # sleep 5 s
    def read(self):
        #随机 5-15 休眠
        self.getSwipeMark();
        r_readtime=random.randint(28,30);
        time.sleep(r_readtime);
    # exec as shell command
    def nextPage(self):
        indexs = self.getSwipeNextIndex();
        baseshell = abdpath+" shell input swipe %d %d %d %d"%indexs;
        return self.calladb(baseshell);
    def calladb(self,adbcmd):
        p = subprocess.Popen(adbcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_stdout, s_stderr = p.communicate()
        return_code = p.returncode
        self.checkResult((s_stdout, s_stderr, return_code));
        return (s_stdout, s_stderr, return_code)
    def checkResult(self,adbresult):
        if not ((adbresult[0] == adbresult[1]) and (adbresult[1] == '')):
            print(adbresult,nowTime);# adb操作失败
            pass
        pass
    
    def getSwipeMarkIndex(self):
        sx = random.randint(300,800);
        sy = 404+random.randint(300,500);
        ex = sx+random.randint(-200,200);
        ey = sy+random.randint(570,750);
        return sx,sy,ex,ey;
    def getSwipeNextIndex(self):
        sx = 950-random.randint(1,200);
        sy = 1800-random.randint(1,200);
        ex = 100+random.randint(1,200);
        ey = 1800-random.randint(300,500);
        return sx,sy,ex,ey;

if __name__ == "__main__":
    wxyd = ReadWeiXin();
    while(endTime > nowTime):
        wxyd.nextPage();# ('', '', 1)
        wxyd.read();#等待一会
        nowTime = int(time.time());#获取当前时间


#屏幕： 1920 1080
#屏幕： 宽1050 高1900

# 自设定
#宽度范围 70-900
#高度范围 700-1800>

# 下滑 存书签：       最低y1 最低长度（570-） 最高长度
# 左右滑动 翻页读书： 最低起点 最低长度 最高长度(屏幕)
# swipe#(1020-220)->60 160
