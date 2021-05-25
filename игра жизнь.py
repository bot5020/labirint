from tkinter import *
import random
red = "#ad7474"

def krac(a,b):
    main[a-2][b]["bg"] = red
    main[a][b-2]["bg"] = red
    main[a+2][b]["bg"] = red
    main[a][b+2]["bg"] = red
    

n = 30
m = 30
#entries = [[False if random.randint(0, 1) == 0 else True for col in range(m)] for row in range(n)]
root = Tk()
root.resizable(width = False, height = False)
root.title("Жизнь")

a = random.randrange(n)
#a = 29
b = random.randrange(m)
#b = 29
main = [[None for col in range(m)] for row in range(n)]
for row in range(n):
	for col in range(m):
		e = Button(width = 2, height = 1, state = DISABLED, font = "Verdana 6", bg="#A9A9A9")
		e.grid(row = row, column = col)
		main[row][col] = e
main[a][b]["bg"] = "#ffffff"
krac(a,b)

