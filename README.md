# Discord Sign Bot
Hi! This is Discord Sign Bot code  
You just need to follow the steps

  1. Downland [
Disocrd Sign Bot](https://github.com/Coca-Sprite/Discord-Sign-Bot/blob/main/main.py) in ur server or computer.

  2. install datetime  
```  
pip install datetime  
```  
  3.  
```  
pip install discord.py  
```  
  4. Replace "Your_Token" with your Token  
  
  5. Use **admin** run the code(Prevent messages from being saved due to insufficient permissions)  

## If there is insufficient permission, it may result in the following error:  
1.
```py
Ignoring exception in on_message
Traceback (most recent call last):
  File "Ur Discord.py install file", line 343, in _run_event
    await coro(*args, **kwargs)
  File "file.py", line 42, in on_message
    with open(f"./sign_log.txt", "a", encoding='utf8') as log:
FileNotFoundError: [Errno 2] No such file or directory: './sign_log.txt'
```   
2.*[**Closing without reason**]*

### 創用CC標示  
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/tw/"><img alt="創用 CC 授權條款" style="border-width:0" src="https://i.creativecommons.org/l/by/3.0/tw/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/InteractiveResource" property="dct:title" rel="dct:type">Discord Sign Bot</span>由<span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Jiang Sprite</span>製作，以<a rel="license" href="http://creativecommons.org/licenses/by/3.0/tw/">創用CC 姓名標示 3.0 台灣 授權條款</a>釋出。<br />此作品衍生自<a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/Coca-Sprite/Discord-Sign-Bot/" rel="dct:source">github.com</a>。
