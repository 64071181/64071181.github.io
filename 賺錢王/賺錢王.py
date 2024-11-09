






'''
在 html $('#標題分頁').html(`<div id="py過">`) 
做 user not see py can see 元素
比py 判斷下一步
'''







import os
'''
      :::::::::           :::    :::::::::::           :::
     :+:    :+:        :+: :+:      :+:             :+: :+:
    +:+    +:+       +:+   +:+     +:+            +:+   +:+
   +#+    +:+      +#++:++#++:    +#+           +#++:++#++:
  +#+    +#+      +#+     +#+    +#+           +#+     +#+
 #+#    #+#      #+#     #+#    #+#           #+#     #+#
#########       ###     ###    ###           ###     ###

'''
更新時間 = '202411060935'
本程式名 = '賺錢王'

# 賺錢王瀏覽器
playwright = None
browser = None
page = None





















'''
        :::   :::       ::::::::       ::::    :::       ::::::::::    :::   :::       :::    :::       :::::::::::       ::::    :::       ::::::::
      :+:+: :+:+:     :+:    :+:      :+:+:   :+:       :+:           :+:   :+:       :+:   :+:            :+:           :+:+:   :+:      :+:    :+:
    +:+ +:+:+ +:+    +:+    +:+      :+:+:+  +:+       +:+            +:+ +:+        +:+  +:+             +:+           :+:+:+  +:+      +:+
   +#+  +:+  +#+    +#+    +:+      +#+ +:+ +#+       +#++:++#        +#++:         +#++:++              +#+           +#+ +:+ +#+      :#:
  +#+       +#+    +#+    +#+      +#+  +#+#+#       +#+              +#+          +#+  +#+             +#+           +#+  +#+#+#      +#+   +#+#
 #+#       #+#    #+#    #+#      #+#   #+#+#       #+#              #+#          #+#   #+#            #+#           #+#   #+#+#      #+#    #+#
###       ###     ########       ###    ####       ##########       ###          ###    ###       ###########       ###    ####       ########
'''



def 前往賺錢王(flow=''):
    global playwright, browser, page  # 使用全域變數

    print(f'''
            _\|/_
            (o o)
    +----oOO--U--OOo-------------------------{更新時間}-+
    |                                                     |
    | 賺錢王 歡迎您 !                                     |
    |                                                     |
    |     =====     賺錢王已啟動，請選擇功能     =====    |
    |                                                     | 
    |      *****************************************      |    
    |                                                     |
    +-----------------------------------------------------+
    ''')
    if flow == 1:
        # 啟動瀏覽器
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

    # 前往 賺錢王頁面
    #page.goto(f"file://{os.path.abspath('64071181.github.io/賺錢王/index.html')}?!?exe")
    #page.goto(f"file://{os.path.abspath('64071181.github.io/賺錢王/index.html')}")
    page.goto("https://64071181.github.io/賺錢王?MoneyKing")

    # 等已到首頁
    page.wait_for_selector('#py睇野')

    # user說明:5分鐘沒操作(沒標題分頁)，將自動退出
    page.locator("#py睇野").evaluate("div => div.innerText = '為保護您的隱私，5分鐘沒操作將自動退出'")

    _Page控Py流程(page,'#py過')

    # 等待 #標題分頁 元素出現並獲取初始值
    初始標題 = page.query_selector('#標題分頁 input').get_attribute('value')
    print(f"到 * {初始標題} * 頁")

    # admin功能
    if 初始標題 == 'exe':
        _adminFun(page,'exe')
    else:
        print(f"{初始標題}功能開發中...")
    
    前往賺錢王()






















'''
      :::::::::       :::::::::::       :::::::::       :::::::::::       ::::    :::       ::::::::   :::::::::::
     :+:    :+:          :+:           :+:    :+:          :+:           :+:+:   :+:      :+:    :+:      :+:
    +:+    +:+          +:+           +:+    +:+          +:+           :+:+:+  +:+      +:+             +:+
   +#++:++#+           +#+           +#++:++#+           +#+           +#+ +:+ +#+      +#++:++#++      +#+
  +#+                 +#+           +#+                 +#+           +#+  +#+#+#             +#+      +#+
 #+#                 #+#           #+#                 #+#           #+#   #+#+#      #+#    #+#      #+#
###             ###########       ###             ###########       ###    ####       ########       ###
'''
import subprocess
import sys

