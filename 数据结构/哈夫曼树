#include <iostream>  
#include <vector>  
#include <queue>  

using namespace std;  

// 哈夫曼树的节点结构  
struct Node {  
    int weight;       // 叶子节点的权重  
    Node *left;      // 左子树  
    Node *right;     // 右子树  

    Node(int w) : weight(w), left(nullptr), right(nullptr) {}  
};  

// 自定义比较器，用于优先队列  
struct Compare {  
    bool operator()(Node* a, Node* b) {  
        return a->weight > b->weight; // 按权重升序排列  
    }  
};  

// 计算哈夫曼树的带权路径长度  
int calculateWeightedPathLength(Node* root, int depth) {  
    if (!root)  
        return 0;  
    // 叶子节点的带权路径长度  
    if (!root->left && !root->right)  
        return root->weight * depth;  

    // 在左子树和右子树中递归计算  
    return calculateWeightedPathLength(root->left, depth + 1) +   
           calculateWeightedPathLength(root->right, depth + 1);  
}  

int main() {  
    int n;  
 
    cin >> n;  

    priority_queue<Node*, vector<Node*>, Compare> minHeap;  


    for (int i = 0; i < n; ++i) {  
        int weight;  
        cin >> weight;  
        minHeap.push(new Node(weight)); // 将每个整数作为叶子节点插入优先队列  
    }  

    // 构建哈夫曼树  
    while (minHeap.size() > 1) {  
        Node *left = minHeap.top(); minHeap.pop();  
        Node *right = minHeap.top(); minHeap.pop();  

        // 创建新节点，权重为左右子树的权重之和  
        Node *newNode = new Node(left->weight + right->weight);  
        newNode->left = left;  
        newNode->right = right;  
        
        // 插入到优先队列  
        minHeap.push(newNode);  
    }  

    // 获取哈夫曼树的根节点  
    Node *root = minHeap.top();  
    
    // 计算并输出带权路径长度  
    int weightedPathLength = calculateWeightedPathLength(root, 0);  
    cout <<  weightedPathLength << endl;  
    
    return 0;  
}  
