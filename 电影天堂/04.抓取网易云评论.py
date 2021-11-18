# 1.找到未加密的参数
# 2.先办法把参数加密（参照网易的逻辑），params = "encText"，encSecKey = "encSecKey"
# 3.请求到网易，拿到评论信息
# 需要安装pycrypto ：pip install pycryptodome
import requests
from Crypto.Cipher import AES

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203",
    "referer": "https://music.163.com/song?id=1859925367"
}
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

d = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",       # pageNo 评论的页码
    "pageSize": "20",
    "rid": "R_SO_4_1859925367",    #  R_SO_4_{歌曲id}
    "threadId": "R_SO_4_1859925367"
}

e = "010001"

f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

g = "0CoJUm6Qyw8W8jud"

i = "TY3HBIatS4xMw5tm"

"""
    !function() {
    function a(a = 16) {            #返回的随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)          #for循环执行16次
            e = Math.random() * b.length,   #随机数     2.544962566
            e = Math.floor(e),              #取整       2
            c += b.charAt(e);               #取字符串中的xxx位置     abc 取 c
        return c
    }
    function b(a, b) {      # a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b)      #  这时b是加密的密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)    # 到这e成了数据
          , f = CryptoJS.AES.encrypt(e, c, {   # 此时c是加密的密钥
            iv: d,     #偏移量
            mode: CryptoJS.mode.CBC    #加密模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {               # c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d: 数据   e,f,g :固定的
        var h = {}     #创建一个空对象 
          , i = a(16);     # i就是一个16位的随机字符串，把i设置成定值
        return h.encText = b(d, g), #  这是的g是密钥
        h.encText = b(h.encText, i), # 返回的就是params   i也是密钥
        h.encSecKey = c(i, e, f),       #这里得到的是encSecKey，e和f是定死的， 如果此时把i固定, 得到的一定是固定的。
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
}();

两次加密：
数据+g =》 b =》 第一次加密+i =》 b = params

"""

def get_encSecKey():
    return "3f5325706db4a1c04b790f165b26b69646494608a44bafabc9082b560d4f06f34ec6bda7ba424af01fa0e07d0f392097b855ba57e795e81dde300c211e1c6076da1233db6a11b2fa13897be0a18a79c2437771fed8803ab31a8b668b7068cdf763d9a8fdb34e453fcb331b4af9dc6358a9991a2b7e230e5c60a452d5ade1116f"

def get_params(data):   #默认收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second
    pass


def enc_params(data, key):   #加密过程
    aes = AES.new()  #创造加密器
    aes.encrypt()       #加密
    pass



resp = requests.post(url, headers=header)
print(resp.text)






































































