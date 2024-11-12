









'''
      ::::    :::       ::::::::   :::::::::::       ::::::::::
     :+:+:   :+:      :+:    :+:      :+:           :+:
    :+:+:+  +:+      +:+    +:+      +:+           +:+
   +#+ +:+ +#+      +#+    +:+      +#+           +#++:++#
  +#+  +#+#+#      +#+    +#+      +#+           +#+
 #+#   #+#+#      #+#    #+#      #+#           #+#
###    ####       ########       ###           ##########

202411112253

'''
import os
import 賺錢王



更新時間 = 賺錢王.更新時間




















'''
      :::::::::       :::::::::::       :::::::::       :::::::::::       ::::    :::       ::::::::   :::::::::::
     :+:    :+:          :+:           :+:    :+:          :+:           :+:+:   :+:      :+:    :+:      :+:
    +:+    +:+          +:+           +:+    +:+          +:+           :+:+:+  +:+      +:+             +:+
   +#++:++#+           +#+           +#++:++#+           +#+           +#+ +:+ +#+      +#++:++#++      +#+
  +#+                 +#+           +#+                 +#+           +#+  +#+#+#             +#+      +#+
 #+#                 #+#           #+#                 #+#           #+#   #+#+#      #+#    #+#      #+#
###             ###########       ###             ###########       ###    ####       ########       ###

# 卸載 Playwright 套件：
pip uninstall -y playwright
pip uninstall -y playwright-python

# 刪除 Playwright 緩存資料夾（此步驟會移除下載的瀏覽器資料）：
rmdir /s /q %USERPROFILE%\.cache\ms-playwright

# 設定要安裝的庫
    要安裝的庫 = ['playwright']
    _自動安裝py庫(要安裝的庫)

'''

import sys


def _自動安裝py庫(要安裝的庫):
    for 庫 in 要安裝的庫:
        try:
            # 使用 __import__ 動態匯入模組
            __import__(庫)
            print(f"**** {庫} 已安裝 ****")
        except ImportError:
            賺錢王.subprocess.check_call([sys.executable, "-m", "pip", "install", 庫])

            print(f"**** {庫} 安裝完成 ****")
























'''
      ::::::::::       :::    :::       ::::::::::         :::   :::
     :+:              :+:    :+:       :+:               :+:+: :+:+:
    +:+               +:+  +:+        +:+              +:+ +:+:+ +:+
   +#++:++#           +#++:+         +#++:++#         +#+  +:+  +#+
  +#+               +#+  +#+        +#+              +#+       +#+
 #+#              #+#    #+#       #+#              #+#       #+#
##########       ###    ###       ##########       ###       ###

'''

# py生成的.exe
from multiprocessing import Event

def _py生成的exe(file,版本=''):

    _自動安裝py庫(['pyinstaller'])

    # 檢查文件是否存當前目錄
    for 件 in [f'{file}.py','0.ico']:
        if not os.path.isfile(os.path.join(os.getcwd(), 件)):
            結果 = f'請將 *** {件} *** 放在當前目錄內，再執行'
            return 結果

    # 封裝exe
    封裝exe指令 = f'pyinstaller -F -i 0.ico {file}.py -n {file}{版本}'
    process = os.popen(封裝exe指令)
    output = process.read()
    結果 = f" *** 封裝 * {file} * 已完成 *** "

    return 結果



























'''
     :::    :::       :::::::::         :::   :::       ::::::::::       ::::::::           :::
    :+:    :+:       :+:    :+:       :+:+: :+:+:      :+:             :+:    :+:        :+: :+:
   +:+    +:+       +:+    +:+      +:+ +:+:+ +:+     +:+             +:+              +:+   +:+
  +#+    +:+       +#++:++#+       +#+  +:+  +#+     +#++:++#        :#:             +#++:++#++:
 +#+    +#+       +#+             +#+       +#+     +#+             +#+   +#+#      +#+     +#+
#+#    #+#       #+#             #+#       #+#     #+#             #+#    #+#      #+#     #+#
########        ###             ###       ###     ##########       ########       ###     ###


'''

