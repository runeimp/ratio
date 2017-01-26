Ratio Calculator
================

A simple <abbr title="JavaScript Database">JSDB</abbr> script to calculate the ratio of two numbers. Such as the dimensions of an image or screen.


Usage
-----

```bash
$ ratio 1280 720

    Caclulating ratio of 1280×720
    Ratio: 16:9 (80) or 1.777~
    Points: 921600

```


Installation
------------

This installation example assumes you have a directory off of your home directory named `repos`, a local `bin` directory that already exists in your `PATH` and you have already installed [Node.js][]. Adjust appropriately if you have a different location for your cloned repositories or intend to link the script to another executable path.


### Linux, macOS/Darwin, UNIX, etc.

```bash
$ cd ~/repos
$ git clone git@github.com:runeimp/ratio.git
$ cd ~/bin
$ ln -s ../repos/ratio/ratio.js ratio
```


### Windows

Please note that this install method for Windows has NOT been tested in any way. I'm just riffing off the top of my head as a former Windows guy who still uses it for gaming and minor Windows specific projects. O:-)

To be honest I should probably have done this initially with [Microsoft - Windows Script Host][] instead of [JSDB][] back in the day for Windows machines. But I'd already switched to Mac by then and love cross-platform over system specific whenever possible. Plus we're way beyond that at this point!  :-)

```dos
> CD \REPOS
> git clone git@github.com:runeimp/ratio.git
> CD \BIN
> mklink /D \BIN\ratio \REPOS\ratio\ratio.bat
```

Installing in this fashion will allow for easy updating of the repo while maintaining an extensionless executable reference.


[Node.js]: https://nodejs.org/en/
[Microsoft - Windows Script Host]: https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/wsh_overview.mspx?mfr=true
[JSDB]: http://www.jsdb.org/

