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

da_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # create the dictionary of variables you'll use in render
        #the values can be any data type; use what you want to use in html.
        user_cat_type = self.request.get("cat")
        number_of_cats = self.request.get("number")
        my_template_dictionary = {"cat_type": user_cat_type, "cat_number": number_of_cats}
        # self.response.write('Hello world!') We want it to write one of our templates, not hello world
        #so load the first template you want to See
        first_template = da_jinja_environment.get_template('templates/landing.html') #in this environment, go get the template, here's its name
        #we have the template, now write it
        self.response.out.write(first_template.render(my_template_dictionary)) #here's my html file, now turn it into a string to write with render method
        #the variables you want to go inside render need to go into a dictionary.



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
