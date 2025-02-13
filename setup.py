
import re
import sys

from setuptools import setup, find_packages

version = None
for line in open("./fudge/__init__.py"):
    m = re.search("__version__\s*=\s*(.*)", line)
    if m:
        version = m.group(1).strip()[1:-1] # quotes
        break
assert version

setup(
    name='fudge',
    version=version,
    description="Replace real objects with fakes (mocks, stubs, etc) while testing.",
    long_description="""
Complete documentation is available at https://fudge.readthedocs.org/en/latest/

Fudge is a Python module for using fake objects (mocks and stubs) to test real ones.

In readable Python code, you declare what methods are available on your fake and
how they should be called. Then you inject that into your application and start
testing. This declarative approach means you don't have to record and playback
actions and you don't have to inspect your fakes after running code. If the fake
object was used incorrectly then you'll see an informative exception message
with a traceback that points to the culprit.

Here is a quick preview of how you can test code that sends
email without actually sending email::

    @fudge.patch('smtplib.SMTP')
    def test_mailer(FakeSMTP):
        # Declare how the SMTP class should be used:
        (FakeSMTP.expects_call()
                 .expects('connect')
                 .expects('sendmail').with_arg_count(3))
        # Run production code:
        send_mail()
        # ...expectations are verified automatically at the end of the test

""",
    author='Kumar McMillan',
    author_email='kumar.mcmillan@gmail.com',
    license="The MIT License",
    packages=find_packages(exclude=['ez_setup']),
    install_requires=[],
    url='https://github.com/fudge-py/fudge',
    include_package_data=True,
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
        ],
    )
