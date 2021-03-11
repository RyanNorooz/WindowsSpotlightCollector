import os
from platform import system
from traceback import print_exc

from PIL import Image
from win10toast import ToastNotifier


def main():
    global saved_counter

    imgs_dir = os.path.join(os.environ['USERPROFILE'],
                            'AppData\\Local\\Packages',
                            'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')
    # destination = os.path.join(os.environ['USERPROFILE'], 'Desktop\\Windows SpotLight Images')
    destination = 'Windows SpotLight Images'
    file_list = os.listdir(imgs_dir)
    if not os.path.exists(destination):
        # os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop'))
        os.mkdir('Windows SpotLight Images')

    for file in file_list:
        with Image.open(os.path.join(imgs_dir, file)) as img:
            if img.size == (1920, 1080):
                img.save(os.path.join(destination, f'{file}.jpg'))
                saved_counter += 1


if __name__ == '__main__' and system() == 'Windows':
    try:
        saved_counter = 0
        main()
        ToastNotifier().show_toast(f"{saved_counter} images saved…!", "Windows Spotlight Images")
    except Exception as e:
        print(e)
        print_exc()
        input('\nPress enter to exit.')
