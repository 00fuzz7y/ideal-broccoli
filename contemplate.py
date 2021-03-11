from mako.template import Template  #basic Template

""" the goal of this module is to use the best of mako, jinja2, and genshi
    that said, the only way to avoid this becoming an involved mess is vision

    since this is to be a multi-system manager, we need a Template design
    Our Template is a console window, so maybe start with those constraints"""
#-80--this---is---a----bunch----of-----filler----to----show---console---width-|


class Field:
    def __init__(self, n, ty, d):   # field: (title, type, default, format)
        self._name = n
        self._type = ty
        self._default = d

class Group:
    def __init__(self, n, o, f):     # Group(name, fields, orientation)
        self._name = n
        self._order = o
        self._fields = f
        
"""    
name:'Strength' abbr:"STR" descr:"Raw might." def:1 base:def current:def
    after we input for Strength we can use that as a Template for Attribute 
    console.width is our buffer.length and we should try to fill it out


    groupings of templates output as templates
    context: 
"""
