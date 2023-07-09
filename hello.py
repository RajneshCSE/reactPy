from reactpy import component, html, run
@component
def Show():
    return html.h1("Hello, world!")
    
run(Show,host="192.168.11.19",port=7000)