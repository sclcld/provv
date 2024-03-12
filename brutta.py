

class claudioArray:

    
    def __init__(self, array):

        self.data = array
        
    def __repr__(self):    
        
        final = []
        
        for index,row in enumerate(self.data):

            rep = f'{"array:" if index == 0 else "      "}[{",".join([str(col) for col in row])}]\n'
            
            final.append(rep)

        return "".join(final)
       
    def __hash__(self):
       
        return hash(tuple(tuple(row) for row in self.data))
    
    def __eq__(self, other):
        
        return self.data == other.data
    
    def __add__(self,num):

        return [[col + num for col in row] for row in self.data]            
    
    def max(self):

        numbers = [num for row in self.data for num in row]

        max = 0

        for x in numbers:

            if x > max:

                max = x
        
        return max

             
            
            

b = claudioArray([[6,8,10],[4,6,8],[8,9,0]])

print(b+2)


