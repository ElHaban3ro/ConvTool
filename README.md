# ConvTool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellowgreen.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-310/) [![PyPi Package](https://img.shields.io/badge/PyPi_Package-pip_install_ConvTool-yellow.svg?style=flat-square&logo=pypi)](https://pypi.org/project/ConvTool/)




## Summary and details
---
A unified **package** to convert your videos or images to another **image**/**video** format. Convert a whole ***folder*** from that **format** to a different one, or if you prefer, *convert just one*!

- Python Version: **3.10**
- Pip Version: **The Lastest version**





## Functions
---

#### - conv_video(route, convert_to, folder, delete_original)
> Convert your video files, or an ENTIRE folder with video files to a different format!

- ***Parameters:*** 
    
    - route: **string** | Path of your file or folder to convert!

    - convert_to: **string** | Format you want to convert the files to.

    - folder: **boolean** | If you want to convert a folder with video files, this has to be set to True. 

    - delete_original: **boolean** | If you want that when converting the file to the desired format, the original file is completely deleted, you should leave this parameter to True.
  
> Remember that the formats supported are:

  - MP4
  - MOV
  - WAV
  - AVI
  - FLV
  - MKV

---

#### - conv_image(route, convert_to, folder, delete_original)
> Convert your image files, or an ENTIRE folder with image files to a different format!

- ***Parameters:*** 
    
    - route: **string** | Path of your image or folder to convert!

    - convert_to: **string** | Format you want to convert the image to.

    - folder: **boolean** | If you want to convert a folder with images files, this has to be set to True. 

    - delete_original: **boolean** | If you want that when converting the image to the desired format, the original image is completely deleted, you should leave this parameter to True.
  
> The formats supported are:

  - BMP
  - GIF
  - JPG
  - JPEG
  - PNG
  - ICO
  - TIFF




## Use
---

#### Installation:
To use this package, the best idea is to do it through ***pip***:
```bash
pip install ConvTool
```
***IT IS VERY IMPORTANT THAT THE "C" AND THE "T" ARE CAPITALIZED.***


Or, on the contrary, you can **clone** this repository and access it:
```bash
git clone https://github.com/ElHaban3ro/ConvTool
```

This will create a folder of the project itself inside your python root project. Next we have to install the necessary dependencies for the project to work correctly, this can be done with:
```bash
pip install -r requirements.txt 
```

This would **ideally** have to install all the necessary libraries for you. This will be installed in the ***virtual environment*** of your project. See how to create a [virtual environment here]('https://docs.python.org/3/tutorial/venv.html').


#### Use:

To ***import*** and use any **module**, do it as follows (if you **cloned** the repository, ***make sure*** it is in the root of your **project**):
```python
from ConvTool.ConvTool import conv_video
```

And with that done, start using it as follows:

```python
from ConvTool.ConvTool import conv_video

conv = conv_video(folder = False, convert_to = 'mp4', delete_original = True, route = r'miruta/archivo.mov')
```

*Now run!*




# (v1.0) Images Update. ¿What's New?
- Support for converting images to different formats!
- Cleaner code (a bit :c)
- Intentions to add support for converting text files in next updates!





# Autor Contact
---

[![Contact Twitter](https://img.shields.io/badge/Twitter-ElHaban3ro-9cf.svg?style=for-the-badge&logo=twitter)](https://twitter.com/ElHaban3ro) [![Contact Discord](https://img.shields.io/badge/Discord-!%20Die()%231274-lightgray?style=for-the-badge&logo=discord)](https://discord.com) [![Contact Discord](https://img.shields.io/badge/GitHub-ElHaban3ro-lightgray?style=for-the-badge&logo=github)](https://github.com/ElHaban3ro)