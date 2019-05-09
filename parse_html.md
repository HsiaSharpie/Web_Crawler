在`Parse HTML`的時候，許多人都是由先由`Beautifulsoup`著手，因為我也是XD
<br>不過，前不久接觸到另一個解析HTML的工具，叫做`request_html`，也是由`requests`函式庫的開發者所開發。
<br>它的主旨是："HTML Parsing for Humans!"，就是希望能讓使用者能更簡單、直覺地操作。

而在`request_html library`的官方`Github`上，有特別介紹當你使用`request_html`之優點：
<br>以下：
``` bash
1. Full JavaScript support!
2. CSS Selectors (a.k.a jQuery-style, thanks to PyQuery).
3. XPath Selectors, the faint at heart.
4. Mocked user-agent (like a real web browser).
5. Automatic following of redirects.
6. Connection–pooling and cookie persistence.
7. The Requests experience you know and love, with magical parsing abilities.
8. Async Support
```
特別是第一點與第八點，是作者特別強調的重點，在後面會有一點點介紹。

同樣地以`ptt-gossip`版為例子。
<br>假設，我們今天想爬下一個頁面中的所有文章標題，以`request_html`實作的話，該如何著手？
<br>Review: 由前篇之`get_web_page`函數，我們回傳了`resp.text`。

``` Python
from requests_html import HTML

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
resp_text = get_web_page(url)

def get_web_title(doc):
  html = HTML(html=doc)
  titles = html.find('div.r-ent')
  return titles

titles = get_web_title(resp_text)
print(titles)
```
