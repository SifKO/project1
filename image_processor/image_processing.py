"""
Этот модуль содержит функции для работы с данными пользователей.
Здесь определены функции для их добавления, удаления и редактирования.
"""
# import logging
import os
import magic
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
from image_processor import logger, app


class ImgSlices:
    """
    Accept IMGE
    :param image: Input image used library (PIL Image).
    :param path: Your path to save sliced IMG.
    :param pieces: The number of parts to split the image along the axes.
    """
    def __init__(self, image, path, pieces):
        """
        Initializing the ImgSlices class.
        """
        self.input_img = image
        self.path = path

        # Getting img parameters
        self.x, self.y = image.size
        step_x = self.x // pieces
        step_y = self.y // pieces
        self.split_x(pieces, self.y, step_x)
        self.split_y(pieces, self.x, step_y)

    def split_x(self, pieces, y, step_x):
        """
        Cuts along the x axis for pieces
        Save Pics as x<i>.png
        Call function plot_graph and save RGB graphs as x<i>rgb.png
        """
        prefix = 'x'
        for i in range(pieces):
            box = (step_x * i, 0, step_x * (i + 1), y)
            image = self.input_img.crop(box)
            local_p = os.path.join(self.path, f'{prefix}{i}.png')
            image.save(local_p)
            self.plot_graph(image, str(i), prefix)

    def split_y(self, pieces, x, step_y):
        """
        Cuts along the y axis for pieces
        Save Pics as y<i>.png
        Call function plot_graph and save RGB graphs as y<i>rgb.png
        """
        prefix = 'y'
        for i in range(pieces):
            box = (0, step_y * i, x, step_y * (i + 1))
            image = self.input_img.crop(box)
            local_p = os.path.join(self.path, f'{prefix}{i}.png')
            image.save(local_p)
            self.plot_graph(image, str(i), prefix)

    def plot_graph(self, img, i, prefix):
        """
        Plotting histogram for R, G, B channels
        Save RGB graphs as <prefix><i>rgb.png (x1rgb.png)
        """
        try:
            pixels = list(img.getdata())
            r = [p[0] for p in pixels]
            g = [p[1] for p in pixels]
            b = [p[2] for p in pixels]

            plt.figure(figsize=(10, 6))
            plt.hist(r, bins=256, color='red', alpha=0.5, label='Red Channel')
            plt.hist(g, bins=256, color='green', alpha=0.5,
                     label='Green Channel')
            plt.hist(b, bins=256, color='blue', alpha=0.5,
                     label='Blue Channel')
            plt.title('Color Histogram')
            plt.xlabel('Pixel Value')
            plt.ylabel('Frequency')
            plt.legend()
            local_p = os.path.join(self.path, f'{prefix}{i}rgb.png')
            plt.savefig(local_p)
            logger.info('Создн файл %s', local_p)
            plt.close()
        except Exception as e:
            logger.error('Error while plotting graph for %s %s: %s',
                         prefix, i, e)
        finally:
            plt.close()


def create_path(session_id, prefix, peaces):
    """
    Create path for images in session and generat links for flask
    :param session_id: Session ID in Flask needs to create individual floder
    :param prefix: Use to define slices x or y
    :param peaces: Count of slices
    """
    orig = []
    slices = []
    for i in range(peaces):
        orig.append(os.path.join(session_id, prefix + str(i) + '.png'))
        slices.append(os.path.join(session_id, prefix + str(i) + 'rgb.png'))
    return orig, slices


def save_image(path, name_of_img, img):
    """
    Save IMG in your path and cuusen name
    path, name_of_img, img
    :param path: Your chosen folder to save IMG
    :param name_of_img: Your define name
    :param img: Object of IMG
    """
    try:
        os.makedirs(path)
        # Создает папку, включая промежуточные директории
        logger.info('Папка %s успешно создана.', path)
    except FileExistsError:
        logger.info('Папка %s уже существует.', path)
    except Exception as e:
        logger.error('Ошибка при создании папки: %s', e)
    f = img
    filepic = secure_filename(f.filename)
    f.save(os.path.join(path, name_of_img))
    logger.info('All is OK!')


def is_allowed_img(img):
    """
    Cheсked allowed files and return true/false
    :param img: Object of IMG for checking
    """
    # Определяем MIME-тип файла
    mime = magic.Magic(mime=True)
    # Read firs 2024 for def
    file_type = mime.from_buffer(img.read(2024)) 
    img.seek(0)
    # Сбросим курсор обратно
    allowed_file = app.config['ALLOWED_EXTENSIONS']
    logger.info('Allowed: %s', allowed_file)
    if file_type in ['image/jpeg', 'image/png']:
        # Check type
        return True
    return False

# # Пример использования
# uploaded_file = request.files['photo']  # Получаем файл из запроса
# if is_valid_file(uploaded_file):
#     # Обрабатываем файл
# else:
#     # Обрабатываем ошибку
