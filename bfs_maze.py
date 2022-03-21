import queue

def createMaze():
    maze = []
    maze.append([&quot;#&quot;,&quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;O&quot;,&quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot; &quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;,&quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;,&quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;,&quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot; &quot;,&quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot; &quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;,&quot;#&quot;])
    maze.append([&quot;#&quot;,&quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;X&quot;,&quot;#&quot;])
    return maze
def createMaze2():
    maze = []
    maze.append([&quot;#&quot;,&quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;O&quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot;#&quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;, &quot; &quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;])
    maze.append([&quot;#&quot;,&quot; &quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot; &quot;, &quot;#&quot;])
    maze.append([&quot;#&quot;,&quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;#&quot;, &quot;X&quot;, &quot;#&quot;])
    return maze

def printMaze(maze, path=&quot;&quot;):
    for x, pos in enumerate(maze[0]):
        if pos == &quot;O&quot;:
            start = x
    i = start
    j = 0
    pos = set()
    for move in path:

        if move == &quot;L&quot;:
            i -= 1
        elif move == &quot;R&quot;:
            i += 1
        elif move == &quot;U&quot;:
            j -= 1
        elif move == &quot;D&quot;:
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print(&quot;+ &quot;, end=&quot;&quot;)
            else:
                print(col + &quot; &quot;, end=&quot;&quot;)
        print()
        

def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == &quot;O&quot;:
            start = x
    i = start
    j = 0
    for move in moves:
        if move == &quot;L&quot;:
            i -= 1
        elif move == &quot;R&quot;:
            i += 1
        elif move == &quot;U&quot;:
            j -= 1
        elif move == &quot;D&quot;:
            j += 1
        if not(0 &lt;= i &lt; len(maze[0]) and 0 &lt;= j &lt; len(maze)):
            return False
        elif (maze[j][i] == &quot;#&quot;):
            return False
    return True

def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == &quot;O&quot;:
            start = x
    i = start
    j = 0
    for move in moves:
        if move == &quot;L&quot;:
            i -= 1
        elif move == &quot;R&quot;:
            i += 1
        elif move == &quot;U&quot;:
            j -= 1
        elif move == &quot;D&quot;:
            j += 1
    if maze[j][i] == &quot;X&quot;:
        print(&quot;Found: &quot; + moves)
        printMaze(maze, moves)
        return True
    return False

nums = queue.Queue()
nums.put(&quot;&quot;)
add = &quot;&quot;
maze  = createMaze2()
while not findEnd(maze, add): 
    add = nums.get()
    for j in [&quot;L&quot;, &quot;R&quot;, &quot;U&quot;, &quot;D&quot;]:
        put = add + j
        if valid(maze, put):
            nums.put(put)
