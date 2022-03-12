import ctypes 

class MyIntArray(object): 
	def __init__(self): 
		self.n = 0  
		self.capacity = 10 
		self.A = self.make_array(self.capacity) 
		
	def __len__(self): 
		return self.n 
	
	def getSize(self):
	    return self.n
	
	def get(self, k): 
		if not 0 <= k <self.n: 
			return IndexError('K is out of bounds !') 
		
		return self.A[k]
		
	
	def set(self, k, x): 
		if not 0 <= k <self.n: 
			# Check it k index is in bounds of array 
			return IndexError('K is out of bounds !') 
		
		self.A[k] = x
		
	def pushBack(self, ele): 
		if self.n == self.capacity: 
			# Double capacity if not enough room 
			self._increaseCapacity(2 * self.capacity) 
		
		self.A[self.n] = ele # Set self.n index to element 
		self.n += 1

		
	def popBack(self): 
		if self.n==0: 
			print("Array is empty deletion not Possible") 
			return
		
		self.A[self.n - 1]=0
		self.n -= 1
		
	def _increaseCapacity(self, new_cap): 
		B = self.make_array(new_cap)  
		
		for k in range(self.n):  
			B[k] = self.A[k] 
			
		self.A = B 
		self.capacity = new_cap 
		
	def make_array(self, new_cap): 
		return (new_cap * ctypes.py_object)() 

def main():
    print("Hello!")
    # a = MyIntArray()
    # a.pushBack(5)
    # print(a.getSize())
    
if __name__ == '__main__':
    main()
