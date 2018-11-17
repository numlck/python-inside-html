#import PythonInsideHtml36 as pih
import sys
sys.path.append("..")

import PythonInsideHtml36 as pih
import functools
import time
import os
from flask import Flask, request, abort

app = Flask(__name__)


template_cache = {}
def render_template(file, **kwargs):
	start_time = time.time()
	if not template_cache.get(file):
		template  = pih.PIH(file)
		code = template.pythonCode()
		template_cache[file] = code
	
	e = dict(env)
	e.update({
		"debug_start_time":start_time,
	})
	e.update(**kwargs)

	exec(template_cache.get(file), e)
	return e["py_code"].getvalue()

env = {
	"include":render_template,
	"time":time,
}

@app.route("/")
@app.route("/<path:location>", methods=["GET"])
def index(location):
	if os.path.exists(location):
		return render_template(location)
	else:
		return abort(404)

if __name__ == '__main__':
    app.run()
