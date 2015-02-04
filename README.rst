================
django-mail-tester
================
A simple sendmail management command to send email using your django project.

NOTE This tool was created for mail testing purpose, not for any kind of production mailing tasks.
But if you find it useful for any other tasks, gratz! Tell us about your experience.

Installation
============

::

$ pip install django-mail-tester

Configure installed apps in your ``settings.py`` ::

  INSTALLED_APPS = [
      # ... your app list
      'django_mail_tester',
  ]

Usage
=====

Send email to your address

::

$ ./manage.py sendmail -e test@example.com This is a test message

If you need a cheap, simple and efficient way to quickly test the quality of your own newsletters, try `Mail Tester <http://www.mail-tester.com>`_.

Changelog
=========
The changelog can be found at `repo's release notes <https://github.com/satyrius/django-mail-tester/releases>`_

Contributing
============
Fork the repo, create a feature branch then send me pull request. Feel free to create new issues or contact me via email.
