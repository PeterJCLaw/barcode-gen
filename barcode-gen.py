#!/usr/bin/env python3
import time
import argparse
import re
import pyqrcode
import io

templates = {
# -----------------------------------------------------------------
#
#                           KIT LABEL
#
# -----------------------------------------------------------------
    "kit_label": """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="90mm"
   height="29mm"
   viewBox="0 0 90 29"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.3 (2405546, 2018-03-11)"
   sodipodi:docname="KitLabel.svg">
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="2.8"
     inkscape:cx="165.21401"
     inkscape:cy="38.384659"
     inkscape:document-units="mm"
     inkscape:current-layer="g1046"
     showgrid="true"
     inkscape:window-width="1600"
     inkscape:window-height="837"
     inkscape:window-x="-8"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     showguides="false"
     inkscape:snap-text-baseline="true"
     inkscape:snap-object-midpoints="true"
     inkscape:object-nodes="false"
     inkscape:snap-bbox="true"
     inkscape:bbox-nodes="true">
    <sodipodi:guide
       position="-30.201457,-41.694046"
       orientation="0.70710678,0.70710678"
       id="guide1861"
       inkscape:locked="false" />
    <inkscape:grid
       type="xygrid"
       id="grid1863"
       originx="0"
       units="mm"
       spacingx="2.5"
       spacingy="2.5" />
  </sodipodi:namedview>
  <defs
     id="defs2" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(0,-268.00001)">
    <g
       transform="matrix(0.264583,0,0,0.264583,6.740765,281.94758)"
       inkscape:label="DataMatrix"
       id="g1046">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:16.00002098px;line-height:125%;font-family:'OCRA';-inkscape-font-specification:'OCRA';text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         x="163.49968"
         y="9.6469927"
         id="text1855"><tspan
           sodipodi:role="line"
           id="tspan1853"
           x="163.49968"
           y="9.6469927"
           style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:32.00004196px;font-family:'OCRA';-inkscape-font-specification:'OCRA';text-align:center;text-anchor:middle;stroke-width:1.00000131px">{code}</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:16.00002098px;line-height:125%;font-family:sans-serif;-inkscape-font-specification:sans-serif;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         x="163.49968"
         y="-22.699499"
         id="text1859"><tspan
           sodipodi:role="line"
           id="tspan1857"
           x="163.49968"
           y="-18.699499"
           style="text-align:center;text-anchor:middle;stroke-width:1.00000131px">SR part code</tspan></text>
           <g transform="translate(-30,-55)"> {bar} </g>
            <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:16.00002098px;line-height:100%;font-family:sans-serif;-inkscape-font-specification:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         x="87.909027"
         y="28.544655"
         id="text5574"><tspan
           sodipodi:role="line"
           id="tspan5572"
           x="87.909027"
           y="28.544655"
           style="font-size:10.66668034px;line-height:100%;stroke-width:1.00000131px">Property of Student Robotics</tspan><tspan
           sodipodi:role="line"
           x="87.909027"
           y="44.544678"
           style="font-size:10.66668034px;line-height:100%;stroke-width:1.00000131px"
           id="tspan5576">Do not remove or cover this label</tspan></text>
      <g
         id="Symbol"
         style="fill:none;fill-rule:evenodd;stroke:none;stroke-width:1"
         transform="matrix(0.06216337,0,0,0.06216336,248.53915,-37.597162)">
        <path
           id="Combined-Shape"
           d="M 677.02569,617.02111 C 647.86936,653.56793 611.78587,684.96457 570,709.08965 c -117.57241,67.88047 -262.42759,67.88047 -380,0 C 149.36918,685.63144 114.12985,655.29811 85.407993,620.03996 237.45689,462.35413 363.12698,500.77008 363.12698,444.72918 c 0,-58.40687 -216.99267,-96.85099 -216.99267,-137.37364 0,-40.41177 127.88133,-71.09181 236.54807,-71.25942 108.66671,0.16761 236.54802,30.84765 236.54802,71.25942 0,40.52265 -216.99268,78.96677 -216.99268,137.37364 0,55.6804 124.05847,18.11529 274.78795,172.29195 z m 31.57148,-46.17064 C 627.79949,503.08549 552.57476,461.04506 482.92298,444.72918 c 34.56671,-27.89165 229.03772,-98.84427 229.03772,-136.825 0,-37.84011 -167.95212,-128.40681 -328.38423,-129.07691 -0.298,-0.004 -0.59603,-0.003 -0.89409,-0.003 -0.2981,-6.2e-4 -0.59613,-9.3e-4 -0.89415,-9.3e-4 -160.4321,0.67384 -328.384228,91.24054 -328.384228,129.08065 0,37.98073 194.471018,108.93335 229.037718,136.825 C 211.75955,461.28643 135.33833,504.33496 53.178046,573.87479 18.942376,516.16059 -1.4631037e-6,449.42886 0,380 -2.8609475e-6,244.23908 72.427587,118.79081 190,50.910347 c 117.57241,-67.880463 262.42759,-67.880463 380,0 C 687.57241,118.79081 760,244.23908 760,380 c 0,68.2194 -18.28817,133.83483 -51.40283,190.85047 z"
           inkscape:connector-curvature="0"
           style="fill:#000000;fill-rule:nonzero" />
      </g>
    </g>
  </g>
</svg>""",
# -----------------------------------------------------------------
#
#                           TEAM LABEL
#
# -----------------------------------------------------------------

"team_label":"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="90mm"
   height="29mm"
   viewBox="0 0 90 29"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.3 (2405546, 2018-03-11)"
   sodipodi:docname="TeamLabels.svg">
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="5.6"
     inkscape:cx="104.85939"
     inkscape:cy="73.686811"
     inkscape:document-units="mm"
     inkscape:current-layer="g1046"
     showgrid="true"
     inkscape:window-width="1600"
     inkscape:window-height="837"
     inkscape:window-x="-8"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     showguides="false"
     inkscape:snap-text-baseline="true"
     inkscape:object-nodes="false"
     inkscape:snap-bbox="true"
     inkscape:bbox-nodes="true">
    <sodipodi:guide
       position="-30.201457,-41.694046"
       orientation="0.70710678,0.70710678"
       id="guide1861"
       inkscape:locked="false" />
    <inkscape:grid
       type="xygrid"
       id="grid1863"
       originx="0"
       units="mm"
       spacingx="5"
       spacingy="5" />
  </sodipodi:namedview>
  <defs
     id="defs2" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(0,-268.00001)">
    <g
       transform="matrix(0.264583,0,0,0.264583,6.740765,281.94758)"
       inkscape:label="DataMatrix"
       id="g1046">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:16.00002098px;line-height:125%;font-family:'OCRA';-inkscape-font-specification:'OCRA';text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         x="182.39734"
         y="37.993484"
         id="text1855"><tspan
           sodipodi:role="line"
           id="tspan1853"
           x="182.39734"
           y="37.993484"
           style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:64.00008392px;font-family:'OCRA';-inkscape-font-specification:'OCRA';text-align:center;text-anchor:middle;stroke-width:1.00000131px">{code}</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:16.00002098px;line-height:125%;font-family:sans-serif;-inkscape-font-specification:sans-serif;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         x="182.39734"
         y="-18.699499"
         id="text1859"><tspan
           sodipodi:role="line"
           id="tspan1857"
           x="182.39734"
           y="-18.699499"
           style="text-align:center;text-anchor:middle;stroke-width:1.00000131px">Team</tspan></text>
      <g
         id="Symbol"
         style="fill:none;fill-rule:evenodd;stroke:none;stroke-width:1"
         transform="matrix(0.09946138,0,0,0.09946138,-6.5792776,-37.597162)">
        <path
           id="Combined-Shape"
           d="M 677.02569,617.02111 C 647.86936,653.56793 611.78587,684.96457 570,709.08965 c -117.57241,67.88047 -262.42759,67.88047 -380,0 C 149.36918,685.63144 114.12985,655.29811 85.407993,620.03996 237.45689,462.35413 363.12698,500.77008 363.12698,444.72918 c 0,-58.40687 -216.99267,-96.85099 -216.99267,-137.37364 0,-40.41177 127.88133,-71.09181 236.54807,-71.25942 108.66671,0.16761 236.54802,30.84765 236.54802,71.25942 0,40.52265 -216.99268,78.96677 -216.99268,137.37364 0,55.6804 124.05847,18.11529 274.78795,172.29195 z m 31.57148,-46.17064 C 627.79949,503.08549 552.57476,461.04506 482.92298,444.72918 c 34.56671,-27.89165 229.03772,-98.84427 229.03772,-136.825 0,-37.84011 -167.95212,-128.40681 -328.38423,-129.07691 -0.298,-0.004 -0.59603,-0.003 -0.89409,-0.003 -0.2981,-6.2e-4 -0.59613,-9.3e-4 -0.89415,-9.3e-4 -160.4321,0.67384 -328.384228,91.24054 -328.384228,129.08065 0,37.98073 194.471018,108.93335 229.037718,136.825 C 211.75955,461.28643 135.33833,504.33496 53.178046,573.87479 18.942376,516.16059 -1.4631037e-6,449.42886 0,380 -2.8609475e-6,244.23908 72.427587,118.79081 190,50.910347 c 117.57241,-67.880463 262.42759,-67.880463 380,0 C 687.57241,118.79081 760,244.23908 760,380 c 0,68.2194 -18.28817,133.83483 -51.40283,190.85047 z"
           inkscape:connector-curvature="0"
           style="fill:#000000;fill-rule:nonzero" />
      </g>
    </g>
  </g>
</svg>
""",
# -----------------------------------------------------------------
#
#                       SHORT KIT LABEL
#
# -----------------------------------------------------------------
"short_kit_label":"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="90mm"
   height="29mm"
   viewBox="0 0 90 29"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.2 2405546, 2018-03-11"
   sodipodi:docname="KitLabel_short.svg">
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="3.8365839"
     inkscape:cx="212.80249"
     inkscape:cy="66.28275"
     inkscape:document-units="mm"
     inkscape:current-layer="g1046"
     showgrid="true"
     inkscape:window-width="2560"
     inkscape:window-height="1440"
     inkscape:window-x="0"
     inkscape:window-y="0"
     inkscape:window-maximized="0"
     showguides="false"
     inkscape:snap-text-baseline="true">
    <sodipodi:guide
       position="-30.201457,-41.694046"
       orientation="0.70710678,0.70710678"
       id="guide1861"
       inkscape:locked="false" />
    <inkscape:grid
       type="xygrid"
       id="grid1863"
       originx="0"
       units="mm"
       spacingx="2.5"
       spacingy="2.5" />
  </sodipodi:namedview>
  <defs
     id="defs2" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
 <g transform="translate(3,1.8) scale(0.16,0.16)">
    {bar}
 </g>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(0,-268.00001)">
    <g
       transform="matrix(0.264583,0,0,0.264583,6.740765,281.94758)"
       inkscape:label="DataMatrix"
       id="g1046">
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:16.00002098px;line-height:125%;font-family:'OCRA';-inkscape-font-specification:'OCRA';text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         x="116.25552"
         y="9.6469917"
         id="text1855"><tspan
           sodipodi:role="line"
           id="tspan1853"
           x="116.25552"
           y="9.6469917"
           style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:32.00004196px;font-family:'OCRA';-inkscape-font-specification:'OCRA';text-align:center;text-anchor:middle;stroke-width:1.00000131px">{code}</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:16.00002098px;line-height:125%;font-family:sans-serif;-inkscape-font-specification:sans-serif;text-align:center;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         x="116.25552"
         y="-18.699501"
         id="text1859"><tspan
           sodipodi:role="line"
           id="tspan1857"
           x="116.25552"
           y="-18.699501"
           style="text-align:center;text-anchor:middle;stroke-width:1.00000131px">SR part code</tspan></text>
      <text
         xml:space="preserve"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:16.00002098px;line-height:69.99999881%;font-family:sans-serif;-inkscape-font-specification:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         x="-6.5792861"
         y="32.544659"
         id="text5574"><tspan
           sodipodi:role="line"
           id="tspan5572"
           x="-6.5792861"
           y="32.544659"
           style="font-size:10.66668034px;line-height:69.99999881%;stroke-width:1.00000131px">Property of Student Robotics</tspan><tspan
           sodipodi:role="line"
           x="-6.5792861"
           y="43.744675"
           style="font-size:10.66668034px;line-height:69.99999881%;stroke-width:1.00000131px"
           id="tspan5576">Do not remove or cover this label</tspan></text>
      <path
         style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1.00000131px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
         d="M 201.29501,-47.045993 V 47.442318"
         id="path19"
         inkscape:connector-curvature="0" />
    </g>
  </g>
</svg>"""
}

parser = argparse.ArgumentParser()
parser.add_argument('template', choices=templates.keys(), help="Template to use")
parser.add_argument('codes', metavar='NNNNNNNN', nargs='*', help="list of codes to generate (with or without dashes)")
args = parser.parse_args()

# sanitise codes, so we can support both with and without dashes.
codes =  args.codes
template = templates[args.template]
for code in codes:
    out_file = code+".svg"
    qr = pyqrcode.create(code)
    svg = io.BytesIO()
    qr.svg(svg, scale=4)
    svg_content = svg.getvalue().decode("utf-8")
    svg_content = '\n'.join(svg_content.split('\n')[1:])
    with open(out_file,'w') as o:
        print(template.format(bar=svg_content,code=code),file=o)
