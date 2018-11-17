# python-inside-html
Standalone Library based on very old Karigell Framework, Updated to Python 3.6

Backend Example: 
  ```Python
  env = {
    "time":time
    "t1":time.time(),
  }
  template  = pih.PIH(file)
	code = template.pythonCode()
  exec(code, e)
  
  rendered = e["py_code"].getvalue()
  ```
  
Frontend Example
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
