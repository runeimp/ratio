#!/usr/bin/env python3
"""
Ratio

@license MIT


ChangeLog
---------
2017-01-24  1.2.0      Updated using Python 3 and added display spec features
2014-22-24  1.1.0      Updated using NodeJS
2010-12-12  1.0.0      Initial creation with JSDB
"""

# __all__ = []
__version__ = '1.2.0'
__author__ = 'RuneImp <runeimp@gmail.com>'

import argparse
import json
import locale
import math
import re

#
# DEV CONSTANTS
#
APP_NAME = 'Ratio'
CLI_NAME = 'ratio'
APP_VERSION_MAJOR = 1
APP_VERSION_MINOR = 2
APP_VERSION_PATCH = 0
APP_VERSION = "{}.{}.{}".format(APP_VERSION_MAJOR, APP_VERSION_MINOR, APP_VERSION_PATCH)
APP_LABEL = "{} v{}".format(APP_NAME, __version__)

#
# CONSTANTS
#
DIMENSIONS_RE = re.compile('([0-9]+)[^0-9]([0-9]+)')
DISPLAY_SPEC = {
	0.6666666666666666: {    #   2:3
		'spec': '2:3, Analog Video Tape',
		320: 'Betamax, VHS', # 320x480
	},
	1.0: {              #    1:1
		'spec': 'Square',
		1024: 'Square', # 1024x1024
		800: 'Square',  #  800x800
		640: 'Square',  #  640x640
		480: 'Square',  #  480x480
		320: 'Square',  #  320x320
		240: 'Square',  #  240x240
	},
	1.25: {            #    5:4
		'spec': '5:4, SXGA',
		2560: 'QSXGA', # 2560x2048
		1280: 'SXGA',  # 2560x2048
	},
	1.3333333333333333: { #    4:3
		'spec': '4:3, NTSC, PAL, VGA',
		2048: 'QXGA',     # 2048x1536
		1600: 'UXGA',     # 1600x1200
		1400: 'SXGA+',    # 1400x1050
		1280: 'QVGA *',   # 1280x960 (non standard spec. Why is that?)
		1152: 'XGA+',     # 1152x864
		1024: 'XGA',      # 1024x768
		800: 'SVGA',      #  800x600
		768: 'PAL',       #  768x576
		640: 'NTSC, VGA', #  640x480
		320: 'qVGA',      #  320x240
	},
	1.5: {                #   3:2
		'spec': '3:2, D1, HVGA',
		720: 'D1, DVD',   # 720x480
		480: 'HVGA',      # 480x320
	},
	1.6: {          #   8:5
		'spec': '8:5, CGA',
		320: 'CGA', # 320x200
	},
	1.6666666666666667: { #    5:3
		'spec': '5:3, WVGA',
		1280: 'WXGA',     # 1280x768
		800: 'WVGA',      #  800x480
	},
	1.7777777777777777: {        #   16:9
		'spec': '16:9, HD',
		3840: '2160p, UHD-1',    # 3840x2160
		2560: '1440p, WQHD',     # 2560x1440
		1920: '1080p, FHD, XHD', # 1920x1080
		1280: '720p, HD',        # 1280x720
		1024: 'Wide PAL',        # 1024x576
		854: 'WVGA, Wide NTSC',  #  854x480
	},
	1.8962962962962964: { # K Series
		'spec': '256:135, #K',
		8192: '8K',       # 8192x4320
		4096: '4K',       # 4096x2160
		2048: '2K',       # 2048x1080
		1024: '1K',       # 1024x540
	},
	2.3333333333333335: { # 21:9
		'spec': '21:9, Ultra Wide',
	},
	2.388888888888889: {  # 43:18, Ultra Wide. What they call 21:9
		'spec': '43:18, Ultra Wide',
		3440: 'UWQHD',    # 3440x1440
		# ____: '____',
		# ____: '____',
	},
	2.3703703703703702: { # 64:27, Ultra Wide. What they call 21:9
		'spec': '64:27, Ultra Wide',
		2560: 'UWHD',      # 2560x1080
	}
}


#
# VARIABLES
#
dim_h = 0     # Dimension Height
dim_w = 0     # Dimension Width
ratio_d = 0   # Ratio Divisor
ratio_f = 0.0 # Ratio Float
ratio_h = 0   # Ratio Height
ratio_o = ""  # Ratio Output
ratio_r = 0.0 # Ratio Rounded
ratio_w = 0   # Ratio Width
pixels = 0    # Pixle Count


