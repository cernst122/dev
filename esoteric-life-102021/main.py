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

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
      main_template = jinja_environment.get_template('templates/index.html')
      self.response.out.write(main_template.render())
    def post(self):
      myName = self.request.get("name")
      question = self.request.get("question") #gets these variables from the html form
      userAnswers = {"name": myName, "question": question } #use these green keys in html between mustaches
      results_template = jinja_environment.get_template('templates/results.html')



      ballAnswers= ["Yes", "Absolutely", "Uncertain", "Ask again later", "Without a doubt", "Definitely not", "No way", "Perhaps", "Only if you believe", "The answer is foggy"]
      answers = {"answers" : ballAnswers}
      self.response.out.write(results_template.render(answers))
    # #   from random import randint
    # #   randomNum=randint(0,2)
    #   self.response.out.write(results_template.render(ballAnswers[randomNum]))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)