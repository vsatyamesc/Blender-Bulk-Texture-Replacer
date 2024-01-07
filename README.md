# Blender-Bulk-Texture-Replacer
### If you are using Blender 4.0, download the **replacing_addone.py** directly from repository and install it like usual. If you do not see the Python file in the Blender Addon Installation Window make a zip of this Python file.
Install the Tool.
 
The Convertor should be inside the "Tool" UI.

## Bulk Texture Replacer
>> 1. It can replace bulk replace textures with your input name
>> 2. Another use case, suppose you have a texture image which is applied to a lot of objects, you can run this addon to rename the texture to your new one, basically Remapping the texture with your new one. Works like Remap user in blender file API.
Before Using:
Use a convertor tool to convert all your texture files into whatever you want
 
Usage:
1. Click on Replace button
2. A Dialog Will appear.
3. In Original (which is current extension) put the extension name.
4. In Resultant (Which you want to replace to) put the next extension name.
5. Press Enter or OK or LMB on 3D viewport.
6. Now, File > External Data > Find Missing File and go where your converted texture files are.
 
This should bulk replace all the texture files.

## New Feature: Bulk Blend Type Changer

Added Bulk Blend Type Change Feature.

This "Change" feature should be just below your "Bulk Text Replacer".

Usage:
1. Click on Change Button.
2. A Dialog will appear.
3. In Original, select the Blend Type from which you want to Change (All: for replacing all the Blend Type)
4. In Resultant, select the type you want to convert to.
5. Click "OK"

## New Feature: Bulk Rename Objects
Works like above.

# Remove Unused Nodes
```Use this on the Scripting Tab on Blender. Copy-Paste the Code and Run. ```
Removes the unused nodes from the shader editor of all the materials.

## If you run into Error please raise an issue. But before that please copy the errors from "System Console Window" and paste in the issue.
