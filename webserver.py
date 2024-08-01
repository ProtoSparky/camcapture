import pyassets.tools as tools 
settings_dir = "./settings.json"
try:
    settings = tools.open_json(settings_dir)
except:
    print("Settings file missing! Run setup.py")
    exit()

tools.launch_html_server("./", settings["web_port"], False)
