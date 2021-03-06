延續前一篇，我們使用`requests`模組發送網路請求後，接著可使用`BeautifulSoup`包去解析它。
但在發送網路請求時可能會遇到一些狀況，例如：「404 Page Not Found」、「500 Internal Server Error」等問題，會造成我們無法正常解析回傳的檔案。

而在這些狀況發生時，函式會丟出`RequestException`此種例外狀況。為了避免一遇到這種狀況程式就直接暫停，我們可以使用`try/except`方法以讓程式繼續執行。

Example:
```Python
def get_web_page(url):
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

若請求失敗，則我們會印出失敗的原因，並回傳`None object`。而`RequestException`是一個在`requests.exceptions`下，的一個`Class`。

假設我的目標是要取得這個網頁的標題，且由上面的code我可以知道我的`get request`是否請求成功。接著，就可以透過`BeautifulSoup`去解析他了。

我們在前面遇到了可能會因為找不到頁面、連不到主機等問題而出現例外。同樣地問題，我們在透過`BeautifulSoup`解析後，也可能因為對不存在的資料進行處理而發生另一種叫做`AttributeError`的例外。

結合上面的 get_web_page() ，把它寫成一個 get_web_title 函式。
```Python
def get_web_title(url):
  try:
    resp = requests.get(url)
    print(resp.status_code)
  except requests.exceptions.RequestException as e:
    print(e)
    return None
  try:
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.body.h1
  except AttributeError as e:
    print(e)
    return None
  return title
```

透過`BeautifulSoup`解析後，我們會取得一個`BeautifulSoup物件`，在上述例子我把它丟給soup。接著，就可以直接對`BeautifulSoup物件`去取標籤，如果此時要取的標籤是不存在的，`BeautifulSoup`會回傳一個`None object`。

如果你還想對這個`None object`做什麼動作，則會拋出`AttributeError`。

Note:
``` bash
在利用try/except處理例外情形的時候，要盡量避免在try的區塊中放入太多的code。
假設今天拋出了例外，但你可能會無法判斷出到底是哪行了產生了例外！
```
