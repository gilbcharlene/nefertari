import os
import ra
import webtest


appdir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..'))
ramlfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'api.raml'))
testapp = webtest.TestApp('config:local.ini', relative_to=appdir)

# ra entry point: instantiate the API test suite
api = ra.api(ramlfile, testapp)
api.autotest()
