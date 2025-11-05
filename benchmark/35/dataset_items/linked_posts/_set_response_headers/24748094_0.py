#!/usr/bin/env python

import bottle


@bottle.get("/static/js/<filename:re:.*\.js>")
def javascripts(filename):
    response = bottle.static_file(filename, root="./static/js/")
    response.set_header("Cache-Control", "public, max-age=604800")
    return response

bottle.run(host="localhost", port=8000, debug=True)
