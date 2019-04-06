在寫爬蟲程式時，第一步就是發送網路請求，而在Python中有Python內建的`urllib`以及`requests`模組可以完成這件事，而究竟這兩者究竟哪個比較好或是和使用呢？

Note:
``` bash
在Python2.x中，內建的稱為urllib2庫。而在Python3.x後， urllib2被改名為urllib。
```

上網搜尋以後，發現一片導向偏好使用`requests`模組，而`requests`模組到底有什麼好的呢？

優點：
1. 程式碼短且易於理解。

Example:
```Python
import requests
r = requests.get('https://api.github.com/events')
```

由以上`Python code`，我們可以清楚知道我們發送`get request`給一個`github`網址。

2. requests模組完美的與`RESTful API`結合。

Example(from stackoverflow):
```Python
import requests
resp = requests.get('http://www.mywebsite.com/user')
resp = requests.post('http://www.mywebsite.com/user')
resp = requests.put('http://www.mywebsite.com/user/put')
resp = requests.delete('http://www.mywebsite.com/user/delete')
```

在送出`post request`時，通常會連同資料一起送出，使用`requests`模組處理的方式也相當簡單。

Example:
```Python
import requests
userdata = {"name": Jay, "number": 32}
resp = requests.post('http://www.mywebsite.com/user', data=userdata)
```

那什麼是RESTful API呢？
Note:
``` bash
REST的全稱為Representational State Transfer，他屬於一種網路架構風格，
但他並非一種強制標準，故網站不一定要依此架構建構。
而以REST形式打造的網頁，也就可稱為RESTful形式。
```

3. 輕鬆將網站回傳的response進行轉換。

它具有`json decoder`，故我們可用以下把response轉為json形式。
```Python
resp.json()
```

如果response僅是一個文字檔，我們也可把它輕鬆回傳並使用它。
```Python
resp.text
```

除了以上，`requests`模組對於`Session`、`cookies`等等的處理也相對簡單、方便，許多部分目前我也曾未接觸過，就留由後續等待接觸到再一一摸索。
