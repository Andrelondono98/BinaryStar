from __future__ import division
from visual import *
from visual.graph import *

scene = display(width = 800, height = 800)
scene.autoscale =0
scene.range=7e11

#Create objects to be modeled/ define geometric attributes
star1 = sphere(radius = 7e9,color = color.white, pos=vector(1.5e11,0,0) )
star2 = sphere(radius = 7e10, color = color.blue,pos=vector(-1.5e11,0,0))

#mywindow1 = gdisplay(xtitle = 'time(s)',ytitle = 'Energy (J)', title = 'Total energy of star 1')
#f1 = gcurve(gdisplay = mywindow1, color = color.cyan)
#f2 = gcurve(gdisplay = mywindow1, color = color.red)

#Define physical attributes of objects
G = 6.7e-11
star1.m = 2.0e30
star2.m = 10.0e30
#star2.m = 2.0e30

#Specify initial conditions
star1.p = star1.m*vector(0, 5e4,0)
#star1.p = star1.m*vector(0, 5e3, 0)
star2.p= -star1.p
planet1 = sphere(pos = (-300, 10, 0), radius = 30, color = color.red, make_trail=true)

star2.Fnet = vector(0,0,0) 
star1.Fnet = vector(0,0,0)

#Visualize momentum/force vectors with arrows
#Determine scale through approximation of magnitude of vector to scale arrow into scene
scale = 2e10/1e27
star1.FnetVector= arrow(pos = star1.pos, axis = star1.Fnet*scale, color = color.white)
star2.FnetVector = arrow(pos = star2.pos, axis = star2.Fnet*scale, color = color.blue)


momentumScale = 2e11/star1.p.mag
star1.momentumVector = arrow(pos = star1.pos, axis = star1.p*momentumScale, color = color.white)
star2.momentumVector = arrow(pos = star2.pos, axis = star2.p*momentumScale, color = color.blue)

trail1 = curve(color = star1.color)
trail2 = curve(color = star2.color)


t = 0
dt = 1.0e5

while true:
    rate(100)
    
    dvector = star1.pos-star2.pos
    dmagnitude = mag(dvector)
    dDir = dvector/dmagnitude

    #calculate gravitational force between stars
    Fgrav1 = G*star1.m*star2.m / dmagnitude**2.0
    star2.Fnet = Fgrav1*dDir
    star1.Fnet = -star2.Fnet

    #update momentum/position
    star2.p = star2.p + star2.Fnet*dt
    star2.pos = star2.pos+star2.p/star2.m*dt
    star1.p = star1.p + star1.Fnet*dt
    star1.pos = star1.pos+star1.p/star1.m*dt

    #append positions to curve object
    trail1.append(pos = star1.pos)
    trail2.append(pos = star2.pos)
    
    star1.momentumVector.pos=star1.pos
    star1.momentumVector.axis=star1.p*momentumScale
    star2.momentumVector.pos=star2.pos
    star2.momentumVector.axis=star2.p*momentumScale
	
    star1.FnetVector.pos=star1.pos
    star1.FnetVector.axis=star1.Fnet*scale
    star2.FnetVector.pos=star2.pos
    star2.FnetVector.axis=star2.Fnet*scale
	


    t = t+dt

    #graphs
 #   star1KE = .5*star1.m*mag(star1.p)**2
 #   star1GPE = G*(star2.m*star1.m)/(mag(star2.pos-earth.pos)

    #t = t + dt
   # f1.plot(pos = (t, star1KE))
 #   f2.plot(pos = (t, star1GPE))
 

