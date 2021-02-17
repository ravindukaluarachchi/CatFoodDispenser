from math import sqrt

from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import pandas as pd
import matplotlib.pyplot as plt

a=[(0.53, 0.56, 0.53), (0.3, 0.32, 0.3), (0.79, 0.81, 0.78)]

b=[(0.79, 0.8, 0.78), (0.52, 0.55, 0.52), (0.29, 0.32, 0.29)]

def compare(list1, list2):
    distances = []
    for x in list1:
        for y in list2:
            distance = getDistance(x, y)
            distances.append(distance)   
            '''print('(Start)comparing---------------')
            print(x)
            print(y)
            print(distance)
            print('(End)-------------------------')'''
    distances.sort(reverse=False)
    distances = distances[:3]
    '''print('distances---------------')
    print(distances)'''
    avg = sum(distances) / 3
    print('avg : ' + str(avg))
    if avg < 0.1:
        return True
    else:
        return False
    

def getDistance(color1, color2):
    distance = pow(color1[0] - color2[0], 2) + \
               pow(color1[1] - color2[1], 2) + \
               pow(color1[2] - color2[2], 2)
    distance = sqrt(distance)
    return distance

#compare(a,b)    
def detectColorFeatures(image):
    r = []
    g = []
    b = []
    for row in image:
    
        for temp_r, temp_g, temp_b in row:
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
    
    df = pd.DataFrame({'red' : r,
                              'green' : g,
                              'blue' : b})
    
    df['scaled_color_red'] = whiten(df['red'])
    df['scaled_color_blue'] = whiten(df['blue'])
    df['scaled_color_green'] = whiten(df['green'])
    
    cluster_centers, _ = kmeans(df[['scaled_color_red',
                                           'scaled_color_blue',
                                           'scaled_color_green']], 3)
    
    dominant_colors = []
    
    red_std, green_std, blue_std = df[['red','green','blue']].std()
    
    for cluster_center in cluster_centers:
        red_scaled, green_scaled, blue_scaled = cluster_center
        dominant_colors.append((
            round(red_scaled * red_std / 255, 2),
            round(green_scaled * green_std / 255, 2),
            round(blue_scaled * blue_std / 255, 2)
        ))
    print('dominant colors')
    print(dominant_colors)
    #plt.imshow([dominant_colors])
    #plt.show()
    return dominant_colors