'''
# 卸載 Playwright 套件：
pip uninstall -y playwright
pip uninstall -y playwright-python

# 刪除 Playwright 緩存資料夾（此步驟會移除下載的瀏覽器資料）：
rmdir /s /q %USERPROFILE%\.cache\ms-playwright

# 設定要安裝的庫
    要安裝的庫 = ['playwright']
    _自動安裝py庫(要安裝的庫)

'''
def _自動安裝py庫(要安裝的庫):
    for 庫 in 要安裝的庫:
        try:
            # 使用 __import__ 動態匯入模組
            __import__(庫)
            print(f"**** {庫} 已安裝 ****")
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", 庫])
            print(f"**** {庫} 安裝完成 ****")

















'''
      :::::::::::       ::::    :::       ::::::::         :::   :::       ::::::::       :::::::::      :::    :::       :::        ::::::::::
         :+:           :+:+:   :+:      :+:    :+:       :+:+: :+:+:     :+:    :+:      :+:    :+:     :+:    :+:       :+:        :+:
        +:+           :+:+:+  +:+      +:+             +:+ +:+:+ +:+    +:+    +:+      +:+    +:+     +:+    +:+       +:+        +:+
       +#+           +#+ +:+ +#+      +#++:++#++      +#+  +:+  +#+    +#+    +:+      +#+    +:+     +#+    +:+       +#+        +#++:++#
      +#+           +#+  +#+#+#             +#+      +#+       +#+    +#+    +#+      +#+    +#+     +#+    +#+       +#+        +#+
     #+#           #+#   #+#+#      #+#    #+#      #+#       #+#    #+#    #+#      #+#    #+#     #+#    #+#       #+#        #+#
###########       ###    ####       ########       ###       ###     ########       #########       ########        ########## ##########

'''

# 利用分離模組動態載入
# https://chatgpt.com/share/672a38ed-5d24-8002-9b0f-4a5968693630
import importlib.util

def _動態載入Py(module_name, path):
    if os.path.exists(path):
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    else:
        print(f"Module {module_name} not found.")
        return None
'''
module = load_module('2525', './GGGGGG.py')
if module:
    # 使用載入的模組呼叫函式
    module.TESTQQQQ('Hello')
'''


























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

def _py生成的exe(file):

    _自動安裝py庫(['pyinstaller'])

    # ./dist
    #放exe位 = os.path.join(os.getcwd(), 'dist')

    # 檢查文件是否存當前目錄
    for 件 in [f'{file}.py','0.ico']:
        if not os.path.isfile(os.path.join(os.getcwd(), 件)):
            結果 = f'請將 *** {件} *** 放在當前目錄內，再執行'
            return 結果

    # 封裝exe
    封裝exe指令 = f'pyinstaller -F -i 0.ico {file}.py'
    process = os.popen(封裝exe指令)
    output = process.read()
    結果 = f" * 封裝{file}已完成 * "

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




def _Page控Py流程(page,id):
    # '#py過'
    try:
        page.wait_for_selector(id, timeout=300000)
        內容 = page.query_selector(id).text_content()
        print(f"操作={內容}")
        return 內容
    except:
        print("User 5分鐘沒操作，自動退出")
        exit()






def _adminFun(page,sel):

    if sel == 'exe':
        print(f"admin 功能 * 封裝 {sel} *")

        # 修改字 要網user del app
        page.locator("#執行").evaluate("button => button.innerText = '執行'")

        while True:
            # user 點 執行 or 退出
            流程 = _Page控Py流程(page,'#py過')
            if 流程== '退出':   
                前往賺錢王()

            if 流程 == '執行':   
                page.evaluate("document.querySelector('#a1').value = '封裝中...'")

                # 取 exe 名稱
                封裝後的exe名 = page.locator('textarea#b1').input_value()
                #print(f"封裝後的 exe 名稱是: {封裝後的exe名}")
                結果 = _py生成的exe(封裝後的exe名)

                print(結果)
                page.evaluate(f"document.querySelector('#a1').value = '{結果}'")

                # 封裝未完成重試
                if "已完成" not in 結果:
                    page.locator("#執行").evaluate("button => button.innerText = '重試'")
                    continue

                # 封裝完成    
                break














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

    while True:
        try:
            from playwright.sync_api import sync_playwright
            break
        except ImportError:
            _自動安裝py庫(['playwright'])

    前往賺錢王(1)

    input('任主按任意鍵結束程式...')
