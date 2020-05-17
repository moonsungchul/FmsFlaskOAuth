
import schedule
import time
from flask import Flask
from flask_restful import Resource, Api
#from flask_oauthlib.provider import OAuth2Provider
from oauth2client.contrib.flask_util import UserOAuth2


app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'mmm'
app.config['GOOGLE_OAUTH2_CLIENT_SECRETS_FILE'] = 'client_secrets.json'

@app.route('/version')
def version():
    return {'versin':'OAuth test version 1'}


@app.route('/')
def root():
    return {'versin':'OAuth test version home 1'}



oauth2 = UserOAuth2(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5600, debug=True)

