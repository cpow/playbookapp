#!/usr/bin/env python2.5
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import datetime
import logging
import os

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from django.utils import simplejson as json

def get_image_list():
    return ["testImg",
            "testImg2"]

class Design(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    greetings = "Welcome to the Football Playbook Creater!"
    if not user:
      login_url = users.create_login_url(self.request.uri)
      login_text = 'Login'
    else:
      login_url = users.create_logout_url(self.request.uri)
      login_text = 'Logout'

    #play_img_list=dirList=os.listdir(play_images_dir)
    play_img_list=get_image_list()

    template_values = {}
    template_values = {
        'greetings': greetings,
        'login_url': login_url,
        'login_text': login_text,
        'play_img_list': play_img_list
    }
    #path = os.path.join(os.path.dirname(__file__), 'templates/design2.html')
    path = os.path.join(os.path.dirname(__file__), 'templates/design.html')
    self.response.out.write(template.render(path, template_values))


class SubmitPlay(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    greetings = "Welcome to the Football Playbook Creater!"
    if not user:
        login_url = users.create_login_url(self.request.uri)
        login_text = 'Login'
        action="Add Play"
        template_values = {}
        template_values = {
          'action': action,
          'login_url': login_url,
          'login_text': login_text,
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/accessdenied.html')
        self.response.out.write(template.render(path, template_values))

    else:
      login_url = users.create_logout_url(self.request.uri)
      login_text = 'Logout'
  def post(self):
    self.response.out.write('<html><body>You wrote:<pre>')
    self.response.out.write(cgi.escape(self.request.get('playname')))
    self.response.out.write('<BR>You wrote:')
    self.response.out.write(cgi.escape(self.request.get('positions')))
    self.response.out.write('</pre></body></html>')


class MainHandler(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      template_values = {}
      path = os.path.join(os.path.dirname(__file__), 'templates/design.html')
      self.response.out.write(template.render(path, template_values))
    else:
      self.redirect(users.create_login_url(self.request.uri)) 

def main():
  application = webapp.WSGIApplication([('/', MainHandler),
                                        ('/design', Design),
                                        ('/submitplay', SubmitPlay)],
                                         debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
