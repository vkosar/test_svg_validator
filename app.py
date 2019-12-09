import rnginline
from lxml import etree

svg_file = 'sign-abc.svg'
html_file = 'iframe.html'

rng_dir = './TinySVG-rng'
rng_file = 'Tiny-1.2.rng'

svg_validator = rnginline.inline(path=rng_dir + '/' + rng_file)
#print(dir(svg_validator))

svg_doc = etree.parse(svg_file)
#print(etree.tostring(svg_doc))
v1 = svg_validator.validate(svg_doc)
print('SVG valudate %s' % v1)

html_doc = etree.parse(html_file)
#print(etree.tostring(html_doc))
v2 = svg_validator.validate(html_doc)
print('HTML valudate %s' % v2)
