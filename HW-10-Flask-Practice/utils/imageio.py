import base64
import io
import PIL.Image

# This function calls init on each registered PIL plugin,
# thus returning a dict of {'.ext': 'FORMAT_NAME'}
EXTENSIONS = PIL.Image.registered_extensions()
# Build the inverse for lookups, containing {FORMAT: EXT}
FORMATS = {v: k for k, v in EXTENSIONS.items()}

# max num of pixels allowed
MAX_PIXELS = 3_500_000

# max size allowed
MAX_SIZE = 10 * 1024 * 1024  # 10 MB

class ImageIOError(Exception):
    pass


class ImageIO(io.BytesIO):
    # class-level default to ensure attr is always present
    ext = None

    def __init__(self, *args, ext=None, **kwargs):
        # if image object passed as first argument
        # consume it creating buffer from image
        try:
            first, *etc = args
            if isinstance(first, PIL.Image.Image):
                super().__init__(*etc, **kwargs)
                self.save_image(img=first, ext=ext)
                return
        except ValueError:
            pass

        # assuming no image object passed
        # -> act as standard BytesIO
        super().__init__(*args, **kwargs)
    

    def save_image(self, img, ext=None):
        assert self.tell() == 0, 'Buffer not empty before save'

        try:
            ext = FORMATS[img.format] if ext is None else ext
            ext = ext.lower()
            format = EXTENSIONS[ext]
        except KeyError:
            err = ImageIOError(f'Unsupported image extension "{ext}"')
            raise err from None

        # check file extension
        if not ext in ['.jpg', '.jpeg', '.jfif', '.png']:
            err = ImageIOError(f'Unsupported image extension "{ext}"')
            raise err from None

        # check file size
        if self.getbuffer().nbytes > MAX_SIZE:
            err = ImageIOError(f'File size exceeds maximum allowed ({MAX_SIZE} bytes)')
            raise err from None

        # check image dimensions
        img_size = img.size[0] * img.size[1]
        
        if img_size > MAX_PIXELS:
            print(f'{img_size} > {MAX_PIXELS}')
            err = ImageIOError(f'Image size exceeds maximum allowed ({MAX_PIXELS} pixels)')
            raise err from None

        img.save(self, format=format)

        self.truncate() # remove extra data if there were any
        self.seek(0)    # rewind so it gets read from the beginning
        self.ext = ext
        return self.getbuffer().nbytes
    
    def as_base64(self, altchars=None):
        data = self.getvalue()
        enc = base64.b64encode(data, altchars=altchars)
        return enc.decode('ascii')


