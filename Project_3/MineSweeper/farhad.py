import sys
from random import *
from pygame import *
init()

########################################################################

class Cell(Rect):
	"defining a cell object for each element of matrix"
	def __init__(self,rect):
		
		Rect.__init__(self, rect)
		self.value = 0
		self.flag = False
		self.disp = False
		self.bomb = False

	def uncover(self):
		j = 0
		if self.bomb == True:
			self.disp = True
			screen.blit(ubomb,self)
			j += 1
			display.update()
			return False
			
		elif 0 < self.value < 9:
			self.disp = True
			screen.blit(numbers[self.value],self)		
			j += 1
		
		elif (self.value == 0 and self.bomb == False):

			screen.blit(numbers[self.value],self)				
			self.disp = True
			j += 1
			display.update()
			time.wait(100)

			source = self.neighbour_check()
			#j += self.neighbour_check()[1]
			#print j
			for item in source:
				if item.value == 0:
					source.extend(item.neighbour_check())
					#j += item.neighbour_check()[1]
		display.update()
		
		#return j
			
	def neighbour_check(self):
		
		j = 0
		List = []
		Neighbours = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
		a = (self.centerx)/30
		b = (self.centery)/30
		for (m,n) in Neighbours:
			if 0<=a+m<x and 0<=b+n<y:
				if cells[a+m][b+n].disp == False:
					if 0 <= cells[a+m][b+n].value < 9:
						if cells[a+m][b+n].bomb == False:
							obj = cells[a+m][b+n]
							screen.blit(numbers[obj.value],obj)	
							obj.disp = True
		#					j += 1
							
							display.update()
							
							if obj.value == 0:
								List.append(obj)
							
		return List#,j

######################################### defining display by X x Y cell

x = 30									
y = 20									
screen = display.set_mode((x*30,y*30)) 	# >> Surface


def  MinesNumber(s):

    if s == 'easy':
        return 0.1*x*y
    elif s == 'medium':
        return 0.2*x*y
    elif s == 'hard':
        return 0.3*x*y

######################################## Importing images which are used

numbers = []
for num in range(9):
	name = str('%d.jpg' % num)
	pic	= image.load(name)
	numbers.append(pic)  				# >> surface
	#numbers.append(Surface((30,30)).blit(pic, (0,0), (0,0,30,30))) #>> Rect

#cover = Surface((30,30)).blit(image.load('cover.jpg'), (0,0), (0,0,30,30)) 
cover = image.load('cover.jpg')
flag = image.load('flag.jpg')
bomb = image.load('bomb.jpg')
ubomb = image.load('ubomb.jpg')

############################################ Main Program (infinit loop)

while True:

#	level = raw_input("choose level of difficulty as easy, medium and hard:")
	mines = int(MinesNumber('easy'))
	time0 = time.get_ticks()
	time.set_timer(USEREVENT,1000)
	cells = []          # >> draw initial screen blitting cover to each cell and creating a list of list of Cell objects which their type is Rect
	for a in range(x):
		column = []
		for b in range(y):
			column.append(Cell(screen.blit(cover, (30*a,30*b))))
		cells.append(column)
	

	MinePos = []				# assigning random places for mines, change the
	i = 0						# value of object rect.bomb to true
	while i < mines:
		xm = randint(0,x-1)
		ym = randint(0,y-1)
		if (xm,ym) not in MinePos:
			MinePos.append((xm,ym))
			cells[xm][ym].bomb = True
			i+=1
			
	Neighbours = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
	for (X,Y) in MinePos:
		for (a,b) in Neighbours:
			if 0<=X+a<x and 0<=Y+b<y:
				if cells[X+a][Y+b].bomb == False:
					if cells[X+a][Y+b].value < 9:
						cells[X+a][Y+b].value += 1

	
	display.update()
	remain = x*y - mines
	
	while remain:

		move = event.wait() ##
		#time.set_timer(USEREVENT,1000)
		if move.type == USEREVENT:
			dt = (time.get_ticks() - time0)/1000
			sec = str(dt%60)
			min = str(dt/60)
			
			
			r = 0
			for i in range(len(cells)):
				for j in range(len(cells[0])):
					if cells[i][j].disp == False:
						r +=1
			remain = r - mines
			
			
			title = "%s:%s	Remaining %d Cells" % (min,sec,remain)
			display.set_caption(title)
			

		elif move.type == MOUSEBUTTONUP:
			
			(a0,b0) = mouse.get_pos()
			(a,b) = (a0/30,b0/30)

			if cells[a][b].disp == False:
				if move.button == 1: #and cells[a][b].flag == False:
					cells[a][b].uncover() # i = 
		#			remain -= i
					if cells[a][b].uncover() == False:
						break
						
						
						
				elif move.button == 3:
					if cells[a][b].flag == False:
					 	cells[a][b].flag = True
						display.update(screen.blit(flag, cells[a][b]))
					else:
						cells[a][b].flag = False
						display.update(screen.blit(cover, cells[a][b]))
		
		if move.type == QUIT:
			quit()
			sys.exit()
					
	for (m,n) in MinePos:
		if (m,n) != (a,b):
			display.update(screen.blit(bomb, cells[m][n]))
		else:
			display.update(screen.blit(ubomb, cells[m][n]))
			
	move = event.wait()
	while not key.get_pressed()[K_SPACE]:
		if event.wait().type == QUIT: exit()
					
########################################################################					
					
						
				

	
	

