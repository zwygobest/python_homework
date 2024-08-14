import matplotlib.pyplot as plt
import math
log_p = []
log_q = []

# prepare q and p dates
q = [50,100,200,300,500,750,1000]
p = [2.75,3.5,4.45,5.15,6.15,7.1,7.85]

# calculate q and p
for i in q:
    log_q.append(math.log(i))
for i in p:
    log_p.append(math.log(i))

# only draw the dots,(q,p)
plt.plot(q,p,marker='o', linestyle='none')

plt.title("(q,p)")
plt.xlabel("q")
plt.ylabel("p")
plt.show()

#draw (q,log_p)
plt.plot(q,log_p,marker='o', linestyle='none')

plt.title("(q,log_p)")
plt.xlabel("q")
plt.ylabel("lop_p")
plt.show()
#
# draw (log_q,p)
plt.plot(log_q,p,marker='o', linestyle='none')

plt.title("(log_q,p)")
plt.xlabel("log_q")
plt.ylabel("p")
plt.show()
#
#draw(log_q,log_p)
plt.plot(log_q,log_p,marker='o', linestyle='none')

plt.title("(log_q,log_p)")
plt.xlabel("log_q")
plt.ylabel("log_p")
plt.show()

# for i , j in zip(log_q,log_p):
#     print("log(q) = {},log(p) = {}".format(i,j))
