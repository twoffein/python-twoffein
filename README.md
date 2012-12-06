Python-twoffein README
======================

This is python-twoffein, a python module that allows you
accessing the Twoffein.com API using Python classes instead
of manual HTTP requests.

Installation instructions
-------------------------

Since python-twoffein uses setuptools, you just need to
run

 python2 setup.py install

to install it.

Using
-----

After importing the twoffein module, you need to create an
instance of the Twoffein class, passing the user name and
API key to it's constructor:

```
>>> import twoffein
>>> api = twoffein.Twoffein( ("the_user", "the-api-key") )
```

Now, there are the following method available:

```
>>> api.get_drinks()
[{u'brand': u'0', u'drink': u'Kaffee', u'key': u'kaffee'}, […], {u'brand': u'2', u'drink': u'Limettenlimonade', u'key': u'limettenlimonade'}]
```

returns a list of all available drinks.

```
>>> api.get_profile("user")
{u'drunken': u'456', u'first_login': u'1342804622', u'profile_image_https': u'https://si0.twimg.com/profile_images/2766884822/d3dc48aea258f3a26ad1e1a703542595_normal.png', u'screen_name': u'user', u'bluttwoffeinkonzentration': u'1%', u'drink': u'Schwarztee', u'profile_image': u'http://a0.twimg.com/profile_images/2766884822/d3dc48aea258f3a26ad1e1a703542595_normal.png', u'rank': 4, u'quest': u'Liebesbotschaft', u'rank_title': u'Kaffekännchen'}
```

returns the profile of "user". If the parameter is omitted,
the profile of the user used to authenticate against the API
is returned.

```
>>> api.give_cookie("target_user")
{u'info': u'Thanks for the cookie, nomnomnom!', u'code': u'celestia'}
```

gives a cookie to "target_user".

```
>>> api.drink( twoffein.Drink("drink_id"), "target_user")
{u'info': u'Youre Tweet has been tweeted. Thanks.', u'tweets': 1, u'code': u'luna'}
```

For the return codes, please refer to the [official API documentation](http://twoffein.com/api-faq/).

