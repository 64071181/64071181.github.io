


















/* $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        :::   :::       ::::::::       :::    :::           :::        :::    :::       :::::::::::
      :+:+: :+:+:     :+:    :+:      :+:   :+:          :+: :+:      :+:   :+:            :+:
    +:+ +:+:+ +:+    +:+    +:+      +:+  +:+          +:+   +:+     +:+  +:+             +:+
   +#+  +:+  +#+    +#+    +:+      +#++:++          +#++:++#++:    +#++:++              +#+
  +#+       +#+    +#+    +#+      +#+  +#+         +#+     +#+    +#+  +#+             +#+
 #+#       #+#    #+#    #+#      #+#   #+#        #+#     #+#    #+#   #+#            #+#
###       ###     ########       ###    ###       ###     ###    ###    ###       ###########

202410211001                                         mokaki
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */
























/* $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

      :::::::::           :::        ::::::::       ::::::::::
     :+:    :+:        :+: :+:     :+:    :+:      :+:
    +:+    +:+       +:+   +:+    +:+             +:+
   +#++:++#+       +#++:++#++:   +#++:++#++      +#++:++#
  +#+    +#+      +#+     +#+          +#+      +#+
 #+#    #+#      #+#     #+#   #+#    #+#      #+#
#########       ###     ###    ########       ##########

基本功能：
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */


