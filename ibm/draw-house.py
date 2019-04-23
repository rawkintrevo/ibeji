



humidity = 0.4
temp = 70.2
light_color = "0c0" # off is "030"


f = open('/home/rawkintrevo/gits/ibeji/ibm/examples/data/Floor_Plan.svg', 'r')
svg_str = f.read()


tmeter = { 'x' : 400, 'y' : 500 }
hmeter = { 'x' : 400, 'y' : 480 }
hvacstatus = {'x' : 400, 'y' : 520 }


gauges = {
    "css" : """
        .dot {
    width:25px;
height:25px;
background-color: #%s; 
border-radius: 50%%;
}

#tmeter {
left:%ipx;
top:%ipx;
}

#hmeter {
left:%ipx;
top:%ipx;
}

#hvacstatus {
left:%ipx;
top:%ipx;
}"
        
}""",
    "html" : """
    <div id="hmeter" class="element">humidity<meter value=%.2f></meter></div>
        <div id="tmeter" class="element">temperat<meter min=50 max= 90 value=%.1f></meter></div>
        <div id="hvacstatus" class="element dot">HVAC Status</div>"""
}

css_str = gauges['css'] % (light_color,
                            tmeter['x'], tmeter['y'],
                            hmeter['x'], hmeter['y'],
                            hvacstatus['x'], hvacstatus['y'])
html_str = gauges['html'] % (humidity, temp)


html = """
<html>
  <head>
    <style>
* {
  padding:0px;
  margin:0px;
}

.container {
  position: relative;
  box-shadow: inset 0 0 0 5px #add;
}

html, body {
  width: 100%%;
  height: 100%%;
}

.overlay {
  position: absolute;
  background: rgba(100,100,100,0);
  top:0px;
  bottom:0px;
  left:0px;
  right:0px;
}

.element {
  background: #fff;
  position: absolute;
  opacity: .7;
}

%s
  </style>
</head>
<body>
    %s
    <div class="overlay">
        
    </div>
</body>
</html>
""" % (css_str,
       svg_str,
       html_str)

with open('webpage.html', 'w') as f:
    f.write(html)