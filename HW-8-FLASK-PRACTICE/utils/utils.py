import psutil as ps


def get_docstring(func):
   docstring = getattr(ps, func).__doc__.replace('\n', '<br>') 
   return docstring

def to_bool(**kwargs):
    for k, v in kwargs.items():
        if v in ('True', 'False'):
            kwargs[k] = bool(v)
    return kwargs


