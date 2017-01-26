Ratio Calculator
================

A simple <abbr title="JavaScript Database">JSDB</abbr> script to calculate the ratio of two numbers. Such as the dimensions of an image or screen.


Usage
-----

```bash
$ ratio 1280 720
Caclulating ratio of 1280x720
Ratio: 16:9 (80) or 1.777~
```


Installation
------------

This installation example assumes you have a directory off of your home directory named `repos`, a local `bin` directory that already exists in your `PATH` and you have already installed [JSDB][]. Adjust appropriately if you have a different location for your cloned repositories or intend to link the script to another executable path.


### Linux, macOS/Darwin, UNIX, etc.

```bash
$ cd ~/repos
$ git clone git@github.com:runeimp/ratio.git
$ cd ~/bin
$ ln -s ../repos/ratio/ratio.js ratio
```


### Windows

```dos
> CD \REPOS
> git clone git@github.com:runeimp/ratio.git
> CD \BIN
> mklink /D \BIN\ratio \REPOS\ratio\ratio.js
```

Installing in this fashion will allow for easy updating of the repo while maintaining an extensionless executable reference.


[JSDB]: http://www.jsdb.org/

