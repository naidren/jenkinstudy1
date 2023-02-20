# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: configUpgrade.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: 
# @Time: 9月 30, 2022
# ---
import requests,re,os
import zipfile
def get_driver_version(brower_version:str):
    donwload_url = r"http://chromedriver.storage.googleapis.com/?delimiter=/&prefix="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    res = requests.get(donwload_url, headers=headers).text
    print("*******************获取驱动器下载列表成功！*********************************")
    # all_version = re.findall("\d{2,3}\.0\.\d{4}\.\d{1,3}", res)
    # 只支持100版本以后的
    all_version = re.findall("\d{3}\.0\.\d{4}\.\d{1,3}", res)
    print(all_version)
    ver_sum = len(all_version)
    # 浏览器器版本号
    google_version = brower_version.split(".")
    for i in range(ver_sum):
        d_version = all_version[i].split('.')
        if d_version[0] == google_version[0] and d_version[2] == google_version[2]:
            # 驱动版本小于浏览器版本
            if int(d_version[3]) <= int(google_version[3]):
                return all_version[i]
            # 驱动版本大于浏览器版本
            elif int(d_version[3]) > int(google_version[3]):
                if i == 0:
                    print("没有找到更小的驱动器版本！")

                elif i > 0:
                    return all_version[i-1]

def upgrade_driver(google_path=None,python_path=None):
    if google_path is None:
        google_path = r"C:\Program Files\Google\Chrome\Application"
    if python_path is None:
        python_path = r"C:\Users\86166\AppData\Local\Programs\Python\Python38"
    zip_file = python_path + "\\" + "chromedriver_win32.zip"
    driver_file = python_path + "\\" + "chromedriver.exe"
    # 先删除压缩包文件
    if os.path.exists(zip_file):
        os.remove(zip_file)
    # 获取和本地谷歌浏览器相匹配的版本号
    goal_verison = get_driver_version(os.listdir(google_path)[0])
    print("当前浏览器的版本号为:{0}".format(goal_verison))
    if goal_verison:
        donwload_url = r"http://chromedriver.storage.googleapis.com/{0}/chromedriver_win32.zip".format(goal_verison)
        print(donwload_url)
    else:
        raise ValueError("获取驱动版本号失败")
    headers ={
        "Accept-Encoding": "gzip, deflate",
        # "Upgrade-Insecure-Requests":"1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

    # 下载驱动器和保存到python安装目录下
    res = requests.get(donwload_url,headers=headers)
    with open(zip_file,mode="wb") as f:
        f.write(res.content)
    # 删除驱动文件
    find_cmd1 = 'tasklist | findstr "chromedriver.exe"'
    kill_cmd2 = 'taskkill -f -PID chromedriver.exe'
    if os.path.exists(driver_file):
        # 查询驱动器进程是否运行,1为没有该进程.不是1则说明存在进程，需要杀掉。
        if os.system(find_cmd1)!=1:
            # 此命令执行成功返回0
            os.system(kill_cmd2)
        os.remove(driver_file)

    # 解压缩驱动文件
    with zipfile.ZipFile(zip_file) as zf:
        zf.extractall(python_path)
    print("驱动器更新完成！！！")



if __name__ == '__main__':
    upgrade_driver()







