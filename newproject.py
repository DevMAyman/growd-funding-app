 
import json
with open('users.json', "w") as file:
            json.dumps({
                    
                    'name':'Ayman'
            }, file ,indent=4, separators=(',', ': '))
        