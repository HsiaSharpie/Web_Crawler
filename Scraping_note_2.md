延續前一篇，我們使用`requests`模組發送網路請求後，接著可使用`BeautifulSoup`類別庫去解析它。
但在發送網路請求時可能會遇到一些狀況，例如：「404 Page Not Found」、「500 Internal Server Error」等問題，會造成我們無法正常解析回傳的檔案。

而在這些狀況發生時，函式會丟出`RequestException`此種例外狀況。為了避免一遇到這種狀況程式就直接暫停，我們可以使用`try/except`方法以讓程式繼續執行。

```Python
try:
    resp = requests.get(url)
    print(resp.status_code)
except requests.exceptions.RequestException as e:
    print(e)
    return None
```

由以上的範例，我在try中試著對目標url發送`get request`，如果成功回傳response則我們印出它的`status code`。
Note:
``` bash
當status code為200時，表時請求是成功的。
```

若請求失敗，則我們會印出失敗的原因，並回傳`None object`。

在`requests.exceptions`下，我們可以去看看`Class RequestException`的`Source code`。

![](https://i.imgur.com/PldagGO.png?1)
