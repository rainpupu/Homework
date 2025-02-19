#include <iostream>  
#include <stack>  
#include <vector>

using namespace std;  

// 定义方向，右、下、左、上  
const int DIRECTIONS[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};  

// 用于存储坐标  
struct Point {  
    int x, y; // 行和列  
};  

// 判断坐标是否合法且为通路  
Point getNextPoint(int x, int y, int m, int n, const vector<vector<int>> &maze, vector<vector<bool>>& visited){
    Point newpoint;
    for(int i = 0; i < 4; i++){
        newpoint.x = x + DIRECTIONS[i][0];
        newpoint.y = y + DIRECTIONS[i][1];
        if(newpoint.x >= 0 && newpoint.x < m &&         
           newpoint.y >= 0 && newpoint.y < n &&  
           maze[newpoint.x][newpoint.y] == 0 && !visited[newpoint.x][newpoint.y])
         return newpoint;
    }
    newpoint.x = -1;
    newpoint.y = -1;
    return newpoint;
}

// 使用栈解决迷宫  
bool solveMazeUsingStack(int m, int n, const vector<vector<int>> & maze, stack<Point> &s) {  

    vector<vector<bool>> visited(m, vector<bool>(n, false));   
    s.push({0, 0}); // 从入口位置推入栈  

    while (!s.empty()) {  
        Point current = s.top();  
        int X = current.x;
        int Y = current.y;

        // 如果到达出口  
        if (X == m - 1 && Y == n - 1) {    
            return true;  
        }  

        //如果没达到出口
        current = getNextPoint(X, Y, m, n, maze, visited);
        if(current.x == -1){
            s.pop();
            continue;
        }
        s.push(current);
        visited[current.x][current.y] = true;
    }  
    return false; // 没有找到路径  
}  

int main() {  
    int m, n;  
    cout << "输入迷宫的行数和列数 (m n): ";  
    cin >> m >> n;  

    vector<vector<int>> maze(m, vector<int>(n));  
    bool istrue = false;
    while(!istrue){
        cout << "输入迷宫的布局（0表示通路，1表示障碍,横向输入且保证（1，1）为入口、5（m，n）为出口）:\n";  
        for (int i = 0; i < m; ++i) {  
            for (int j = 0; j < n; ++j) {  
                cin >> maze[i][j];  
            }  
        }   
        if(maze[0][0] != 0){
            cout << "入口不对请重新输入迷宫" <<endl;
        }
        else if(maze[m-1][n-1] != 0){
            cout << "出口不对请重新输入迷宫" <<endl;
        }
        else istrue = true;
    }
    
    stack<Point> s;

    if (solveMazeUsingStack(m, n, maze, s)) {  
        stack<Point> path;

        while(!s.empty()){
            path.push(s.top());
            s.pop();
        }
        
        cout << "找到从入口到出口的路径:\n";  
        while (!path.empty()) {
			cout<< "(" << (path.top().x)+1 << "," << (path.top().y)+1 <<") ";
			path.pop();
		}
    } else {  
        cout << "没有通路达到出口。\n";  
    }  

    return 0;  
}  
