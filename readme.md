# python-inside-html
Render Python inside HTML with good performance.

Based on standalone library inside very old Karigell Framework, Updated to work with Python 3.6

# Why?
Although i have not written the base implementation myself i believe this framework or ones like it are very important.
Rather then building a template engine in Python via Classes, Parsers, Evaluators, etc. PIH uses Meta Circular Evaluation whereby code intermixed with HTML gets parsed as Python code and then run on the Python VM natively.

Besides increasing performance the fact that we are talking about 1 Language being able to evaluate a other language intermixed and meta circular is a very interesting concept.

Doing the inverse of something Meta does not actually decrease its abstraction. It increases it.
i.e 

Meta ^ 1 = Evaluation

Meta ^ 2 = Virtualization

Meta ^ 3 = Inverse Virtualization

To Illustrate:
![Meta Circular EvaluationVirtual Machine](https://i.imgur.com/MCq4QLp.png)


# Render Whole Python Scripts in HTML

```HTML
<% 
   x = 1
   y = True
   z = {}
%>
<% while x < 100 or y == False: %>
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
x = env.get("x", "") #global variables are stored in env just like a normal python exec
y = env.get("y", "")
z = env.get("z", "")
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

