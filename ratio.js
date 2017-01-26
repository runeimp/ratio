#!/usr/bin/env node
/*
Ratio Calculator

@author RuneImp <runeimp@gmail.com>
@license MIT

ChangeLog
---------
2014-22-24  1.1.0      Updated using NodeJS
2010-12-12  1.0.0      Initial script creation using JSDB
*/

var args = process.argv.slice(2),
	max, min, mond,
	platform = process.argv[0],
	script = process.argv[1];

if(args.length < 2)
{
	var msg = '\n';
	msg += 'Must supply two numbers to devine the ratio.\n';
	msg += '\n';
	msg += 'Output Example:\n';
	msg += '    Ratio: 16:9 (divisor) or 1.777~\n';
	msg += '\n';
	msg += 'The last number is the larger argument divided by the smaller argument.\n';
	console.log(msg);
	process.exit(1);
}
else
{
	console.log('\n    Caclulating ratio of '+args[0]+'×'+args[1]);
}

max = Math.max(args[0], args[1]);
min = Math.min(args[0], args[1]);
mod = min;
points = max * min;

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
		console.log('    Ratio: '+rMax+':'+rMin+' ('+mod+') or '+ratio);
		console.log('    Points: '+points+'\n')
		break;
	}
	mod--;
}
process.exit(0);