# pip install mega.py
from mega import Mega
# 自動up 到 mega
def _UpToMega(page,NewATWexe,ac,pw):
    
    UP檔 = 'dist/'+NewATWexe+'.exe'
    while True:
        # 檢查檔案是否存在
        if os.path.isfile(UP檔):
            print('  **** 正在上傳到mega... ****    ')
            page.evaluate("document.querySelector('#a1').value = '**** 正在上傳到mega... ****'")
            # upload ATW.exe
            # https://pypi.org/project/mega.py/
            mega = Mega()
            m = mega.login(ac, pw)
            folder = m.find('MoneyKing')
            m.upload(UP檔, folder[0])
            break
        else:
            print(f'  **** 請將 {NewATWexe} 放在 dist 資料夾內再試... ****    ')
            page.evaluate(f"document.querySelector('#a1').value = '**** 請將 {NewATWexe} 放在 dist 資料夾內再試... ****'")
            continue

    # mageAtw url   
    # https://www.geeksforgeeks.org/how-to-use-mega-nz-api-with-python/
    fileName = m.find(NewATWexe+'.exe')
    # Use it in get_link function
    link = m.get_link(fileName)

    return NewATWexe,link























'''
     :::    :::       :::::::::       :::::::::           :::    :::::::::::           :::
    :+:    :+:       :+:    :+:      :+:    :+:        :+: :+:      :+:             :+: :+:
   +:+    +:+       +:+    +:+      +:+    +:+       +:+   +:+     +:+            +:+   +:+
  +#+    +:+       +#++:++#+       +#+    +:+      +#++:++#++:    +#+           +#++:++#++:
 +#+    +#+       +#+             +#+    +#+      +#+     +#+    +#+           +#+     +#+
#+#    #+#       #+#             #+#    #+#      #+#     #+#    #+#           #+#     #+#
########        ###             #########       ###     ###    ###           ###     ###

'''

import requests
from github import Github

# 自動up 到 Github
def _UpToGithub(DwlUrl,設備,TOKEN):
    GetData = requests.get('https://raw.githubusercontent.com/64071181/MoneyKingUpdataList/refs/heads/main/MoneyKingUpdataList.js').text

    Dwl列表頭 = GetData.split('[')[0]
    Dwl列表尾 = ']'
    Dwl列內容 = GetData.split('[')[1].split(']')[0]
    Dwl列內容B = Dwl列內容.split(',') # 1,2,3,4
    新的內容 = ""

    if 設備 == 'Windows':
        新的內容 = f'{Dwl列表頭}"{DwlUrl}",{Dwl列內容B[1]},{Dwl列內容B[2]},{Dwl列內容B[3]}{Dwl列表尾}'
    if 設備 == 'Mac':
        新的內容 = f'{Dwl列表頭}{Dwl列內容B[0]},"{DwlUrl}",{Dwl列內容B[2]},{Dwl列內容B[3]}{Dwl列表尾}'
    if 設備 == 'iOS':
        新的內容 = f'{Dwl列表頭}{Dwl列內容B[0]},{Dwl列內容B[1]},"{DwlUrl}",{Dwl列內容B[3]}{Dwl列表尾}'
    if 設備 == 'Android':
        新的內容 = f'{Dwl列表頭}{Dwl列內容B[0]},{Dwl列內容B[1]},{Dwl列內容B[2]},"{DwlUrl}"{Dwl列表尾}'


    # GitHub Token (需在 GitHub 上創建個人存取權杖)
    REPO_NAME = "64071181/MoneyKingUpdataList"
    FILE_PATH = "MoneyKingUpdataList.js"  # 指定檔案在儲存庫中的路徑

    

    COMMIT_MESSAGE = f'''
        更新 MoneyKingUpdataList.js 
        設備={設備}
        版本={更新時間}
    '''

    # 初始化 GitHub 連線
    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)

    # 取得目前的檔案內容與 sha 值
    file = repo.get_contents(FILE_PATH)
    repo.update_file(file.path, COMMIT_MESSAGE, 新的內容, file.sha)

    結果 = f"版本={設備}\n更新時間={更新時間} 已更新成功！"
    return 結果










































