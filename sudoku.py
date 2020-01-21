
su = [[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]



# 发现下一个“0”的坐标(x,y)
def get_x_y(su):
        for x in range(9):
            for y in range(9):
                    if su[x][y] == 0:
                        return x,y
        else:
            return "done"
# 检查并填入一个数
def fill_num(su,x_y):
    dcan = set()
    for n in su[x_y[0]]:
        dcan.add(n)
    for i in range(9):
        dcan.add(su[i][x_y[1]])
    for x in range(9):
        for y in range(9):
                if get_gong((x,y)) == get_gong(x_y):
                    dcan.add(su[x][y])
    dcan.remove(0)
    can = list({1,2,3,4,5,6,7,8,9}-dcan)
    now_n = su[x_y[0]][x_y[1]]
    for d in range(now_n+1,11):
        if d in can:
            su[x_y[0]][x_y[1]] = d
            print("fill-down",x_y,d)
            print(su)
            return True
        
    else:
        su[x_y[0]][x_y[1]] = 0
        back_set(su,vectors)
        return False

def get_gong(x_y):
      if x_y[0] <= 2:
            if x_y[1] <= 2:
                  return 1
            elif 2 < x_y[1] <= 5:
                  return 2
            elif 5 < x_y[1] <=8:
                  return 3
      elif 2 < x_y[0] <= 5:
            if x_y[1] <= 2:
                  return 4
            elif 2 < x_y[1] <= 5:
                  return 5
            elif 5 < x_y[1] <=8:
                  return 6
      else:
            if x_y[1] <= 2:
                  return 7
            elif 2 < x_y[1] <= 5:
                  return 8
            elif 5 < x_y[1] <=8:
                  return 9

def back_set(su,vectors):
    x_y = get_x_y(su)
    index = vectors.index(x_y)-1
    print("backset-down<<<")
    fill_num(su,vectors[index])


vectors = []
for x in range(9):
      for y in range(9):
            if su[x][y] == 0:
                vectors.append((x,y))

while get_x_y(su) != "done":
    x_y = get_x_y(su)
    if not fill_num(su,x_y):
        print(su)
        back_set(su,vectors)
        
    else:
        print("")
    
print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(su)



            
      


      
      
      

