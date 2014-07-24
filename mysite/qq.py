import urllib

class QQOperator:
    appid = '101045764'
    appkey = 'fa26651b39e397e5fa6a9bb3176afd1d'
    loginurl = 'https://graph.qq.com/oauth2.0/authorize'
    tokenurl = 'https://graph.qq.com/oauth2.0/token'
    openurl = 'https://graph.qq.com/oauth2.0/me'
    redirect = 'http://www.yczhou.com/qqauth/'

    def login_url(self):
        return '%s?%s' % (self.loginurl, urllib.urlencode({
               'response_type': 'code',
               'client_id': self.appid,
               'redirect_uri': self.redirect,
               'scope': 'get_user_info',
               'state': 'test',
            }))

    def token_url(self, code):
        return '%s?%s' % (self.tokenurl, urllib.urlencode({
               'grant_type': 'authorization_code',
               'client_id': self.appid,
               'client_secret': self.appkey,
               'code': code,
               'redirect_uri': self.redirect,
            }))

    def get_token(self, code):
        token = urllib.urlopen(self.token_url(code)).read()
        sp = token.split('&')
        return sp[0].split('=')[1]

    def openid_url(self, token):
        return '%s?%s' % (self.openurl, urllib.urlencode({
               'access_token': token,
               }))

    def get_openid(self, token):
        content = urllib.urlopen(self.openid_url(token)).read()
        content = content[content.find('(')+1:content.rfind(')')]
        data = eval(content)
        return data.get('openid')
    
    getuserinfourl = 'https://graph.qq.com/user/get_user_info'
    def get_user_info_url(self, token, openid):
        return '%s?%s' % (self.getuserinfourl, urllib.urlencode({
               'access_token': token,
               'oauth_consumer_key': self.appid,
               'openid': openid,
               }))

    def get_user_info(self, token, openid):
        '''
        return a dict
        keys: 
        ret, msg, is_lost, nickname, gender, figureurl,
        figureurl_1, figureurl_2, figureurl_qq_1, figureurl_qq_2,
        is_yellow_vip, vip, yellow_vip_level, level, is_yellow_year_vip
        '''
        url = self.get_user_info_url(token, openid)
        content = urllib.urlopen(url).read()
        return eval(content)
