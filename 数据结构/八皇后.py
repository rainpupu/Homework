#include <iostream>  
#include <vector>  
#include <cmath>
#include <fstream>

using namespace std;

class Queen
{
private:
    int size;
    int donePieces;
    vector<vector<bool>> board;
    vector<bool> columns;
    vector<bool> forwardSlashs;
    vector<bool> backSlashs;
    ofstream outputFile;
    int solutionCount;  // 解决方案计数  
public:
    Queen(int s){
        size = s;
        board.resize(size, vector<bool>(size, false));
        columns.resize(size, false);
        forwardSlashs.resize(size + size - 1,false);
        backSlashs.resize(size + size - 1,false);
        outputFile.open("D:/c++/solutions.txt");
        solutionCount = 0;  // 初始化解决方案计数  
    };

    ~Queen() {  
        if (outputFile.is_open()) {  
            outputFile.close();  // 确保程序结束时关闭文件  
        }  
    }  

    bool isSafe(int row, int column){
        return (!columns[column] && !forwardSlashs[row + column] && !backSlashs[row - column + size - 1]);
    }

     // 将当前棋盘状态写入到文件  
    void printBoard() {  
        for (int row = 0; row < size; row++) {  
            for (int column = 0; column < size; column++) {  
                outputFile << (board[row][column] ? "1 " : "0 "); // 将棋盘打印到文件  
            }  
            outputFile << endl;  
        }  
        outputFile << endl; // 解决方案之间的空行  
    }  

    void writeSolutionCount() {  
        outputFile << "总解决方案数量: " << solutionCount << endl;  
    } 

    void playQueen(int row){
        if(row == size){
            printBoard();
            solutionCount++;  // 递增解决方案计数 
            return;
        }

        for(int column = 0; column < size; column++){
            if(isSafe(row, column)){
                board[row][column] = true;
                columns[column] = true;
                forwardSlashs[row + column] = true;
                backSlashs[row - column + size - 1 ] = true;

                playQueen(row + 1);  // 递归到下一行

                board[row][column] = false;
                columns[column] = false;
                forwardSlashs[row + column] = false;
                backSlashs[row- column + size - 1 ] = false;
                
            }    
        }
    }
};

int main(){
    Queen queen(8);
    queen.playQueen(0);
    queen.writeSolutionCount(); 
    return 0;
}

