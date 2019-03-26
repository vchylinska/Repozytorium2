def setup():
    size(600,600)
    frameRate(60)
    background(255)
    textSize(100)
    fill(0, 25, 100)
    
    textAlign(CENTER)
    background(255)
    
def draw():

    if keyPressed:
        if (key == 'm' or keyCode == 37):
            background(0)
            textSize(200)
            fill(0, 25, 100)
            text("M", width/2-100, height/2)
            textSize(150)
            fill(10, 20, 70)
            text("CH", width/2+100, height/2)
    if keyPressed:
        if (key == 'c' or keyCode == 39):
            background(150)
            textSize(200)
            fill(0, 100, 150)
            text("CH", width/2+100, height/2)
            textSize(150)
            fill(0, 15, 125)
            text("M", width/2-100, height/2)

                    
    sh = createShape()
    sh.beginShape()
    sh.fill(0, 150, 200)
    sh.noStroke()
    sh.vertex(100, 500)
    sh.vertex(100, 300)
    sh.vertex(350, 400)
    sh.vertex(600, 500)
    sh.endShape(CLOSE)
    shape(sh, 0, 0)
