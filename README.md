#How to use

###installation (on ubuntu 18.04)

#####ElasticSearch Install

install Java
$ sudo apt install openjdk-11-jdk

install Elasticsearch
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt update
$ sudo apt install elasticsearch

$ sudo systemctl start elasticsearch
$ sudo systemctl status elasticsearch

Confirm
$ curl http://127.0.0.1:9200

#####Kibana Install
$ apt update
$ apt install kibana

$ systemctl start kibana

Confirm
$ access http://localhost:5601

#####kuromoji Install
$ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-kuromoji

#####Python and Pip install
$ sudo apt update
$ sudo apt install python3.7
$ vim ~/.bashrc
add `alias python3='/usr/bin/python3.7’`
$ reboot

$ sudo apt install python3-pip
$ pip3 --version
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)

$ sudo pip3 install pipenv
pipenv, version 2018.11.26

###get Rakuten API ID
https://webservice.rakuten.co.jp/
Click "New App"

###Build Application environment
#####make app root
$ mkdir Elastic_app (any name you want)

#####make pipenv virtual platform
$ cd Elastic_app
$ pipenv --three

#####install python library requests
$ pipenv install requests
will make Pipfile and Pipfile.lock

#####get_books_from_rakuten.py
This file fetch book data with 'keyword':'Python' and json.dump to the file rakuten_books.json.

$ pipenv run get_books_from_rakuten.py

#####install python library elasticsearch
$ pipenv install elasticsearch

#####import_data_to_es.py
This file bulk import json data to elasticsearch.

$ pipenv run python import_data_to_es.py


###search application completion

#####structur
locate files from github like the following under app root directory.

application/
    |- __init__py
    |- iews.py
    |- static
        |- style.css
    |- templates
        |- index.html
get_books_from_rakuten.py
import_data\to_es.py
Pipfile
Pipfile.lock
rakuten_books.json
server.py




###How to boot application
$ pipenv run python server.py
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 159-754-361


