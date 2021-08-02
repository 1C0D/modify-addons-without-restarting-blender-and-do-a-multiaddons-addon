import bpy

from . import utils #needed to reload. if too heavy you can use a debug conditions
from .utils import ChangeAge


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"
    bl_options = {'UNDO'}    

    def execute(self, context):

        print('bbb')
        ChangeAge.print_name() # try a change in utils
        x = ChangeAge(16)
        x.print_age()      

        return {'FINISHED'}


def register():
    import importlib
    importlib.reload(utils) ## 
    
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
