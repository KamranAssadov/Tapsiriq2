class isciler():
     def __init__(self,ad,soyad,no,maas):
         self.ad=ad
         self.soyad=soyad
         self.no=no
         self.maas=maas
 
        
     def informasiya_goster(self):
         print("""
             Isci Informasiyasi
              
               Ad:{}
               Soyad:{}
               No:{}
               Maas:{}
               
               """.format(self.ad,self.soyad,self.no,self.maas))
              
 isci1=isciler("Kamran","Asadov",16100004,1600)



 class proqramistler(isciler):
     def informasiya_goster(self):
         print("""
              Proqramistler Informasiyasi
              
               Ad:{}
               Soyad:{}
               No:{}                      
               Maas:{}
               Proqram_bilikleri:{}
               """.format(self.ad,self.soyad,self.no,self.maas,self.proqram_bilikleri))
    
     def proqramBiliyi_artir(self,proqram_dili):
               print("Proqram biliyi artirildi")
               self.proqram_bilikleri+=proqram_dili
        
 proqramist1=proqramistler("Arif","Qurbanov",27091998,4500,"C++,C#,C,Arduino")
 dir(isci1)
 dir(proqramist1)
 proqramistl.proqramBiliyi_artir(1500)
 proqramist1.proqram_bilikleri
     
  class director(isciler):
      def informasiya_goster(self):
          print("""
                Director Informasiyasi
               
                Ad:{}
                Soyad:{}
                No:{}
                Is_muddeti:{}
                
                """.format(self.ad,self.soyad,self.no,self.maas,self.is_muddeti))
                
     def is_muddeti_artir(self,muddet):
         print("Is muddeti artitildi ")
         self.is_muddeti+=muddet
         
 director1=director("Fidan","Taghiyeva",28092000,8)
 dir(isci1)
 dir(director1)
 director1.is_muddeti_artir(3)
 director1.is_muddeti
                
          
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
          