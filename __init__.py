bl_info = {
    "name": "quick multi addons",
    "author": "bbb",
    "blender": (2, 93, 0),
    "version": (0, 0, 0),
    "category": "Object"
}

"""
first easy and quick to group several addons
and whith the debug on you can edit your scripts without having to restart blender.

"""

modules_in_folders = {

"addon1": {"op", "panel"},

"" : {"single_file_addon"},

"meshcheck": {"preferences", "properties", "ui"}

}
    
for folder,moduls in modules_in_folders.items():
    for mod in moduls:
        exec(f"from .{folder} import {mod}")


#N.B: classes are registered in each module 
def register():
    
    import importlib

    for folder,moduls in modules_in_folders.items():
        for mod in moduls:
            exec(f"importlib.reload({mod})")
            exec(f"{mod}.register()")


def unregister():
        
    for folder,moduls in modules_in_folders.items():
        for mod in moduls:
            exec(f"{mod}.unregister()")


