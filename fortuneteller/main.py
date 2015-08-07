#!/usr/bin/env python
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
import webapp2

import jinja2
import os

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write("Test")
        eightball_template = jinja_environment.get_template('templates/eightball.html')
        self.response.out.write(eightball_template.render())

class BallHandler(webapp2.RequestHandler):
    def get(self):
        userQuestion="Will I have a good day? "
        answers= ["Yes", "Absolutely", "Uncertain", "Ask again later", "Without a doubt", "Definitely not", "No way", "Perhaps", "Only if you believe", "The answer is foggy"]
        from random import randint
        randomNum=randint(0,9)
        self.response.write(userQuestion)
        self.response.write(answers[randomNum])
        self.response.write("<img src= 'http://www.mannythemovieguy.com/images/magic_8_ball_the_movie.jpg'></img")





class WhirlyBird(webapp2.RequestHandler):
    def get(self):
        self.response.write("Pick a color: ")
        userColor="blue"
        userNumber=self.request.get('num')


app = webapp2.WSGIApplication([
   ('/', MainHandler),
   ("/8ball", BallHandler),
   ("/whirlybird", WhirlyBird)



], debug=True)
