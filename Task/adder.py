import os
import re

def mergefiles(file_list,output_file):
      
      f_out = file(output_file,'w')
      sum_value = 0

      for f in file_list:
            
            f_in = file(f)
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", f_in.read())
            sum_value += int(numbers[0])
            print(int(numbers[0]))
            f_in.close()
      
      f_out.write(str(sum_value))
      f_out.flush()
      f_out.close()

      return True