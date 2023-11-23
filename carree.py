class carrer:
    
    stocks={}
    class admin():
        def __init__(self):
            self.mind={}
        def create_job(self,role,empid,descrition,salary,location,experience,hr):
            self.mind[empid]=[role,empid,descrition,salary,location,experience,hr]
            print(self.mind)
        def delete_job(self,id):
            del self.mind[id]
            print(self.mind)
        def total_app(self):
            print(carrer.stocks)
        def update_job(self,id,input):
            self.id=id
            for i in self.mind:
                for j in self.mind[i]:
                    if(j==self.id):
                        self.mind.update(input)
                        print(self.mind)

    
    class user(admin):
        
        def total_jobs(self):
            
            print(self.mind)
        def apply_job(self,name,dob,gender,mobile,email,skills,resume):
            carrer.stocks[mobile]=[name,dob,gender,mobile,email,skills,resume]

    
c=carrer()
a=c.admin()
a.create_job("python dev",101,"team player",100000,"hyderabad",2,"ashu")

#l={101:["python dev",101,"team player",100000,"hyderabad",3,"ashu"]}
#a.update_job(101,l)

#a.delete_job(101)
u=c.user()
u.apply_job("balu","11-2-2000","male",9381100847,"balu@gmail.com","python","balu.pdf")
a.total_app()
u.total_jobs()
         

