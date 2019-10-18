def PrintException():
    import sys
    import linecache
    import logging
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.ERROR, datefmt='%Y-%m-%d %I:%M:%S')
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    msg = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    logging.error(msg)
    return msg