const 親老婆 ="\u0032\u0064\u0032\u0063\u0038\u0062\u0037\u0063\u0036\u0037\u0064\u0030\u0037\u0034\u0061\u0030\u0063\u0032\u0061\u0062\u0035\u0034\u0038\u0037\u0063\u0064\u0034\u0033\u0063\u0032\u0062\u0032\u0035\u0035\u0039\u0061\u0066\u0039\u0034\u0066\u0036\u0039\u0036\u0030\u0035\u0038\u0032\u0064\u0037\u0032\u0039\u0030\u0033\u0037\u0066\u0062\u0034\u0065\u0034\u0066\u0030\u0036\u0037\u0065"["\u0073\u0070\u006c\u0069\u0074"](""["\u0073\u0070\u006c\u0069\u0074"](""["\u0073\u0070\u006c\u0069\u0074"]("".split("").reverse().join(""))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"](""))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"](""['split']("".split("").reverse().join(""))['reverse']()["\u006a\u006f\u0069\u006e"]('')))['reverse']()['join'](''['split']("".split("").reverse().join(""))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"](''))
    , 總網址 = '64071181.github.io/'


function mokJsApi_說明(){

  console.log(`
    ****** 202408301445 ******
    **************************
    https://64071181.github.io/mokJsapi/
    **************************
    https://64071181.github.io/
    **************************
    ****** 202410201051 ******
  `);

}  


$(document).ready(function() {
  // <script src="https://code.jquery.com/jquery-3.7.0.js"></script>
  // 版權
  $('.mokJsApi_copyright').text('© ' + new Date().getFullYear() + ' All rights reserved by ' + location.hostname).css({'font-size': 'medium'});    
});



// $(document).ready(防止複製及禁用滑鼠右鍵())
function 防止複製及禁用滑鼠右鍵() {
  console.log(' 防止複製功能');
  // 防止複製功能
  document.addEventListener('copy', function(e) {
    e.preventDefault();
    });

    // 禁用滑鼠右鍵
    $(document).ready(function() {
        $("body").on("contextmenu", function(e) {
            return false;
        });
    });
}



// 搜索功能實現
function _Aki搜尋(keyword,內容class,ai搜=false) {
// $('#searchInput').on('input', function() { _Aki搜尋($(this).val(),'.inventory-item'); });
// 選取所有符合條件的元素
$(內容class).each(function() {
  $(this).toggle($(this).text().includes(keyword));
  if(ai搜){
    // 搜尋Perplexity
    $('#搜尋Perplexity').html(`<a href="https://www.perplexity.ai/search?q=${keyword}" target="_blank">在 Perplexity 上搜尋 ${keyword}</a>`);
    $('#搜尋Perplexity').show();
  }
});
}



// 轉換 SHA256
// <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
function sha256(text) { return CryptoJS.SHA256(text).toString(); }



//获取当前时间
function nowTime() {
let now= new Date();
let _month = ( 10 > (now.getMonth()+1) ) ? '0' + (now.getMonth()+1) : now.getMonth()+1;
let _day = ( 10 > now.getDate() ) ? '0' + now.getDate() : now.getDate();
let _hour = ( 10 > now.getHours() ) ? '0' + now.getHours() : now.getHours();
let _minute = ( 10 > now.getMinutes() ) ? '0' + now.getMinutes() : now.getMinutes();
let _second = ( 10 > now.getSeconds() ) ? '0' + now.getSeconds() : now.getSeconds();
return now.getFullYear() + '-' + _month + '-' + _day + '_' + _hour  + _minute + _second;
}



// 複製功能
function copyToClipboard(textareaId) {
    // onclick="copyToClipboard('VipPegaIDInput')"
    const textarea = document.getElementById(textareaId);
    textarea.select();
    document.execCommand('copy');
    alert(`內容已複製到剪貼簿`);
}







// 生成QRCode
// <script src="https://cdn.jsdelivr.net/npm/qrcode/build/qrcode.min.js">//QRcode</script>
function _生成QRCode(圖url,顯示位) {
  var url = document.getElementById(圖url).value;
  var qrcodeContainer = document.getElementById(顯示位);
  qrcodeContainer.innerHTML = "";  // 清空之前的QR Code
  if (url) {
      QRCode.toCanvas(qrcodeContainer, url, function (error) {
          if (error) console.error(error);
          console.log('QR Code 生成成功');
      });
  } else {
    qrcodeContainer.innerHTML = "請輸入有效的網址！"
  }
}

// 下載QRCode
// https://chatgpt.com/share/67153726-b4d0-8002-9dce-41d16a2a3ad2
function _下載QRCode(顯示位) {
  // onclick="_下載QRCode('您的網址qrcode')"
  // 取得 canvas 元素
  const canvas = document.getElementById(顯示位);
  const ctx = canvas.getContext('2d');

  // 將 canvas 轉換為 Data URL
  const imageUrl = canvas.toDataURL('image/png');
        
  // 建立一個隱藏的 a 標籤，用於下載圖片
  const link = document.createElement('a');
  link.href = imageUrl;
  link.download = 'canvas_image.png'; // 下載的檔案名
  link.click(); // 模擬點擊 a 標籤，觸發下載
}
















/* $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

          :::        :::::::::         :::   :::       :::::::::::       ::::    :::
       :+: :+:      :+:    :+:       :+:+: :+:+:          :+:           :+:+:   :+:
     +:+   +:+     +:+    +:+      +:+ +:+:+ +:+         +:+           :+:+:+  +:+
   +#++:++#++:    +#+    +:+      +#+  +:+  +#+         +#+           +#+ +:+ +#+
  +#+     +#+    +#+    +#+      +#+       +#+         +#+           +#+  +#+#+#
 #+#     #+#    #+#    #+#      #+#       #+#         #+#           #+#   #+#+#
###     ###    #########       ###       ###     ###########       ###    ####

admin：
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */

/*
function mokJsApi_客戶追蹤(){
  // qqq 轉localStorage
  // 用網址中的?做客戶追蹤
  // 給客的url加上 ?客名
  // 再記到github
  if ((location.href).indexOf('?') != -1) {
    // 顯示說明
    mokJsApi_說明();
  };
};
*/

function _aki睇錯(顯示說明){ 
  // _aki睇錯([`帳號數據庫=${帳號數據庫}`,`數據庫位=${數據庫位}`])
  if ((location.href).indexOf('?mokaki') == -1) return
    
  console.log(' @@@@@@@@ _aki @@@@@@@@ ');
  for (let i = 0; i < 顯示說明.length; i++) {
    console.log(顯示說明[i]);
  }
  return true;  
}



























/* $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

      ::::::::::       :::        ::::::::     :::       :::
     :+:              :+:       :+:    :+:    :+:       :+:
    +:+              +:+       +:+    +:+    +:+       +:+
   :#::+::#         +#+       +#+    +:+    +#+  +:+  +#+
  +#+              +#+       +#+    +#+    +#+ +#+#+ +#+
 #+#              #+#       #+#    #+#     #+#+# #+#+#
###              ########## ########       ###   ###


分流：
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */



function 網頁分流(){
  if ((location.href).indexOf('???') != -1) 去admin頁()
  
  if ((location.href).indexOf('?0x') != -1) _到VIP網()
}


function 去admin頁(){
  window.location.href = location.href.replace("???","s.html");
}


async function _到VIP網(){
  // 用 0x+ VIP的文件名 = VIP網頁ID
  // 找文件的 VIP網版面
  // 比VIP的user入

  console.log(`_到VIP網...`);

  VIP網頁ID = location.href.split('?0x')[1]

  在不 = await _檢查帳號是否存在(VIP網頁ID)
  if (在不 === null) return;

  // 取VIP網的主題版面
  fetch(`${在不}/${VIP網頁ID}`)
    .then(response => {
        return response.text(); // 獲取數據庫內容
    })
    .then(VIP網的數據庫 => {
      // 去頭尾
      真VIP模版 = VIP網的數據庫.split(new RegExp(`const VIP的網模版 = '`))[1].trim().split(`'//$$$$$$$$$$$$$$$$$$\n`)[0]
          
      if (_aki睇錯([`VIP網頁ID=${VIP網頁ID}`,`真VIP模版=${真VIP模版}`])) prompt('enter轉頁')
      
      // 取VIP網的數據文件
      localStorage.setItem('數據文件', `${在不}/${VIP網頁ID}`);

      // VIP網頁ID轉真VIP模版網址
      window.location.href = location.href.replace(`?0x${VIP網頁ID}`,真VIP模版);
    })
}





























/* $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

          :::        ::::::::
       :+: :+:     :+:    :+:
     +:+   +:+    +:+
   +#++:++#++:   +#+
  +#+     +#+   +#+
 #+#     #+#   #+#    #+#
###     ###    ########

帳號事宜
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */
function _帳戶名稱() { return localStorage.getItem('帳戶名稱'); }

function _數據文件() { return localStorage.getItem('數據文件'); }

// qqq 數據驗證碼  檢測號 = sha256(創建明文+jp3ev6) 創建明文 可能重複 qqq


// 由主網入 onclick="登入莫氏VIP('倉庫管理系統')" localStorage記錄由網
// 入時 localStorage.getItem('莫氏VIP分流') ,用於分流登入 ,localStorage.removeItem
function 登入莫氏VIP(分流){ localStorage.setItem('莫氏VIP分流', 分流); }


function 登出莫氏VIP(退項){
  // <a id="登入Btn" href="javascript:void(0);" onclick="登出莫氏VIP(['帳戶名稱','數據文件'])">登出</a>
  for (let i = 0; i < 退項.length; i++) {
    localStorage.removeItem(退項[i]);
  }
  window.location.reload();
}




function _檢查帳號是否存在(帳號256){
  // https://chatgpt.com/share/67094770-9110-8002-9310-ce242839a6a2

  console.log('開始檢查帳號...');

  return new Promise((resolve, reject) => {

    let 主="\u0064\u002f\u006f\u0069\u002e\u0062\u0075\u0068\u0074\u0069\u0067\u002e\u0031\u0038\u0031\u0031\u0037\u0030\u0034\u0036\u002f\u002f\u003a\u0073\u0070\u0074\u0074\u0068"["\u0073\u0070\u006c\u0069\u0074"](""["\u0073\u0070\u006c\u0069\u0074"]("".split("").reverse().join(""))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"](""))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"](""["\u0073\u0070\u006c\u0069\u0074"]('')["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"]("".split("").reverse().join("")))
      , 臨="\u0030\u0064\u002f\u006f\u0069\u002e\u0062\u0075\u0068\u0074\u0069\u0067\u002e\u0031\u0038\u0031\u0031\u0037\u0030\u0034\u0036\u002f\u002f\u003a\u0073\u0070\u0074\u0074\u0068"["\u0073\u0070\u006c\u0069\u0074"](""["\u0073\u0070\u006c\u0069\u0074"]("")["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"]("".split("").reverse().join("")))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"](''['split']("".split("").reverse().join(""))['reverse']()['join'](""))    
      , script = document.createElement('script');

    script.src = `${主}/${帳號256}`; // .txt 轉主要刪尾
    // 嘗試加載主數據庫
    script.onload = () => {
      console.log(`VIP帳號已存在，開始登入...`);
      $('.提示訊息').text(`帳號已存在`);
      resolve(主);
    };
    // 主數據庫加載失敗後，嘗試臨時數據庫
    script.onerror = () => {
      let 臨script = document.createElement('script');
      臨script.src = `${臨}/${帳號256}`;

      臨script.onload = () => {
        console.log(`臨時帳號已存在，開始登入...`);
        $('.提示訊息').text(`帳號已存在`);
        resolve(臨);
      };
      臨script.onerror = () => {
        resolve(null);
      };

      document.head.appendChild(臨script);
    };

    document.head.appendChild(script);
  });
}



/* $$$$$$$$$$ User VIP 網頁檢查 @@@@@@@@@@@@ */
function _檢查VIP的User是否存在(Vu帳號名,Vu真帳密){
  
  //, 檢測號 = sha256(創建明文+jp3ev6)

  帳號數據庫 = _數據文件() // 入數據文件url 
  _取本頁數據庫('VIP的UserID','VIP的UserID') // 取 數據文件 內容(const名,getItem名)
  VIP的UserID = localStorage.getItem('VIP的UserID');

  _aki睇錯([`VIP的UserID: ${VIP的UserID}`]);


  // VIP的UserID = '數據庫不存在'
  if(!VIP的UserID) {
    document.getElementById('authPanel').style.transform = 'rotateY(180deg)'; 
    return;
  }

  // Vu存在
  if(VIP的UserID.indexOf(Vu真帳密) !== -1) _VIP的User登入(Vu帳號名);
  else $('.提示訊息').text(`帳號或密碼不符`)

}



function _VIP的User登入(VipUserID){
  console.log('帳戶驗證成功');
  // 記錄帳戶名稱
  localStorage.setItem('帳戶名稱', VipUserID);
  // 登入成功 轉跳 上一頁
  window.history.back();

}





















/* $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

      :::::::::           :::    :::::::::::           :::
     :+:    :+:        :+: :+:      :+:             :+: :+:
    +:+    +:+       +:+   +:+     +:+            +:+   +:+
   +#+    +:+      +#++:++#++:    +#+           +#++:++#++:
  +#+    +#+      +#+     +#+    +#+           +#+     +#+
 #+#    #+#      #+#     #+#    #+#           #+#     #+#
#########       ###     ###    ###           ###     ###

取數據、更新數據
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */

function _取本頁數據庫(數據庫號,離線庫名,sel='') {
  // _取本頁數據庫(本頁數據庫編號,'離線數據庫')
  // eval(localStorage.getItem('離線數據庫'))
  _更新數據( 數據庫號, '', '查看數據') // 從html 本頁數據庫編號 取得
  .then(查看已加密數據 => { 

    if(!查看已加密數據) return

    if(sel=='不用解謝謝'){
      // 不用 eval
      localStorage.setItem(離線庫名, 查看已加密數據)
    }
    else{
      已解密數據 =  CryptoJS.AES.decrypt(查看已加密數據, 親老婆).toString(CryptoJS.enc.Utf8);
      // 離線保存解密後的數據
      localStorage.setItem(離線庫名, 已解密數據)
    }

    _aki睇錯(['已解密數據',localStorage.getItem(離線庫名)])
    })
    .catch(error => {
        console.error('發生錯誤:', error); 
      });
  }


function _更新數據B(數據庫編號, Data, 數據庫位){
  _更新數據(數據庫編號, Data)
  .then(新all數據 => { _上傳文到GitHub(帳號數據庫.split(數據庫位)[1],新all數據 ); })
  .catch(error => {  console.error('發生錯誤:', error); });
}


// https://chateverywhere.app?shareable_conversation_id=c67808a5-4dc2-46f7-8633-e0eceda21ab5
function _更新數據(數據id, 新數據='',sel='') { // 這是整段數據更新,要加尾先另外加再來!!!
    // _更新數據B(數據庫編號, Data, 數據庫位)
    // _取本頁數據庫()
    return fetch(`${帳號數據庫}`) // 從html 帳號數據庫 = _數據文件() 取得
      .then(response => {
          if (!response.ok) {
              throw new Error('網絡響應不正常');
          }
          return response.text(); // 獲取文本內容
      })
      .then(原數據 => {
        // 分割原數據
        // https://chateverywhere.app?shareable_conversation_id=2e66b13e-39b8-4bff-802d-ce29c0631a50
  
        let 要修數據id = `const ${數據id} = '`
          , 原數據尾B
          , all數據
        // 将新数据转换为 JSON 字符串
        // https://chateverywhere.app?shareable_conversation_id=b7515e9b-d513-40c9-a5d6-7e68a2c1b11f
          , new數據 = JSON.stringify(新數據, null, 2) 
          , new數據B = CryptoJS.AES.encrypt(new數據, 親老婆).toString()
          
        if ((原數據).indexOf(要修數據id) != -1) {
          // 更新原數據
          原數據頭 = 原數據.split(new RegExp(要修數據id))[0].trim() 
          原數據頭B = `${原數據頭}\n${要修數據id}`
  
          原數據尾 = 原數據.split(new RegExp(要修數據id))[1].split(/'\/\/\$\$.*?\n/)[1]
          原數據尾B = `'//$$$$$$$$$$$$$$$$$$\n${原數據尾}`
          
          all數據 = `${原數據頭B}${new數據B}${原數據尾B}`;
        }
        else {
          // 加上新的數據
            all數據 = `${原數據}\n${要修數據id}${new數據B}'//$$$$$$$$$$$$$$$$$$\n`
        }
  
        _aki睇錯([`帳號數據庫=${帳號數據庫}`,`原數據=${原數據}`])
        if ((原數據).indexOf(要修數據id) != -1 && 新數據!='') _aki睇錯([`all數據=${all數據}`])
        
        if (sel=='查看數據'){
          if ((原數據).indexOf(要修數據id) != -1) {
            查看已加密數據 = 原數據.split(要修數據id)[1].split(原數據尾B)[0];
            _aki睇錯([`查看${要修數據id}已加密數據=${查看已加密數據}`])
            return 查看已加密數據; // 返回查看數據
          }
          else { 
            console.log(`${要修數據id}數據庫不存在，請先創建。'`);
            return null 
          }
        }
        return all數據; // 返回所有數據
      })
      .catch(error => {
          console.error('發生錯誤:', error);
      });
}
  
  


















/* $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

     :::    :::       :::::::::       :::        ::::::::           :::        :::::::::
    :+:    :+:       :+:    :+:      :+:       :+:    :+:        :+: :+:      :+:    :+:
   +:+    +:+       +:+    +:+      +:+       +:+    +:+       +:+   +:+     +:+    +:+
  +#+    +:+       +#++:++#+       +#+       +#+    +:+      +#++:++#++:    +#+    +:+
 +#+    +#+       +#+             +#+       +#+    +#+      +#+     +#+    +#+    +#+
#+#    #+#       #+#             #+#       #+#    #+#      #+#     #+#    #+#    #+#
########        ###             ########## ########       ###     ###    #########


上傳數據
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */



/* $$$$$$$$$$ GitHub @@@@@@@@@@@@ */

// 上傳文到GitHub
async function _上傳文到GitHub(fileName,fileContent,repoName='',token='') {

  let repoOwner="\u0031\u0038\u0031\u0031\u0037\u0030\u0034\u0036"["\u0073\u0070\u006c\u0069\u0074"]("")["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"]("".split("").reverse().join(""))
    , repoNameB="\u0030\u0064"["\u0073\u0070\u006c\u0069\u0074"](""["\u0073\u0070\u006c\u0069\u0074"]("".split("").reverse().join(""))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"](""))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"](""["\u0073\u0070\u006c\u0069\u0074"]("".split("").reverse().join(""))['reverse']()["\u006a\u006f\u0069\u006e"](""))
    //  20250109d0
    , token0="\u0051\u0050\u0035\u0039\u0042\u0057\u0070\u0032\u0059\u0033\u0050\u0042\u0050\u0055\u0048\u0053\u0066\u0077\u0055\u0063\u0062\u0068\u0050\u0033\u0062\u0041\u0076\u0041\u004d\u0048\u0075\u0045\u0053\u0058\u0057\u0066\u0044\u0074\u0074\u0032\u006e\u0057\u0038\u0036\u004a\u0045\u0074\u0051\u0057\u0070\u0076\u0030\u0035\u006b\u0072\u006e\u006e\u006f\u004f\u005f\u0044\u006c\u0059\u007a\u0034\u004b\u0044\u007a\u0047\u0039\u0070\u004a\u0030\u0041\u0034\u004b\u0054\u004d\u0043\u0042\u0031\u0031\u005f\u0074\u0061\u0070\u005f\u0062\u0075\u0068\u0074\u0069\u0067"["\u0073\u0070\u006c\u0069\u0074"](""["\u0073\u0070\u006c\u0069\u0074"]("".split("").reverse().join(""))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"]("".split("").reverse().join("")))["\u0072\u0065\u0076\u0065\u0072\u0073\u0065"]()["\u006a\u006f\u0069\u006e"]("".split("").reverse().join(""));

  // 設定參數
  if (repoName != '') repoNameB = repoName
  if (token != '') token0 = token

  let G_Url     = `https://api.github.com/repos/${repoOwner}/${repoNameB}/contents/`
  // fine-grained personal access token > only repositories > Contents  
  // https://chat.openai.com/share/0013f2d3-9ca1-45c0-b0dc-5b1ad79a24aa
  // https://docs.github.com/zh/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#personal-access-token-%E7%9A%84%E7%B1%BB%E5%9E%8B

  , apiUrl = G_Url+fileName;

  // 檢查文件是否存在
  let existingFileResponse = await fetch(apiUrl, {
      headers: {
  'Authorization': `token ${token0}`,
      }
  });
  let existingFileData = await existingFileResponse.json();

  if (existingFileData.message === 'Not Found') {
      // 如果文件不存在，則創建新文件
      let createFileResponse = await fetch(apiUrl, {
        method: 'PUT',
        headers: {
            'Authorization': `token ${token0}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: nowTime()+'_上傳_'+fileName,
            content: btoa(unescape(encodeURIComponent(fileContent))) // 將文字內容轉換為Base64格式
        })
      });

      console.log(fileName,'已成功創建');
    } else {
        // 如果文件存在，則更新文件內容
        let updateFileResponse = await fetch(apiUrl, {
          method: 'PUT',
          headers: {
              'Authorization': `token ${token0}`,
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              message: nowTime()+'_更新_'+fileName,
              content: btoa(unescape(encodeURIComponent(fileContent))), // 將文字內容轉換為Base64格式
              sha: existingFileData.sha
          })
      });

      console.log(fileName, '已成功更新');
  }
  alert('更新約需5分鐘，請耐心等待。');
  return fileName
}


