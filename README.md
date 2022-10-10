# ConvTool

## Summary and details
---
This library makes use of ***MoviePy*** (not the one I have in my github, it is another library intended to work with video files). The main idea of this project is that you can convert your video files in a considerably easy way. Convert your entire **folders** or **video files** with ***ConvTool***. In the future I will be creating a version that supports many more formats and even a graphical interface.

- Python Version: **3.10**
- Pip Version: **The Lastest version**
- MoviePy Version: **1.0.3**





## Functions
---

- Convert your video files, or an ENTIRE folder with video files to a different format! ( **conv_video()** ) 
    - ***Parameters:*** 
        
        - route: **string** | Path of your file or folder to convert!
    
        - convert_to: **string** | Format you want to convert the files to.
    
        - folder: **boolean** | If you want to convert a folder with video files, this has to be set to True. 
    
        - delete_original: **boolean** | If you want that when converting the file to the desired format, the original file is completely deleted, you should leave this parameter to True.


## Use
---

If you want to use what is currently the only function, you must import the library, pass the corresponding parameters and execute! Here is an example:

```python
from ConvTool import conv_video
```

And with that done, start using it as follows:

```python
conv = conv_video(folder = False, convert_to = 'mp4', delete_original = True, route = r'miruta/archivo.mov')
```

Now run!











## Instalation
---

Make git clone of the project with:

```bash
git clone https://github.com/ElHaban3ro/ConvTool.git
```

This will create a folder of the project itself inside your python root project. Next we have to install the necessary dependencies for the project to work correctly, this can be done with:
```bash
pip install -r requirements.txt 
```

This would **ideally** have to install all the necessary libraries for you. This will be installed in the ***virtual environment*** of your project. See how to create a [virtual environment here]('https://docs.python.org/3/tutorial/venv.html').







# Autor Contact
---

- Discord: ***! Die()#1274***
- [Twitter Profile @ElHaban3ro](https://twitter.com/elhaban3ro)
- [Github Profile @ElHaban3ro](https://github.com/ElHaban3ro)