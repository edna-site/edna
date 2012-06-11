from __future__ import with_statement
from types import ListType, TupleType
import logging
from xdscfgformat import CONFIGURATION_PARSERS
from xdscfgformat import REPEATABLE_PARAMS

# Load a XDS file, remove the comments, and then split it into a list
# of (keyword, [args]) tuples
def _load_xds_file(path):
    parsedlst = list()
    filelines = []
    with open(path, 'r') as f:
        filelines = f.readlines()
    cleanedup = _uncomment(filelines)

    for line in cleanedup:
        kwds = []

        # since there can be no space between the kw and its first arg
        # we'll make 2 passes to split on whitespace and then resplit
        # kw and 1st arg in this case
        partial_tokens = line.split()
        tokens = list()
        for t in partial_tokens:
            idx = t.find('=')
            # not a kw or already isolated kw
            if idx == -1 or idx == len(t)-1:
                tokens.append(t)
            #kw=firstarg case, split them
            else:
                # keep the = sign a the end of the kw
                tokens.append(t[:idx+1])
                tokens.append(t[idx+1:])

        # look for keywords
        for token, idx in zip(tokens, range(len(tokens)+1)):
            if token.endswith('='):
                kwds.append(idx)
        if len(kwds) == 0:
            #no kw on line, next
            continue
        #we now have the positions for the kw in the line
        #args start right after keywords
        argsstart = [i+1 for i in kwds]
        # and end right before the next one of at the end
        argsend = kwds[1:]
        argsend.append(len(tokens))

        for kw, start, end in zip(kwds, argsstart, argsend):
            parsedlst.append( (tokens[kw], tokens[start:end]) )
    return parsedlst

def parse_xds_file(path):
    parsed = dict()
    loaded = _load_xds_file(path)

    # pythonize the arguments
    for kw, args in loaded:
        if kw not in CONFIGURATION_PARSERS:
            # XXX maybe log it
            continue
        parser = CONFIGURATION_PARSERS[kw]

        #print 'parsing', args, 'with', parser, 'for kw', kw

        # XXX maybe catch exc and log them
        parsedargs = parser(args)

        # special case, for repeatable params, we add them as a list
        # or append them if they already exist
        if kw in REPEATABLE_PARAMS:
            #print 'keyword', kw, 'is repeatable'
            if kw in parsed:
                parsed[kw].append(parsedargs)
            else:
                parsed[kw] = [parsedargs]
        else:
            # regular case just assign the thing
            parsed[kw] = parsedargs

    return parsed

# expects a list of line
# remove comments and strip()s
# only returns non empty lines
def _uncomment(lines):
    res = list()
    for line in lines:
        commentstart = line.find('!')
        if commentstart != -1:
            uncommented = line[:commentstart].strip()
            if len(uncommented) > 0:
                res.append(uncommented)
        else:
            stripped = line[:].strip()
            if len(stripped) > 0:
                res.append(stripped)
    return res

def dump_xds_file(filename, xdsconf):
    with open(filename, 'w') as outfile:
        for key in xdsconf:
            value = xdsconf[key]
            # repeatable keywords have a list associated, we have to
            # repeat the kw along with the values
            if key in REPEATABLE_PARAMS:
                for val in value:
                    outfile.write(_format_param(key, val))
            else:
                outfile.write(_format_param(key, value))

def _format_param(key, value):
    """return a string in the form
key= value value value
taking into account whether value is a list of things or a single
value"""
    if type(value) in [ListType, TupleType]:
        valstring = ' '.join(map(str, value))
        res = '{0} {1}\n'.format(key, valstring)
    else: #single val
        if type(value) == bool:
            value = 'TRUE' if value else 'FALSE'
        res = '{0} {1}\n'.format(key, value)

    return res
