# python-inside-html
Render Python inside HTML with good performance.

Based on standalone library inside very old Karigell Framework, Updated to work with Python 3.6

# Render Whole Python Scripts in HTML

```
<% x = 1 %>
<% while x < 100: %>
	<p><%= x %></p>
	<% x += 1 %>
<% end %>
```

# Bi-Directional Data Flow

Backend
```Python
import time
import PythonInsideHTML36 as pih

env = {}
template  = pih.PIH("filepath")
code = template.pythonCode()
exec(code, env)

html = env["py_code"].getvalue()
data = env["x"]

```

# Render blocks and statements
```
<% if x: %>
	output someting
<% end %>
<% else: %>
	output someting else
<% end %>
```

# Render expressions
```
<%= time.time() - t1 %>s
```

f you want to exit the script before the end of the document, raise a 
SCRIPT_END exception
```
    raise SCRIPT_END(message)
```
# Backend Example: 
```Python
import time
import PythonInsideHTML36 as pih

env = {
"time":time,
"t1":time.time()
}
template  = pih.PIH("filepath")
code = template.pythonCode()
exec(code, env)

rendered = env["py_code"].getvalue()
```

Notes:
	```template.pythonCode()``` returns a ```compile()``` code object, which you can store in a variable and call a different ```env``` along a ```exec()``` so its plenty fast. 
	
Uncached renders at 0.003 seconds with a couple includes, cached renders pretty much instantly. 


See Examples/fileserver.py
  
# Frontend Example
```HTML
<html>

	<head></head>
	<body>
		<h1>Hello from Python Inside HTML</h1>
		<center>
    		Rendered in: <%= time.time() - t1 %>s

		</center>

	</body>
</html>

```

