#----------------the inputes------------------


x = int(input ('enter the number:  '))

print('')

u = input ('enter the measuring unit: ')

print('')

c = input('enter the unit that you want to convert into: ')

#--------------convert into kg or gm ------------
if u == 'gm' and c == 'kg' :
	print(x/ 1000 , 'kg')
	
if u =='kg' and c== 'gm' :
	print(x*1000,'gm')

#---------------convert into metre or cm-------			
if u =='metre' and c == 'cm' :
	print(x*100,'cm')
	
if u =='cm' and c == 'metre' :
	print(x/100,'metre')
	
			
					
#----------------if there is an error--------------	

					