x=[]
y=[]
x_average=0
y_average=0
def meanx(x):
    x_sum=0
    for i in range(len(x)):
        x_sum+=x[i]
    x_mean=x_sum/len(x)
    return x_mean
def meany(y):
    y_sum=0
    for i in range(len(y)):
        y_sum+=y[i]
    y_mean=y_sum/len(y)
    return y_mean
def jisuan(x,y,xm,ym):
    i=0
    number_sum=0
    xs=0
    while i<len(x):
        number_sum+=x[i]*y[i]
        xs=xs+x[i]**2
        i+=1
    number_sum=number_sum-(xm*ym*len(x))
    xs=xs-(xm**2*len(x))
    b=number_sum/xs
    a=ym-b*xm
    return a,b
def cc(a,b,x,y):
    temp=[]
    for i in range(len(x)):
        y2=b*x[i]+a
        temp_number=y[i]-y2
        temp.append(temp_number)
    return temp
while True:
    x_temp=input('X值输入，输入Q或者q退出')
    if x_temp=='Q' or x_temp=='q':
        break 
    y_temp=input('Y值输入，输入Q或者q退出')
    if y_temp=='Q' or y_temp=='q':
        break
    judge=False
    x.append(float(x_temp))
    y.append(float(y_temp))
x_average=meanx(x)
y_average=meany(y)
print('X的平均值是'+str(x_average)+'Y的平均值是'+str(y_average))
a,b=jisuan(x,y,x_average,y_average)
print('y='+str(b)+'x+'+str(a))
cancha=cc(a,b,x,y)
for i in range(len(cancha)):
    print (cancha[i])