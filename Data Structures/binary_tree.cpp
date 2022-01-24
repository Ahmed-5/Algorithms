#include <iostream>
using namespace std;

struct node
{
    int value;
    node *left = nullptr, *right = nullptr, *parent = nullptr;
};

class BST{
    public:
        node *root = nullptr;

    void add_node(int value){
        node *new_node = new node{value = value};
        new_node->value = value;
        if(this->root == nullptr){
            this->root = new_node;
        }else{
            node *current = this->root, *parent = nullptr;
            while (current != nullptr){
                parent = current;
                if (value > current->value){
                    current = current->right;
                }else{
                    current = current->left;
                }
            }
            new_node->parent = parent;
            if(value > parent->value){
                parent->right = new_node;
            }else{
                parent->left = new_node;
            }
        }
    }

    void traverse(node *n){
        if (n == nullptr){
            return;
        }else{
            this->traverse(n->left);
            cout<< n->value << "\n";
            this->traverse(n->right);
        }
    }
};

int main()
{
    BST bst = BST();
    bst.add_node(15);
    bst.add_node(10);
    bst.add_node(11);
    bst.add_node(16);
    bst.add_node(16);
    bst.add_node(22);
    bst.add_node(18);
    bst.traverse(bst.root);

    return 0;
}