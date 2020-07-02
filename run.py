import dimworks.stat as dw
import pandas as pd

x=pd.Series([0.449,0.412,0.546,0.272,0.486,0.449,0.412,0.546,0.272,0.486])
USL=0.7
LSL=-0.7

pp=dw.get_pp(x,USL,LSL)
ppk=dw.get_ppk(x,USL,LSL)
cp=dw.get_cp(x,USL,LSL,5)
cpk=dw.get_cpk(x,USL,LSL,5)
d2=dw.get_d2(5)



print("pp=",pp," ppk=",ppk," cpk=",cp," cpk=",cpk," d2=",d2)
