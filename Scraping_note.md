在寫爬蟲程式時，第一步就是`發送網路請求`，而在Python中有Python內建的`urllib`以及`requests`模組可以
完成這件事，而究竟這兩者究竟哪個比較好或是和使用呢？

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
