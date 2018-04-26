from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	mc = Minecraft.create("127.0.0.1", 4711)  
	return mc

def main():
	mc = init()
	x, y, z = mc.player.getPos()  
	mc.postToChat("Osiris Has Arrived")
	mc = init()
	mc.setBlocks(+164, +64, +164, -164, 0, -164, block.AIR.id) 
	mc.setBlocks(+164, +5, +164, -164, -5, -164, block.SAND.id) 
	x, y, z = mc.player.getPos()
	for i in range(64):
		mc.setBlocks(x+i, y-i,z +i, x-i, y-i, z-i, block.SANDSTONE.id) 
		if i != 0:
			mc.setBlocks(x+i-1,y-i,z+i-1,x-i+1,y-i,z-i+1, block.AIR.id)
	while(mc.getBlock(x,y,z)==block.SANDSTONE.id):
		sleep(1)
	mc.postToChat("Osiris Has Deemed You Unworthy!")
	sleep(1)
	mc.setBlocks(-164, -64, -164, 164, 64, 164, 46, 1)
	mc.setBlocks(-164, 0, -164, 164, 10, 164, 46, 1)
	mc.setBlocks(-164, 10, -164, 164, 64, 164, 10, 1)
main()
