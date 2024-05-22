

# pythonda fonksiyon ve döngüler kullanılarak işlemleri
# işlemleri gerçekleştiren program

#Liste oluşturma

import math

def euclideanDistance(tuple1, tuple2):
    """
    İki tuple alır ve bu iki tuple arasındaki öklid mesafesini döndürür.
    """
    x1, y1 = tuple1[0], tuple1[1]
    x2, y2 = tuple2[0], tuple2[1]
    
    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    sonuc = math.sqrt(d)
    
    return sonuc

points = [(10, 15)]
points2 = [(20, 25)]
print(euclideanDistance(points[0], points2[0]))

