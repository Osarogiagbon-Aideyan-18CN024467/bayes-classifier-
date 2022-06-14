loc_D=float(input('Enter the dolomite mean value'))
scale_D=float(input('Enter the dolomite SD value'))
loc_S=float(input('Enther the shale mean value'))
scale_S=float(input('Enter the shale SD value'))
count_D=float(input('Enter count value for dolomite'))
count_S=float(input('Enter count value for shale'))
count_total=count_D + count_S
p_D=count_D / count_total
p_S=count_S  / count_total

#p_gamma_D = p(gamma>60|D)
#p_gamma_S = p(gamma>60|S)
#p_D_gamma_60= p(D|gamma>60)

import scipy.stats
p_gamma_D=1-scipy.stats.norm(loc_D , scale_D).cdf(0.5)
p_gamma_S=1-scipy.stats.norm(loc_S , scale_S).cdf(0.5)
p_D_gamma_60= p_D* p_gamma_D / p_D* p_gamma_D + p_S * p_gamma_S


if p_D_gamma_60>=0.5:
    print('The interval is Dolomite')
    print('It is a Pay Zone Reservoir')
else:
    print('It is a shale interval')
    print('It is a Non-pay Zone Reservoir')
print('Reservoir formation known')
