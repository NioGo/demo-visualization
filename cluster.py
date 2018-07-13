from scipy.cluster.vq import *
from numpy import *
from matplotlib.pylab import *

class1 = 1.5 * randn(100, 2)
class2 = randn(100, 2) + array([5, 5])

features = vstack((class1, class2))

centroids, variance = kmeans(features, 2)
code, dist = vq(features, centroids)

figure()
ndx = where(code == 0)[0]
plot(features[ndx, 0], features[ndx, 1], "b*")
ndx = where(code == 1)[0]
plot(features[ndx, 0], features[ndx, 1], "gs")
plot(centroids[:,0], centroids[:,1], "ro")
axis('off')
show()
