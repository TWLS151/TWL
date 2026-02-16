M,N = map(int,input().split())
I = int(input())
if N*M < I:
    print(0)
else:
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    x,y = 0,0
    dir = 0
    status = [[0]*M for _ in range(N)]
    def move(x,y,dir):
        
        if 0<=x+dx[dir] <N and 0<=y+dy[dir]<M:
            while status[x+dx[dir]][y+dy[dir]] != 0:
                dir = (dir+1)%4
            return x+dx[dir], y+dy[dir],dir
        else:
            dir = (dir+1)%4
            return x+dx[dir], y+dy[dir],dir
    for i in range(I-1):
        status[x][y] = -1
        x,y,dir = move(x,y,dir)
    
    
    print(y+1,x+1)