# reactPy
ReactPy is a Python library that enables developers to create dynamic and interactive user interfaces, resembling the functionalities of ReactJS, while eliminating the need for JavaScript dependency.
Firstly we create a virtual environment: 
        pip install virtualenv
 After that Creating a Virtual environment with the help of Command :  
 
         virtualenv -p /usr/bin/python/folder_name
         
Now, install ReactPy run the following command:

         pip install "reactpy[starlette]"
         
and you can install more than one option by separating them with commas.

       pip install "reactpy[fastapi,flask,sanic,starlette,tornado]"
       
AT the last end Write a code any text editor e.g Sublime or Notepad++.

I'll break down what each line does here:

1. The first line, "from reactpy import component, html, run," imports the required components from the "reactpy" library. 'html' offers functions to create HTML elements, 'component' is a decorator used to define React components, and 'run' is used to execute the React application.

2. The decorator "@component" designates the ensuing function as a React component.

3. "def Show():": This declares the "Show" function, which symbolises a React component.

4. The line that reads "return html.h1("Hello, world!")" specifies the return value for the "Show" component. It creates an HTML heading element ('h1>') with the text "Hello, world!" using the 'html.h1' function from the 'html' module.
   
5. The React application is launched with the command "run(Show, host="192.168.11.19", port=7000)". The application is launched using the 'run' function from the 'reactpy' library. The root component of the application is passed as the 'Show' component. The IP address and port number on which the application will be hosted are specified by the "host" and "port" arguments. In this instance, it will be accessible via port 7000 and IP address "192.168.11.19."
   
6. The code above creates a straightforward React component called "Show" that renders an HTML heading element with the text "Hello, world!" After that, the React application is launched and hosted at the given IP address and port.
