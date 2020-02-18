from pytube import YouTube
import os

#以os指定影片下載到哪個資料夾，若不存在此資料夾則建立新資料夾
pathdir = "E:\\temp"
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)

#在 pytube 的 YouTube 這個 class 當中，存在著 “on_progress_callback” 可以自行編寫進度條
def progress(stream, chunk, file_handle, bytes_remaining):
    contentSize = yt.streams.filter(subtype='mp4',res='360p',progressive=True).first().filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

url = input('請輸入要下載的影片網址')  #要下載的影片網址
yt = YouTube(url,on_progress_callback=progress)
count = yt.streams.count()  #用count方法抓到影片格式的數量
print(yt.title + '影片格式共有：'+ str(count) + '種')  #要記得將count轉為字串格式
print( 'mp4 360p 影片下載中，請稍後') 
yt.streams.filter(subtype='mp4',res='360p',progressive=True).first().download(pathdir)
#用filter篩選影片格式及解析度等，再下載第一個符合條件的影片，並下載到指定資料夾
print(yt.title + '影片下載完成~')
