









'''
      ::::    :::       ::::::::   :::::::::::       ::::::::::
     :+:+:   :+:      :+:    :+:      :+:           :+:
    :+:+:+  +:+      +:+    +:+      +:+           +:+
   +#+ +:+ +#+      +#+    +:+      +#+           +#++:++#
  +#+  +#+#+#      +#+    +#+      +#+           +#+
 #+#   #+#+#      #+#    #+#      #+#           #+#
###    ####       ########       ###           ##########

202411122127

'''



更新時間 = '202411122127'
本程式名 = '賺錢王'

# 賺錢王瀏覽器
賺錢王瀏覽器位 = 'MoneyKingChrome'

playwright = browser = page = None


import os
import sys
import logging
import subprocess




































'''
      :::::::::           :::        ::::::::       ::::::::::
     :+:    :+:        :+: :+:     :+:    :+:      :+:
    +:+    +:+       +:+   +:+    +:+             +:+
   +#++:++#+       +#++:++#++:   +#++:++#++      +#++:++#
  +#+    +#+      +#+     +#+          +#+      +#+
 #+#    #+#      #+#     #+#   #+#    #+#      #+#
#########       ###     ###    ########       ##########


'''

def _Page控Py流程(page):
    '''
    在 html $('#標題分頁').html(`<div id="py過">`) 
    做 user not see py can see 元素
    比py 判斷下一步
    '''

    try:
        page.wait_for_selector('#py過', timeout=300000)
        內容 = page.query_selector('#py過').text_content()
        print(f"操作={內容}")
        return 內容
    except:
        sys.exit("User 5分鐘沒操作，自動退出")

            
























'''
      ::::::::       :::    :::       :::::::::       ::::::::         :::   :::       ::::::::::
    :+:    :+:      :+:    :+:       :+:    :+:     :+:    :+:       :+:+: :+:+:      :+:
   +:+             +:+    +:+       +:+    +:+     +:+    +:+      +:+ +:+:+ +:+     +:+
  +#+             +#++:++#++       +#++:++#:      +#+    +:+      +#+  +:+  +#+     +#++:++#
 +#+             +#+    +#+       +#+    +#+     +#+    +#+      +#+       +#+     +#+
#+#    #+#      #+#    #+#       #+#    #+#     #+#    #+#      #+#       #+#     #+#
########       ###    ###       ###    ###      ########       ###       ###     ##########
'''
import shutil
def _下載賺錢王Chrome():
    # 確定 EXE 同層目錄，若在打包環境下，使用 sys.executable 取得 EXE 目錄
    exe_dir = os.path.dirname(sys.executable) if hasattr(sys, 'frozen') else os.path.dirname(os.path.abspath(__file__))

    # 設置 MoneyKingChrome 資料夾路徑
    chrome_dir = os.path.join(exe_dir, 賺錢王瀏覽器位)
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = chrome_dir

    # Playwright 預設下載的臨時位置
    temp_chrome_dir = os.path.join(os.getenv("LOCALAPPDATA"), "ms-playwright")

    chromium_path = os.path.join(chrome_dir, "chromium-1140", "chrome-win", "chrome.exe")
    #print('chromium_path =', chromium_path)

    # 檢查 EXE 同層 MoneyKingChrome 資料夾是否已存在 Chrome
    if not os.path.isfile(chromium_path):
        try:
            # 執行 playwright install
            subprocess.run(["playwright", "install"], check=True)
            
            # 在臨時資料夾中找到下載的 Chrome 目錄並複製到 EXE 同層目錄
            downloaded_chrome = os.path.join(temp_chrome_dir, "chromium-1140", "chrome-win")
            if os.path.exists(downloaded_chrome):
                # 若 EXE 同層 MoneyKingChrome 資料夾已存在，先刪除再複製
                if os.path.exists(chrome_dir):
                    shutil.rmtree(chrome_dir)
                shutil.copytree(downloaded_chrome, os.path.join(chrome_dir, "chromium-1140", "chrome-win"))
                print(f"已將 Chrome 瀏覽器複製到 EXE 同層的 {賺錢王瀏覽器位} 資料夾中。")
            else:
                print("瀏覽器下載失敗，無法找到下載的目錄。")
        except subprocess.CalledProcessError as e:
            print(f"安裝 Playwright 瀏覽器失敗: {e}")
    #else:
        #print("Chrome 瀏覽器已安裝在指定路徑中。")






































