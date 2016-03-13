from distutils.core import setup
setup(
    name="autobot",
    packages=["autobot"],
    version="1.0.0",
    description="Context Manager for ease of creating IRC bots",
    author="Wayne Simmerson",
    author_email="wsimmerson@gmail.com",
    url="https://github.com/wsimmerson/autobot",
    download_url="https://github.com/wsimmerson/autobot/tarball/1.0.0",
    keywords=["irc", "bot"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPL"
    ],
    long_description="""
        Autobot
        -------

        Context Manger for ease of creating IRC Bots
    """
)