#
# FUNCTIONS
#
def close_to(ratio):
	"""Returns the standard ratio the ratio is close too"""
	
	tolerance = 1e-01
	if ratio != 1 and math.isclose(ratio, 1.0, rel_tol=tolerance):
		result = ('1:1', '1.000¯', 'Square')
	elif ratio != 1.3333333333333333 and math.isclose(ratio, 1.3333333333333333, rel_tol=tolerance):
		result = ('4:3', '1.333¯', 'NTSC, PAL, VGA')
	elif ratio != 1.7777777777777777 and math.isclose(ratio, 1.7777777777777777, rel_tol=tolerance):
		result = ('16:9', '1.777¯', 'HD')
	elif ratio != 1.5 and math.isclose(ratio, 1.5, rel_tol=tolerance):
		result = ('3:2', '1.5000', 'D1')
	elif ratio != 2.3333333333333335 and math.isclose(ratio, 2.3333333333333335, rel_tol=tolerance):
		result = ('21:9', '2.333~', 'Ultra Wide')
	else:
		result = None

	return result

def get_display_spec(ratio, width):
	"""Get the Display Spec"""
	# print("get_spec() | width: {} | ratio: {}".format(width, ratio))

	try:
		if DISPLAY_SPEC[ratio_f]:
			result = DISPLAY_SPEC[ratio_f]['spec']
			if DISPLAY_SPEC[ratio_f][dim_w]:
				result = DISPLAY_SPEC[ratio_f][dim_w]
	except:
		if result == None:
			result = 'unknown'

	return result


#
# PARSE ARGUMENTS
#
parser = argparse.ArgumentParser(add_help=False, description='Ratio: the ratio parser!', prefix_chars="-/", prog=APP_NAME)
parser.add_argument('dimensions', nargs='+', help='dimensions to process')
parser.add_argument('-a', '--alternate', '/alt', action='store_true', help='Use alternate output format')
parser.add_argument('-h', '--help', '/help', action='help', help='Show this help message and exit')
parser.add_argument('-j', '--json', '/json', action='store_true', help='Output as JSON')
parser.add_argument('-v', '--version', '/ver', action='version', help="Show program's version number and exit", version='%(prog)s {}'.format(__version__))
args = parser.parse_args()


#
# Initialization
#
locale.setlocale(locale.LC_ALL, 'en_US')

args_len = len(args.dimensions)

if args_len == 0:
	parser.parse_args('-h')
	exit(1)
elif args_len == 1:
	match = DIMENSIONS_RE.match(args.dimensions[0])
	# print("match: {} | {}:{}".format(match, match[1], match[2]))
	dim_w = int(match[1])
	dim_h = int(match[2])
else:
	dim_w = int(args.dimensions[0])
	dim_h = int(args.dimensions[1])

ratio_f = dim_w / dim_h
pixels = dim_w * dim_h
mega_pixels = pixels / 1024 / 1024
ratio_r = int(ratio_f * 1000) / 1000
ratio_d = math.gcd(dim_w, dim_h)
ratio_w = int(dim_w / ratio_d)
ratio_h = int(dim_h / ratio_d)

if dim_w == dim_h:
	ratio_o = "1.000¯"
elif ratio_f != ratio_r:
	ratio_o = "{:.3f}~".format(ratio_r)
else:
	ratio_o = "{:.4f}".format(ratio_f)

# print("Dimensions: {}x{}".format(dim_w, dim_h))

is_close = close_to(ratio_f)

if args.json:
	json_data = {
		'ratios': ["{}:{}".format(ratio_w, ratio_h), ratio_o],
		'divisor': ratio_d,
		'pixels': [pixels, "{:,.2f} MP".format(mega_pixels)],
		'spec': get_display_spec(ratio_f, dim_w),
	}
	if json_data['spec'] == 'unknown':
		json_data['spec'] = None
	if is_close:
		json_data['close_to'] = [is_close[0], is_close[1], is_close[2]]
	print(json.dumps(json_data))
else:
	print("")
	if args.alternate:
		print("    Ratios:   {}:{} | {}".format(ratio_w, ratio_h, ratio_o))
	else:
		print("    Ratios:   {}:{} ({})".format(ratio_w, ratio_h, ratio_o))
		# print("    Ratios:   {}:{} ({}) {}".format(ratio_w, ratio_h, ratio_o, ratio_f))
	print("    Divisor:  {}".format(ratio_d))
	print("    Pixels:   {:,} or {:,.2f} MP".format(pixels, mega_pixels))
	print("    Spec:     {}".format(get_display_spec(ratio_f, dim_w)))
	if is_close:
		if args.alternate:
			print("    Close to: {} | {} | {}".format(is_close[0], is_close[1], is_close[2]))
		else:
			print("    Close to: {} ({}) '{}'".format(is_close[0], is_close[1], is_close[2]))
	print("")


exit(0)
