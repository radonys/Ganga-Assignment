import os
import re

def mergefiles(file_list,output_file):

      try:
            sum_value = 0

            for f in file_list:

                  with open(f) as f_in:
                  	
                  	numbers = re.findall(r"[-+]?\d*\.\d+|\d+", f_in.read())
                  	sum_value += int(numbers[0])
                  	#print(int(numbers[0]))

            with open(output_file,'w') as f_out:
            	f_out.write(str(sum_value))

            return True

        except:
              return False
