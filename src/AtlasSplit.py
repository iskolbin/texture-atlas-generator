#!/usr/bin/env python

from PIL import Image
import os
import sys
from xml.dom import minidom

def main():
    
    if len( sys.argv ) < 2:
        print( 'needed argument: path to image and xml' )
        print( 'like ./AtlasSplit.py images/atlas' )
        print( 'if atlas.png and atlas.xml in the "images" folder' )
        return False
    
    im = Image.open( sys.argv[1] + '.png' )
    
    for sxml in minidom.parse( sys.argv[1] + '.xml' ).getElementsByTagName('SubTexture'):
        s = { 'name': sxml.getAttribute('name'), 'x': sxml.getAttribute('x'), 'y': sxml.getAttribute('y'), 'width': sxml.getAttribute('width'), 'height': sxml.getAttribute('height')}
        x, y, width, height = int( sxml.getAttribute('x')), int( sxml.getAttribute('y')), int( sxml.getAttribute('width')), int( sxml.getAttribute('height'))
        name = sxml.getAttribute('name')
        subim = Image.new( 'RGBA', ( width, height ), (0,0,0,0) )
        subim.paste( im.crop(( x, y, x+width, y+height )))
        subim.save( '%s.png' % name )
   
    print 'Success'

    return True

if __name__ == "__main__":
    main()
