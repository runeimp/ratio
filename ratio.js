#!/usr/bin/env jsdb
/*
Ratio Calculator

@author RuneImp <runeimp@gmail.com>

ChangeLog
---------
2010-12-12  1.0.0      Initial script creation using JSDB
*/
var args = jsArguments;
if(args.length < 2)
{
	writeln();
	writeln('Must supply two numbers to devine the ratio.');
	writeln();
	writeln('Output Example:');
	writeln('    Ratio: 16:9 (divisor) or 1.777~');
	writeln();
	writeln('The last number is the larger argument divided by the smaller argument.');
	writeln();
	system.gc();
	system.exit(1);
}
else
{
	writeln('Caclulating ratio of '+args[0]+'x'+args[1]);
}

var max = Math.max(args[0], args[1]);
var min = Math.min(args[0], args[1]);
var mod = min;

while(mod > 0)
{
	if(max % mod == 0 && min % mod == 0)
	{
		var rMax = max / mod;
		var rMin = min / mod;
		var ratio = (max / min);
		var ratioRounded = Math.round(ratio * 10000) / 10000;
		ratio = (ratio * 10000) / 10000;
		if(ratio != ratioRounded)
		{
			ratio = Math.floor(ratio * 1000) / 1000; // Remove the last digit
			ratio += '~';
		}
		writeln('Ratio: '+rMax+':'+rMin+' ('+mod+') or '+ratio);
		break;
	}
	mod--;
}