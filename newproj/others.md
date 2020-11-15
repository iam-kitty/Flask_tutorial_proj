#database commands

from app import db 
( warnings.warn(FSADeprecationWarning)-->ignore warning

>>> db.create_all()
>>> from app import BlogPost
>>> BlogPost.query.all()
[Blog Post1, Blog Post2]
>>> BlogPost.query.all()[0]
Blog Post1
>>> BlogPost.query.all()[0].content
'lalalallala'
>>> BlogPost.query.filter_by(title='My first BlogPost').all()
[Blog Post1]
>>> BlogPost.query.get(1) **using ID**
Blog Post1
>>> BlogPost.query.filter_by(author='kitty').all()
[Blog Post1, Blog Post3]
>>> BlogPost.query.filter_by(author='kitty')[1]
Blog Post3
