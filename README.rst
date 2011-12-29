INTRODUCTION
============

This script parse a sitemap and visit all url listed.

HOW TO INSTALL
==============

you must have git, python with setuptools, firefox and java.

execute this command:

::

    git clone git://github.com/toutpt/gaselenium.git
    cd gaselenium
    python bootstrap.py
    bin/buildout
    bin/python gaselenium.py http://monsite.com/sitemap.xml

Google test
===========

    bin/python googletest.py http://www.inextcom.fr /home/toutpt/tmp/keywords.txt
