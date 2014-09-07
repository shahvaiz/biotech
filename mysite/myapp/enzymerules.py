class Trypsin:

    def __init__(self, seq):
        self.seq = seq
               
    def rules (self):
        CutPoints =[]     
        length = len(self.seq)

        for x in range (0,length-1):        
            if (self.seq[x]=='K' or self.seq[x]=='R') and self.seq[x+1] != 'P':
                CutPoints.append(x+1)
        return CutPoints

class Lyscene:

    def __init__(self, seq):
        self.seq = seq
               
    def rules (self):
        CutPoints =[]   
        length = len(self.seq)
        
        for x in range (0,length-1):
            if (self.seq[x]=='K'):
                CutPoints.append(x+1)
        
        return CutPoints
		
		
class Gluc:

    def __init__(self, seq):
        self.seq = seq
               
    def rules (self):
        CutPoints =[]
        length = len(self.seq)
        
        for x in range (0,length-1):
            if (self.seq[x]=='E' and self.seq[x+1] != 'P' and self.seq[x+1] != 'E'):
                CutPoints.append(x+1)
        
        return CutPoints
    

