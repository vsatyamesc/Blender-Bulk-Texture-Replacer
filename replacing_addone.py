bl_info = {
    "name": "Bulk Replace",
    "author": "Satyam",
    "version": (1, 2),
    "blender": (3, 0, 0),
    "location": "View3D > Tool > Replace Texture(s)",
    "description": "Bulk Replace the Texture \n Bulk convert Blend Mode \n Bulk Name Replace",
    "warning": "",
    "doc_url": "https://github.com/vsatyamesc/Blender-Bulk-Texture-Replacer/blob/main/README.md",
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
    Original: StringProperty(
        name="Original",
        default=".dds",
        description="the extension name with '.' before it",
    ) # you could add more of these
    
    Resultant: StringProperty(
        name="Resultant",
        default=".png",
        description="the extension name with '.' before it",
    ) # you can add more of these   
    
    def execute(self, context):
        for i in bpy.data.images:
                try:
                    i.filepath = i.filepath.replace(self.Original, self.Resultant)
                    i.name = i.name.replace(self.Original, self.Resultant)
                    print("done")
                except:
                    print("replace failed")   
        return {'FINISHED'}
    def invoke(self, context, event): 
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class ReANOperator(bpy.types.Operator):
    """Renames/Changes part of name to whatever you want"""
    bl_idname = "cobject.cs3"
    bl_label = "Rename/Replace"
    Original: StringProperty(
        name="Original",
        default="Defualt",
        description="File Name, or the word that you want to replace",
    )
    
    Resultant: StringProperty(
        name="Resultant",
        default="Final",
        description="New Name",
    ) 

    def execute(self, context):
        i = 0
        for obj in bpy.data.objects:
            i=i+1
            if self.Original in obj.name:
                try:
                    obj.name = str(obj.name).replace(self.Original,self.Resultant)
                except:
                    print("Error Occured at " + obj.name )
            else:
                pass
            if i == len(bpy.data.objects)-1:
                break
        return {'FINISHED'}
        
    def invoke(self, context, event): 
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class BANOperator(bpy.types.Operator):
    """Replaces the Texture to whatever you want"""
    bl_idname = "cobject.cs2"
    bl_label = "Changer"
    inz_initial: bpy.props.EnumProperty(
        name="Original",
        description='Select the Blend Type of your Object',
        items = [
            ("0","All", "Every Blend type"),
            ("1","Blend", "Alpha Blend type"),
            ("2","Hashed", "Alpha Hashed type"),
            ("3","Clip", "Alpha Clip type"),
            ("4","Opaque", "Opaque type")
        ]
    )
    inz_final: bpy.props.EnumProperty(
        name="Final",
        description='Select the Blend Type of your Object',
        items = [
            ("1","Blend", "Alpha Blend type"),
            ("2","Hashed", "Alpha Hashed type"),
            ("3","Clip", "Alpha Clip type"),
            ("4","Opaque", "Opaque type")
        ]
    )
    def blendmd_chk(self,initial=None,final=None):
        switcher = {"0":"All", "1":"BLEND","2":"HASHED","3":"CLIP","4":"OPAQUE"}
        initial = switcher[initial]
        if initial == "All" or None:
            initial = ["BLEND","HASHED","CLIP","OPAQUE"]
        else:
            pass
        if final == None:
            final = switcher["4"]
        final = switcher[final]
        return [initial, final]

    def execute(self, context):
        context = bpy.context
        res = self.blendmd_chk(self.inz_initial,self.inz_final)
        print(res)
        try:
           for o in bpy.data.materials:
                if res[0] == res[1]:
                    pass
                elif isinstance(res[0],list):
                    if o.blend_method in res[0]:
                        o.blend_method = res[1]
                    else:
                        if o.blend_method is None:
                            print("Object"+str(o)+"is NoneType")
                elif o.blend_method == res[0]:
                    o.blend_method = res[1]
                else:
                    print("Error processing object : "+str(o))
        except:
            print("Tis Not Working")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Convert From")
        row = col.row()
        row.prop(self, "inz_initial")
        
        col.label(text="Convert To")
        col.prop(self, "inz_final")  

       
class COS_PT_gg(bpy.types.Panel):
    bl_label = "Replace Texture(s)"
    bl_idname = "cobject_PT_"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout  
        row = layout.row()
        row.operator(RANOperator.bl_idname, text = "Replace", icon = "UV_SYNC_SELECT")

class COS1_PT_gg(bpy.types.Panel):
    bl_label = "Change Blend Mode"
    bl_idname = "cobject_PT1_"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout  
        row = layout.row()
        row.operator(BANOperator.bl_idname, text = "Change", icon = "GP_MULTIFRAME_EDITING")

class COS2_PT_gg(bpy.types.Panel):
    bl_label = "Rename Objects"
    bl_idname = "cobject_PT2_"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout  
        row = layout.row()
        row.operator(ReANOperator.bl_idname, text = "Rename", icon = "OUTLINER_DATA_GP_LAYER")
        
_classes = [ RANOperator,ReANOperator, BANOperator, COS_PT_gg, COS1_PT_gg,COS2_PT_gg]       

def register():
    for cls in _classes:
        register_class(cls)
    
def unregister():
     for cls in _classes:
        unregister_class(cls)
     
if __name__ == "__main__":
    register()
