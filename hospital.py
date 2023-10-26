class Hospital:
    def __init__(self):
        self.chip={}

    def add_pateint(self,pateint_id,name,doj,problem,treating_doctor):
        self.chip[pateint_id]=[pateint_id,name,doj,problem,treating_doctor]
        
    def get_pateint(self):
        print(self.chip)
    def search_filter(self,input):
        self.input= input
        for i in self.chip:
            for j in self.chip[i]:
                if(j==self.input):
                    print(self.chip[i])

    def del_pateint(self,id):
        del self.chip[id]
        print(self.chip)
                

    def update_pateint(self,id):
        self.id= id
        for i in self.chip:
            for j in self.chip[i]:
                if(j==self.id):
                    
                    self.chip.update({1:[1,"ashok","22-11-2022","cold","balu"]})
                    print(self.chip)
            
    
        
    

h=Hospital()
h.add_pateint(1,"balu","12-2-2021","checkup","ashok")
h.get_pateint()
h.search_filter(1)
h.del_pateint(1)
h.update_pateint(1)