'''
          :::        :::::::::         :::   :::       :::::::::::       ::::    :::
       :+: :+:      :+:    :+:       :+:+: :+:+:          :+:           :+:+:   :+:
     +:+   +:+     +:+    +:+      +:+ +:+:+ +:+         +:+           :+:+:+  +:+
   +#++:++#++:    +#+    +:+      +#+  +:+  +#+         +#+           +#+ +:+ +#+
  +#+     +#+    +#+    +#+      +#+       +#+         +#+           +#+  +#+#+#
 #+#     #+#    #+#    #+#      #+#       #+#         #+#           #+#   #+#+#
###     ###    #########       ###       ###     ###########       ###    ####

'''
適用設備 = ''
def _adminFun(page,sel,檔=''): 
    global 適用設備

    # 打開並讀取文件 未加密 ***
    with open('.aki', 'r', encoding='utf-8') as file:
        content = file.read()
        allPw = content.split('\n') 
        # 0=megaAC, 1=megaPW, 2=GithubAPI

    # exe ****
    if sel == 'exe':
        print(f"admin 功能 * 封裝 {sel} *")

        版本 = ''
        # 修改字 要網user del app
        page.locator("#執行").evaluate("button => button.innerText = '執行'")

        while True:
            # user 點 執行 or 退出
            流程 = 賺錢王._Page控Py流程(page)
            if 流程== '退出':   
                #賺錢王.前往賺錢王()
                sys.exit("自動退出")

            if 流程 == '執行':   
                page.evaluate("document.querySelector('#a1').value = '封裝中...'")

                # 取 exe 名稱
                封裝後的exe名 = page.locator('textarea#b1').input_value()

                # admin專用 加時間版本
                if 封裝後的exe名 == "賺錢王":
                    適用設備 = page.query_selector('#device-info').text_content()
                    版本 = f'_{適用設備}_{更新時間}'

                結果 = _py生成的exe(封裝後的exe名,版本)

                print(結果)
                page.evaluate(f"document.querySelector('#a1').value = '{結果}'")

                # 封裝未完成重試
                if "已完成" not in 結果:
                    page.locator("#執行").evaluate("button => button.innerText = '重試'")
                    continue

                # 封裝完成    
                break
            else:
                # 等 退執
                continue

        # admin專用 Up To Mega
        if allPw[1] :
            _adminFun(page,'UpToMega',封裝後的exe名+版本)
        return f'{封裝後的exe名}{版本}.exe封裝已完成，在 dist 資料夾內'


    # UpToMega ****
    if sel == 'UpToMega':
        up完 = _UpToMega(page,檔,allPw[0],allPw[1])
        結果B = f'{up完[0]}.exe 已上傳\n網址: {up完[1]}'
        print(結果B)

        # admin專用 Up To Github
        if allPw[2] :
            _adminFun(page,'UpToGithub',up完[1])
        return 結果B


    # UpToGithub ****
    if sel == 'UpToGithub':
        結果c = _UpToGithub(檔,適用設備,allPw[2] )
        print(結果c)
        return 結果c
        






























































'''
      ::::::::   :::::::::::           :::        :::::::::   :::::::::::
    :+:    :+:      :+:             :+: :+:      :+:    :+:      :+:
   +:+             +:+            +:+   +:+     +:+    +:+      +:+
  +#++:++#++      +#+           +#++:++#++:    +#++:++#:       +#+
        +#+      +#+           +#+     +#+    +#+    +#+      +#+
#+#    #+#      #+#           #+#     #+#    #+#    #+#      #+#
########       ###           ###     ###    ###    ###      ###

'''
if __name__ == "__main__":

    # 打開並讀取文件
    with open('aki.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)


    _UpToGithub()
    input("請由賺錢王進入...")


