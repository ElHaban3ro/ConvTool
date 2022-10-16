# Libraries
import os
from moviepy.editor import VideoFileClip



# noinspection PyShadowingBuiltins
def conv_video(route: str, convert_to: str, folder=False, delete_original=False):
    """
    Convert your video files, or an ENTIRE folder with video files to a different format!


    Parameters
    ----------

    route: **string** | Path of your file or folder to convert!

    convert_to: **string** | Format you want to convert the files to.

    folder: **boolean** | If you want to convert a folder with video files, this has to be set to True. 

    delete_original: **boolean** | If you want that when converting the file to the desired format, the original file is
    completely deleted, you should leave this parameter to True.

    """

    video_formats = ['.mp4', '.mov', '.wav', '.avi', '.mkv', '.flv', '.wmv', '.MP4', '.MOV', '.WAV', '.AVI', '.MKV',
                     '.FLV', '.WMV', '.Mov', '.Wav', '.Avi', '.Mkv', '.Flv', '.Wmv']

    if folder:

        if f'.{convert_to}' in video_formats:

            folder_files = os.listdir(route)  # List directory.
            files = []

            for video_file in folder_files:
                for format in video_formats:
                    if format in video_file:
                        files.append(video_file)

            if route.find('\\') >= 1:
                actual_folder = route.split('\\')[-1]

                route_split = route.split('\\')[:-1]
                route_without_folder = ''

                for e, folder in enumerate(route_split):
                    if e >= 1:
                        route_without_folder = f'{route_without_folder}/{folder}'

                    else:
                        route_without_folder = f'{folder}/'

            else:
                actual_folder = route.split('/')[-1]

                route_split = route.split('/')[:-1]
                route_without_folder = ''

                for e, folder in enumerate(route_split):
                    if e >= 1:
                        route_without_folder = f'{route_without_folder}/{folder}'

                    else:
                        route_without_folder = f'{folder}/'

            for file in files:
                extension = file[::-1].split('.')[0][::-1]
                video = VideoFileClip(f'{route}/{file}')

                new_folder_name = f'[CT - Folder] {actual_folder}'

                try:
                    os.mkdir(f'{route}/{new_folder_name}')

                except FileExistsError:
                    print('Se ha intentado crear una carpeta ya existente.')

                video.write_videofile(
                    f'{route}/{new_folder_name}/{file[:len(file) - (len(extension) + 1)]}.{convert_to}')

                if delete_original:
                    os.remove(f'{route}/{file}')

                print('Hemos convertido tu carpeta de manera satisfactoria! Revisala.')

        else:
            print('We not found your format :(')

    else:
        # SI LO QUE SE QUIERE CONVERTIR ES ESTO, LO QUE VAMOS A HACER ES LO SIGUIENTE, PERO,
        # LAS VARIACIONES QUE SE TIENEN SON CONSIDERABLEMENTE MINIMAS:
        if f'.{convert_to}' in video_formats:

            if route.find('\\') >= 1:
                actual_file = route.split('\\')[-1]

                route_actual_folder = route.split('\\')[:-1]
                route_without_file = ''

                for e, folder in enumerate(route_actual_folder):
                    if e >= 1:
                        route_without_file = f'{route_without_file}/{folder}'

                    else:
                        route_without_file = f'{folder}/'

            else:
                actual_file = route.split('/')[-1]

                route_actual_folder = route.split('/')[:-1]
                route_without_file = ''

                for e, folder in enumerate(route_actual_folder):
                    if e >= 1:
                        route_without_file = f'{route_without_file}/{folder}'

                    else:
                        route_without_file = f'{folder}/'

            extension = actual_file[::-1].split('.')[0][::-1]

            video = VideoFileClip(f'{route_without_file}/{actual_file}')

            new_folder_name = f'[CT - File] {actual_file[:len(actual_file) - (len(extension) + 1)]}'

            try:
                os.mkdir(f'{route_without_file}/{new_folder_name}')

            except ValueError:
                pass

            video.write_videofile(
                f'{route_without_file}/{new_folder_name}/{actual_file[:len(actual_file) - (len(extension) + 1)]}.{convert_to}')

            if delete_original:
                os.remove(f'{route_without_file}/{actual_file}')

            print('Hemos convertido tu archivo de manera satisfactoria! Revisalo.')


def conv_image(route: str, convert_to: str, folder=False, delete_original=False):
    imgs_formats = ['BMP', 'GIF', 'JPG', 'JPEG', 'PNG', 'Bmp', 'Gif', 'Jpg', 'Jpeg',
                    'Png', 'bpm', 'gif', 'jpg', 'jpeg', 'png']  # Formats Avalable

    if folder:
        # Directory Started Config.
        content_acutal_folder = os.listdir(route)  # The list of absolutely all files in the given folder.

        files_extensions = []  # List of the image extensions.
        files_names = []  # List of the images names.

        for content in content_acutal_folder:
            file_extension = content[::-1][:content[::-1].find('.')][::-1]  # Extract file extension.
            file_name = content[::-1][content[::-1].find('.'):][::-1][:-1]  # Extract file name.

            if file_extension in imgs_formats:  # Validates if the file extension is in our
                # list of supported formats.

                files_names.append(file_name)  # Add name!
                files_extensions.append(file_extension)  # Add extension

        # Convert image folder:


    else:
        # Directory Started Config.
        actual_folder = os.path.dirname(route)  # Sets the current folder.
        actual_file = os.path.basename(route)  # Sets the current file.

        file_extension = actual_file[::-1][:actual_file[::-1].find('.')][::-1]  # Sets the file extension.
        file_name = actual_file[::-1][actual_file[::-1].find('.'):][::-1][:-1]  # Sets the file name.

        # Convert Image:


conv_image(
    r'C:\Users\ferdh\Desktop\Projects\Youtube\Global Resources\Analog Video Package\Assets\Still Overlays\Scanlines.png',
    'jpg', False, False)
