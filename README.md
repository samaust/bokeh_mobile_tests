
# bokeh_mobile_tests
Basic Django website to test Bokeh plot rendering in a web browser

## How to use

### Compile bokeh
* cd to bokeh_mobile_tests
* Create a virtual environment (i.e., ```python -m venv env```)
* Activate the virtual environment (on ```Windows, env\Scripts\activate.bat```)
* Install node packages (see https://bokeh.pydata.org/en/latest/docs/dev_guide/setup.html#devguide-setup)
* Install Bokeh for development (i.e., ```python setup.py develop```)
* Install Django (i.e., ```python -m pip install Django```)

### Configure and start a web server
* Edit ```bokeh_mobile_tests\src\site1\settings.py``` and add your ip address to ALLOWED_HOSTS (i.e., ```ALLOWED_HOSTS = ['192.168.0.2']```).
* Copy ```bokeh\bokehjs\build\js\bokeh.js``` to ```bokeh_mobile_tests\static\bokeh_mobile_tests\js\bokeh\bokeh.js```
* Copy ```bokeh\bokehjs\build\css\bokeh.css``` to ```bokeh_mobile_tests\src\bokeh_mobile_tests\static\bokeh_mobile_tests\css\bokeh\bokeh.css```
* ```python manage.py runserver 192.168.0.2:8000```

### Test on mobile
* Open a web browser on a smartphone or tablet and enter the url ```http:\\192.168.0.2:8000```

