import logging
from os import listdir
# Setup logging ASAP, as we want all
# messages to appear in log when this file is
# used as the project root (i.e. without Flask)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)


from utils import DateTriple, cutter
import pathlib as pth
import random

# Directory containing uploaded images,
# relative to project directory
UPLOADDIR = './uploaded'
_PROJDIR = pth.Path(__file__).parent

UPLOADDIR_PATH = _PROJDIR.joinpath('uploaded')

# The logger we use
log = logging.getLogger(__name__)
log.debug('Project directory is "%s"', _PROJDIR.resolve())

def _get_uploaded_images(uploaddir=UPLOADDIR):
    # Ensure all directories reside under project directory
    # and are resolved relative to it

    uploaddir = _PROJDIR.joinpath(pth.Path(uploaddir))
    assert uploaddir.is_relative_to(_PROJDIR)
    images = tuple(uploaddir.iterdir())
    return images

# collect all uploaded images under supplied directory
UPLOADED_IMAGES = _get_uploaded_images(UPLOADDIR)

# Put some info into log
log.info('Uploaded directory set to: %s', UPLOADDIR)
if log.isEnabledFor(logging.INFO):
    log.info('Collected %s uploaded images:\n\t%s',
              len(UPLOADED_IMAGES), '\n\t'.join(str(img) for img in UPLOADED_IMAGES))


def find_cat_file(numext, try_random=False):
    p = pth.Path(numext)
    base, ext = (p.stem, p.suffix) if p.suffix else ('', numext)

    # num specifies the cat image to use
    # if num is omitted, and try_random is True, random cat should appear
    if try_random is True and not base:
        num = random.randint(0, len(UPLOADED_IMAGES) - 1)
    else:
        num = int(base)      # try integer conversion
    
    if num < 0 or num > len(UPLOADED_IMAGES) - 1:
        raise ValueError
    
    return UPLOADED_IMAGES[num], base, ext

def image_exists(name):
    return name in listdir(UPLOADDIR_PATH)

def update_UPLOADED():
    global UPLOADED_IMAGES
    CATS = _get_uploaded_images(UPLOADDIR)