'''
      :::::::::::       ::::    :::       ::::::::         :::   :::       ::::::::       :::::::::      :::    :::       :::        ::::::::::
         :+:           :+:+:   :+:      :+:    :+:       :+:+: :+:+:     :+:    :+:      :+:    :+:     :+:    :+:       :+:        :+:
        +:+           :+:+:+  +:+      +:+             +:+ +:+:+ +:+    +:+    +:+      +:+    +:+     +:+    +:+       +:+        +:+
       +#+           +#+ +:+ +#+      +#++:++#++      +#+  +:+  +#+    +#+    +:+      +#+    +:+     +#+    +:+       +#+        +#++:++#
      +#+           +#+  +#+#+#             +#+      +#+       +#+    +#+    +#+      +#+    +#+     +#+    +#+       +#+        +#+
     #+#           #+#   #+#+#      #+#    #+#      #+#       #+#    #+#    #+#      #+#    #+#     #+#    #+#       #+#        #+#
###########       ###    ####       ########       ###       ###     ########       #########       ########        ########## ##########


module = _動態載入Py('別名', './GGGGGG.py')
if module:
    # 使用載入的模組呼叫函式
    module.TESTQQQQ('Hello')

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
        :::   :::       ::::::::       ::::    :::       ::::::::::    :::   :::       :::    :::       :::::::::::       ::::    :::       ::::::::
      :+:+: :+:+:     :+:    :+:      :+:+:   :+:       :+:           :+:   :+:       :+:   :+:            :+:           :+:+:   :+:      :+:    :+:
    +:+ +:+:+ +:+    +:+    +:+      :+:+:+  +:+       +:+            +:+ +:+        +:+  +:+             +:+           :+:+:+  +:+      +:+
   +#+  +:+  +#+    +#+    +:+      +#+ +:+ +#+       +#++:++#        +#++:         +#++:++              +#+           +#+ +:+ +#+      :#:
  +#+       +#+    +#+    +#+      +#+  +#+#+#       +#+              +#+          +#+  +#+             +#+           +#+  +#+#+#      +#+   +#+#
 #+#       #+#    #+#    #+#      #+#   #+#+#       #+#              #+#          #+#   #+#            #+#           #+#   #+#+#      #+#    #+#
###       ###     ########       ###    ####       ##########       ###          ###    ###       ###########       ###    ####       ########
'''

from playwright.sync_api import sync_playwright
def 前往賺錢王(flow=''):
    global playwright, browser, page  # 使用全域變數

    歡迎 = '賺錢王已啟動，請選擇功能'

    if flow == 1:
        # 使用指定的 Chrome 瀏覽器路徑
        exe_dir = os.path.dirname(sys.executable) if hasattr(sys, 'frozen') else os.path.dirname(os.path.abspath(__file__))
        chromium_path = os.path.join(exe_dir, 賺錢王瀏覽器位, "chromium-1140", "chrome-win", "chrome.exe")
        # 啟動瀏覽器
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False, executable_path=chromium_path)
        page = browser.new_page()
    else:
        歡迎 = flow

    print(f'''
            _\|/_
            (o o)
    +----oOO--U--OOo-------------------------{更新時間}-+
    |                                                     |
      賺錢王 歡迎您 !                                      
    |                                                     |
           {歡迎}                     
    |                                                     | 
           *****************************************          
    |                                                     |
    +-----------------------------------------------------+
    ''')

    # 前往 賺錢王頁面
    #page.goto(f"file://{os.path.abspath('64071181.github.io/賺錢王/index.html')}?!?exe")
    #page.goto(f"file://{os.path.abspath('index.html')}")
    page.goto("https://64071181.github.io/賺錢王?MoneyKing")

    # 等已到首頁
    page.wait_for_selector('#py睇野')

    # user說明:5分鐘沒操作(沒標題分頁)，將自動退出
    page.locator("#py睇野").evaluate("div => div.innerText = '為保護您的隱私，5分鐘沒操作將自動退出'")
    _Page控Py流程(page)

    # 等待 #標題分頁 元素出現並獲取初始值
    初始標題 = page.query_selector('#標題分頁 input').get_attribute('value')
    #print(f"到 * {初始標題} * 頁")

    # admin功能
    admin功能 = _動態載入Py('admin功能py', './_adminFun.py')

    # 按標題選動作
    結果 = f"{初始標題}功能開發中..."

    if 初始標題 == 'exe':
        # 需有 _adminFun.py 和 .aki pw文件
        if admin功能 and os.path.isfile('.aki'):
            結果 = admin功能._adminFun(page,初始標題)



    前往賺錢王(結果)





















































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
    try:
        # 自動安裝Chrome
        _下載賺錢王Chrome()


        if playwright == None:
            前往賺錢王(1)
        else:
            前往賺錢王()


    except Exception as e:
        logging.error("發生錯誤", exc_info=True)
        input("按任意鍵結束...")


