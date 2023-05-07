import logging
from os import listdir
# Setup logging ASAP, as we want all
# messages to appear in log when this file is
# used as the project root (i.e. without Flask)

from utils import DateTriple, cutter
import pathlib as pth
import random

# Directory containing images,
# relative to project directory
class ImagesDir:
    def __init__(self, DIR='./cats'):
        self.DIR = DIR
        self._PROJDIR = pth.Path(__file__).parent
        self.DIR_PATH = self._PROJDIR.joinpath(DIR[2:])

     # collect all images under supplied directory
        self.IMAGES = self._get_imgs(self.DIR)
        
        # The logger we use
        log = logging.getLogger(__name__)
        log.debug('Project directory is "%s"', self._PROJDIR.resolve())
        
        # Put some info into log
        log.info('Images directory set to: %s', self.DIR)
        if log.isEnabledFor(logging.INFO):
            log.info('Collected %s images:\n\t%s',
                    len(IMAGES), '\n\t'.join(IMAGES))   

    def _get_imgs(self, dir=None):
            dir = dir or self.DIR
            # Ensure all directories reside under project directory
            # and are resolved relative to it
            dir = self._PROJDIR.joinpath(pth.Path(dir))
            assert dir.is_relative_to(self._PROJDIR)
            imgs = tuple(dir.iterdir())
            return imgs
    
    
    def find_img_file(self, numext, try_random=False):
        p = pth.Path(numext)
        base, ext = (p.stem, p.suffix) if p.suffix else ('', numext)

        # num specifies the image to use
        # if num is omitted, and try_random is True, random image should appear
        if try_random is True and not base:
            num = random.randint(0, len(self.IMAGES) - 1)
        else:
            num = int(base)      # try integer conversion
        
        if num < 0 or num > len(self.IMAGES) - 1:
            raise ValueError
        
        return self.IMAGES[num], base, ext

    def image_exists(self, name):
        return name in listdir(self.DIR_PATH)

    def update_IMAGES(self):
        global IMAGES
        IMAGES = self._get_imgs(self.DIR)
        
class UploadedDir(ImagesDir):
    def __init__(self, DIR='./uploaded', *args, **kwargs):
        super().__init__(DIR=DIR, *args, **kwargs)

        
catday = ImagesDir()
uploaded = UploadedDir()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
