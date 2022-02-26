from PIL import Image

with open("/home/stryck3r/Téléchargements/MHSCTF/reconstruction.txt","r") as data:
	img_line=data.readline().split(";")
	
every_lines=[]
for pixl in img_line:
	liste=pixl.split(",")
	every_lines.append(liste)

img=Image.new("RGB",(970,970))
px=img.load()

for i in range(len(every_lines)):
		for j in range(0,len(every_lines[1]),3):
			px[i,j/3]=int(every_lines[i][j]),int(every_lines[i][j+1]),int(every_lines[i][j+2])
img.save("/home/stryck3r/Téléchargements/MHSCTF/reconstruction.png","PNG")
	
