# Youtube_download
## 下載Youtube 影片
### 聲明：此程式為學習使用，影片下載後將立即刪除，絕無他用。

專題目標：透過Youtube模組來達成自動下載影片，並可選擇影片格式及解析度。

1. 透過pip 安裝pytube3(原先的pytube模組已無法使用)，並且import道專案中：
```
pip install pytube3
```
```
from pytube import YouTube
```

2. 找到中意的Youtube影片，儲存該網址
```
url = Youtube影片網址
```
 3. 利用streams方法可以取得所有影片格式，其中的filter方法可以指定傳回的影片格式
```
yt = Youtube(url).streams.filter(subtype = 'mp4')
```

影片格式
streams方法取得影片所有格式，下列主要方法可對格式進一步操作：


| 方法 | 功能 | 語法範例 |
| ---- | ---- | -------- |
| all() | 傳回影片所有格式 |yt.streams.all()|
| first()|傳回第一個影片格式|yt.streams.first()|
| last() |傳回最後一個影片格式|yt.streams.last()|
| filter() |傳回符合指定條件的影片格式|yt.streams.filter(subtype='mp4'|
| count()|傳回影片格式數量|yt.streams.count()|

---
filter的條件如：

| 條件 | 功能 | 語法範例 |
| ---- | ---- | -------- |
| progressive |篩選"同時"具有影片及聲音的格式|progressive=True|
| adaptive|篩選只具有影像"或"聲音其中之一的格式|adaptive=True|
| subtype|篩選指定影片類型的格式|subtype='mp4'|
| res| 篩選指定解析度的格式 |res='720p'|
---
4. 使用os模組，可以指定影片下載的資料夾
```
import os
#如果資料夾不存在，則新建一個資料夾
pathdir = "E:\\temp"
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
```

5. Youtube Class中存在著 “on_progress_callback” 可以自行編寫進度條，並將其加入Youtube的參數
```
def progress(stream, chunk, file_handle, bytes_remaining):
    contentSize = yt.streams.filter(subtype='mp4',res='360p',progressive=True).first().filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

    yt = YouTube(url,on_progress_callback=progress)
```
6. 最後加上download方法即可下載指定格式的影片，並存在指定資料夾中
```
yt.streams.filter(subtype='mp4',res='360p',progressive=True).first().download(pathdir)
```
