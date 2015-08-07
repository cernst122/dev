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
import os
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
my_dictionary={"Of Monsters and Men": "Crystals", "Mumford and Sons": "Lover of the Light", "Imagine Dragons": "Bet My Life", "Of Monsters and Men": "Mountain Sound", "Breaking Benjamin": "Diary of Jane", "Journey": "Don't Stop Believin'"}

class MainHandler(webapp2.RequestHandler):

    def get(self):

        for artist in my_dictionary:
            self.response.out.write (my_dictionary[artist] + "<br>" )

        first_template = jinja_environment.get_template('templates/index.html')
        self.response.write(first_template.render(my_dictionary))

    def post(self):


        songName = self.request.get("songName")
        newArtist = self.request.get("artist") #gets these variables from the html form
        newMusic={}
        # Add a new item.
        newMusic[newArtist] = songName
        my_dictionary.update(newMusic)


# You may also use different types other than strings for key/value pairs.
# Assigns an integer value to the 'key2' key.


        results_template = jinja_environment.get_template('templates/index.html')
        


app = webapp2.WSGIApplication([
    ('/', MainHandler)

], debug=True)
