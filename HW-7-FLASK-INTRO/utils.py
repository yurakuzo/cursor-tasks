from flask import abort

def validate_timezone(time_zone):
   if abs(time_zone) > 12:
        abort(406, "Timezone not found")

def get_docstring(func):
   docstring = func.__doc__.replace('\n', '<br>') 
   return docstring