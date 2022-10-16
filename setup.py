from setuptools import setup
# EJECUTA ESTO CON: py -m build
# and upload with:  twine upload dist/*


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


# with open('./requirements.txt', 'rb') as f:
#     requirements = f.read().splitlines()





setup(
    name = 'ConvTool',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['ConvTool'],
    version = '1.0',
    license = 'MIT',
    description = 'A unified package to convert your videos or images to another image/video format. Convert a whole folder from that format to a different one, or if you prefer, convert just one! 🥵',
    author = 'ElHaban3ro',
    author_email = 'habanferd@gmail.com',
    url = 'https://github.com/ElHaban3ro/ConvTool',
    keywords = 'python converter video-processing video-converter image-processing image-converter',
    classifiers = [
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=['moviepy==1.0.3', 'Pillow==9.2.0']
)