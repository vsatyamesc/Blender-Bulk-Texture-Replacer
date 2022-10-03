bl_info = {
    "name": "Bulk Texture Replace",
    "author": "Seven3D",
    "version": (1, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Tool > Replace Texture(s)",
    "description": "Bulk Replace the Texture",
    "warning": "",
    "doc_url": "https://pastebin.com/XBnJSWrj",
    "category": "Tool",
}

import bpy
from bpy.types import (Panel, Operator)
from bpy.utils import register_class, unregister_class
from bpy.props import (StringProperty,BoolProperty,IntProperty,FloatProperty,EnumProperty)

class RANOperator(bpy.types.Operator):
    """Replaces the Texture to whatever you want"""
    bl_idname = "cobject.cs1"
    bl_label = "Converter"
    ############################################### REMOVE THIS COMMENT IF NOT WORKING ################# bl_options = {'REGISTER', 'UNDO'} # You need this for Adjust Last Operation panel
    Original: StringProperty(
        name="Original",
        default=".dds",
        description="the extension name with '.' before it",
    ) # you could add more of these
    
    Resultant: StringProperty(
        name="Resultant",
        default=".png",
        description="the extension name with '.' before it",
    ) # you could add more of these   
    def execute(self, context):
        for i in bpy.data.images:
            i.filepath = i.filepath.replace(self.Original, self.Resultant)
            i.name = i.name.replace(self.Original, self.Resultant) 
        return {'FINISHED'}
    def invoke(self, context, event): ########################################################REMOVE THIS IF TOO NOT WORKING##########################################
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class COS(bpy.types.Panel):
    bl_label = "Replace Texture(s)"
    bl_idname = "cobject_PT_"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout  
        row = layout.row()
        row.operator(RANOperator.bl_idname, text = "Replace", icon = "UV_SYNC_SELECT")
        
_classes = [ RANOperator, COS]       

def register():
    for cls in _classes:
        register_class(cls)
    
def unregister():
     for cls in _classes:
        unregister_class(cls)
     
if __name__ == "__main__":
    register()
