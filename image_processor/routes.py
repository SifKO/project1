"""
Routers for ouer Web A
"""
import os
from PIL import Image
from flask import render_template, flash, redirect, url_for, session, request
from image_processor import app, logger
from image_processor.image_processing import save_image, create_path, is_allowed_img, ImgSlices
from image_processor.forms import ImgProcessForm


NUM_OF_SLICE = 4


@app.context_processor
def utility_processor():
    """
    Enable zip in context app
    """
    return dict(zip=zip)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    """
    Main HTML page
    Download IMG, slice and plotting RGB graphs for sliced IMG,
    """
    form = ImgProcessForm()
    session_id = session.get('csrf_token')
    logger.info('Name of Session - %s', session_id)
    orig_pic = os.path.join(session_id, 'orig.png')
    x_orig, x_rgb = create_path(session_id, 'x', NUM_OF_SLICE)
    y_orig, y_rgb = create_path(session_id, 'y', NUM_OF_SLICE)
    pic = {
        'orig_pic': orig_pic,
        'x_orig': x_orig,
        'x_rgb': x_rgb,
        'y_orig': y_orig,
        'y_rgb': y_rgb
    }

    if request.method == 'POST':
        if form.validate_on_submit():
            if is_allowed_img(form.photo.data):
                name_of_img = 'orig.png'
                path = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
                save_image(path, name_of_img, form.photo.data)
                im = Image.open(os.path.join(path, name_of_img))
                ImgSlices(im, path, NUM_OF_SLICE)
                im.close()
                return redirect(url_for('index'))
            else:
                logger.error('Error - Type of file!!!')
                flash('Ошибка: Не корректный файл. разрешенные *.png *.jpg')
        else:
            # Сообщение об ошибке
            logger.error('Error - Upload File')
            flash('Ошибка: Пожалуйста, заполните все поля корректно.')

    return render_template('index.html', title='Upolad', form=form, pic=pic)
