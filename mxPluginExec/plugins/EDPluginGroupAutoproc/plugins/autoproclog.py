import httplib
import urllib
import logging

LOG_SERVER=None
CONNECTION_TIMEOUT=3

def log(**kwargs):
    param_names = ['datacollect_id', 'processing_type', 'beamline',
                   'succeeded', 'creation_time', 'xds_runtime',
                   'total_time', 'inner_i_over_sigma', 'inner_r_value real',
                   'outer_i_over_sigma', 'outer_r_value',
                   'overall_i_over_sigma', 'overall_r_value',
                   'comments']
    # debugging aid
    extra = [k for k in kwargs.keys() if k not in param_names]
    missing = [k for k in param_names if k not in kwargs.keys()]
    logging.debug('extra keys: %s', extra)
    logging.debug('missing keys: %s', missing)

    if LOG_SERVER is None:
        logging.error('no logging server specified')
        return
    params = urllib.urlencode(kwargs)
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "application/json"}
    conn = httplib.HTTPConnection(LOG_SERVER, timeout=CONNECTION_TIMEOUT)
    conn.request('POST', '/log', params, headers)
    response = conn.getresponse()
    data = response.read()
    return response.status, data
