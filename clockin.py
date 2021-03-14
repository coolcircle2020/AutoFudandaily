from selenium import webdriver
import time
import random

while True:
    print('欢迎使用自动平安复旦小程序~~')
    print('version 1.0.2')
    print('功能：每8个小时自动打卡平安复旦，全默认选项')
    click_delay = 2  # 设置按键延迟
    fo = open("usr.txt", "r", encoding='utf-8')
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 设置option
        c = webdriver.Chrome(executable_path=r'.\chromedriver.exe', options=option)  # 调用带无窗口参数的谷歌浏览器    time.sleep(int(2 * random.random()) + click_delay)
    except:
        # option = webdriver.EdgeOptions()
        # option.add_argument('headless')  # 设置option
        # c = webdriver.Edge(executable_path=r'.\msedgedriver.exe')  # 调用Edge
        print('请检查浏览器驱动位置是否在本程序同一目录下')
    else:
        pass
    try:#尝试进行登录
        # c = webdriver.Chrome(executable_path=r'.\chromedriver.exe', options=option)  # 调用带无窗口参数的谷歌浏览器
        c.get('https://zlapp.fudan.edu.cn/site/ncov/fudanDaily')  # 打开平安复旦
        time.sleep(3+int(1 * random.random()) + click_delay)
        cusr = c.find_element_by_id('username')
        cpw = c.find_element_by_id('password')
        data = fo.readlines()
        nu=data[0].strip('\n')
        pw=data[1].strip('\n')
        cusr.send_keys(nu)  # 输入学号
        cpw.send_keys(pw)  # 输入密码
        c.find_element_by_id('idcheckloginbtn').click()
        # print('登录成功！')
    except:
        print('登录失败！再试一次吧')
        time.sleep(int(1 * random.random()) + click_delay)
    else:
        time.sleep(int(1 * random.random()) + click_delay)
    try:#第一次登录提示界面
        confirm = c.find_element_by_class_name('wapat-btn')
        confirm.click()  # 确认
        print('登录成功，恭喜这是今天第一次登录！')
        time.sleep(int(1 * random.random()) + click_delay)
    except:
        time.sleep(int(1 * random.random()) + click_delay)
    else:
        time.sleep(int(1 * random.random()) + click_delay)
    try:#尝试获取位置信息
        area = c.find_element_by_name('area')
        area.click()  # 获取位置信息
        print('登录成功，正在获取位置信息！！')
    except:
        print('登录成功，获取位置信息失败！！')
        time.sleep(int(1 * random.random()) + click_delay)
    else:
        time.sleep(int(1 * random.random()) + click_delay)
    try:
        confirm1 = c.find_element_by_xpath('/ html / body / div[1] / div / div[1] / section / div[5] / div / a')
        confirm1.click()  # 提交信息
    except:
        time.sleep(int(1 * random.random()) + click_delay)
    else:
        time.sleep(int(1 * random.random()) + click_delay)
    try:
        confirm2 = c.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]')
        confirm2.click()  # 最终确认
        print('滴滴！打卡成功！学生卡！！！')
    except:
        print('滴滴！打卡失败，重复打卡！！！')
    else:
        time.sleep(int(1 * random.random()) + click_delay)
    c.quit()
    fo.close()
    localtime = time.asctime(time.localtime(time.time()))
    print("当前时间 :", localtime)
    print('自动打卡等待中......请不要关闭本窗口，八小时后自动再次打卡，当日重复打卡不会起效')
    time.sleep(8 * 60 * 60 + int(random.random()))
else:
    print('这不合理！')