todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]
valor1=(max(max(todos[:1])))
valor2=(max(max(todos[:2])))
valor3=(max(max(todos[:3])))
valor4=(max(max(todos[:4])))



if valor1>valor2 & valor1>valor3 & valor1>valor4:
	print("El valor mas grande se ecuentra en el primer grupo")
else:
	if valor2>valor1 & valor2>valor3 & valor2>valor4 :
		print("El valor mas grande se encuentra en el segundo grupo")	
	else:
	    if valor3>valor1 & valor3>valor2 & valor3>valor4:
	    		print("El valor mas grande se encuentra en el tercero grupo")	
	    else:
	            print("El valor mas grande se encuentra en el cuarto grupo")		