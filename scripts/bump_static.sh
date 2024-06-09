#!/bin/bash

csshash=`sha1sum static/css/index.css | awk '{print substr($0,1,8)}'`
jshash=`sha1sum static/js/index.js | awk '{print substr($0,1,8)}'`

sed -i "s/csshash/$csshash/g" templates/patient-profile.html
sed -i "s/jshash/$jshash/g" templates/patient-profile.html
