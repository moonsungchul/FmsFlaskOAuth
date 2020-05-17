
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

oauth2 = UserOAuth2(app)

@app.route('/version')
def version():
    return {'versin':'OAuth test version 1'}


@app.route('/')
def root():
    return {'versin':'OAuth test version home 1'}


@app.route('/info')
@oauth2.required
def info():
    return "Hello, {}{}".format(oauth2.email, oauth2.user_id)


@app.route('/islogin')
def islogin():
    if oauth2.has_credentials():
        return "로그인"
    else:
        return "로그인 하세요"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5600, debug=True)

