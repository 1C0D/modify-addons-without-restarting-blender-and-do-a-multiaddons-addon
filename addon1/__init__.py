bl_info = {
    "name": "addon1",
    "author": "bbb",
    "blender": (2, 93, 0),
    "version": (0, 1, 1),
    "category": "Object"
}


modules = ("op", "panel")


for mod in modules:
    exec(f"from . import {mod}")


def register():
    import importlib

    for mod in modules:
        exec(f"importlib.reload({mod})") #to import this init in the main init, I disable this. but not if addon1 was stand alone
        exec(f"{mod}.register()")


def unregister():
    for mod in modules:
        exec(f"{mod}.unregister()")
