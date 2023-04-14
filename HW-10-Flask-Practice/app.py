import os
from imagedir import catday, uploaded
from utils.textcut import cutter
import utils

from flask import Flask, Response, abort, send_file
from flask import render_template, request, redirect

import PIL.Image
import logging

from time import perf_counter

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',
                            title='Hello World!', 
                          )

# Note:
#   If a rule ends with a slash and is requested without a slash by the user,
#   the user is automatically redirected to the same page with a trailing 
#   slash attached.
#   If a rule does not end with a trailing slash and the user requests
#   the page with a trailing slash, a 404 not found is raised.
# So we try to always define rules with trailing slashes '/'

@app.route('/cats/')
def list_cats():
    msg = 'There are {num} cats in our collection'
    return msg.format(num=len(catday.IMAGES))


def get_cat(numext, try_random=False):
    try:
        ret = catday.find_img_file(numext=numext,
                                         try_random=try_random)
    except ValueError:      # integer unconvertable or wrong range
        abort(404, 'Wrong image number')
    else:
        app.logger.debug('Retrieve image "%s" for '
                        'base %s with ext "%s"',
                        *ret)
        return ret


@app.route('/cats/cat<int:num>.<string:ext>')
def cat_original(num, ext):
    t_start = perf_counter()    # measure request time

    file, base, ext = get_cat(f'{num}.{ext}', try_random=False)

    name = f'cat{base}{ext}'   # the filename passed to browser
    
    app.logger.debug('Original extension is %s', file.suffix)
    
    # if the extension is different, perform conversion with PIL
    if ext.lower() != file.suffix.lower():
        
        try:
            img = PIL.Image.open(file)
            # Save to buffer in memory and serve with Flask
            buf = utils.ImageIO(img, ext=ext)
        except utils.ImageIOError as err:
            abort(400, str(err))
        else:
            # now our file gets mocked by conversion result
            file = buf
    
    # if the file has the same extension,
    # don't convert at all and return directly

    took = perf_counter() - t_start

    if app.logger.isEnabledFor(logging.DEBUG):
        msg = f'Request took {took * 1000:.2f} ms'
        app.logger.debug(msg)

    return send_file(file, as_attachment=False, download_name=name)


@app.route('/cats/catoftheday<name>')
def cat_modified(name, text=''):
    file, base, ext = get_cat(name, try_random=True)

    date = utils.DateTriple()       # try UADateTriple() here
    date_suffix = date.tostr(fmt='{day}_{month:.3}').lower()

    text = text if text else date.tostr(fmt='{weekday:.3},\n{day}\n{month:.3}')

    try:
        img = PIL.Image.open(file)
        bgcolor = (255, 255, 255, int(255 * 0.4))
        cut = cutter.text_cutout(img, text, bgcolor=bgcolor)
        if ext in ['.jpg', '.jpeg', '.jfif']:
            # eliminate alpha-channel as JPEG has no alpha
            cut = cut.convert('RGB')
        file = utils.ImageIO(cut, ext=ext)
    except utils.ImageIOError as err:
        abort(400, str(err))

    # passed to browser
    name = f'catoftheday{base}-{date_suffix}{ext}'
    return send_file(file, as_attachment=False, download_name=name)



@app.route('/cats/custom', methods=['GET', 'POST'])
def custom():
    if request.method == 'GET':
        return render_template('custom_cat.html',
                            title='Custom Image'
                            )
    if request.method == 'POST':
        file = request.files.get('image')
        filename, ext = file.filename.split('.')
        ext = f'.{ext}'

        text = request.form.get('text')

        try:
            img = PIL.Image.open(file)
            bgcolor = (255, 255, 255, int(255 * 0.4))
            cut = cutter.text_cutout(img, text, bgcolor=bgcolor)
            if ext in ['.jpg', '.jpeg', '.jfif']:
                # eliminate alpha-channel as JPEG has no alpha
                cut = cut.convert('RGB')
            file = utils.ImageIO(cut, ext=ext)
        except utils.ImageIOError as err:
            abort(400, str(err))

        # passed to browser
        name = f'custom_cat_{filename}-{text}{ext}'
        return send_file(file, as_attachment=False, download_name=name)

@app.route('/cats/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html',
                                title='Upload own picture'
                              )
    if request.method == 'POST':
        file = request.files.get('image')
        filename, ext = file.filename.split('.')
        ext = f'.{ext}'
        print(f"file: {file}\nfilename: {filename}\next: {ext}\n")
        
        if ext in ('.jpg', '.jpeg', '.jfif', '.png'):
            filename = utils.hash.get_hash(file) + ext
            if not uploaded.image_exists(filename):
                path_file = os.path.join(uploaded.DIR_PATH, filename)
                file.save(path_file)
                uploaded.update_IMAGES()
                return Response('Your image has been successfully uploaded', 200)
            else:
                return Response('Your image has been already uploaded before', 409)
        else:
            return Response('Invalid file format', 422)


if __name__ == '__main__':
    import logging
    app.logger.setLevel(logging.DEBUG)
    app.run(host='127.0.0.1', port=5000, debug=True)