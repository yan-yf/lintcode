/*
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/assignment-operator-overloading-c-only
@Language: C++
@Datetime: 17-01-16 08:22
*/

/*
实现赋值运算符重载函数，确保：
新的数据可准确地被复制
旧的数据可准确地删除/释放
可进行 A = B = C 赋值
*/
class Solution {
public:
    char *m_pData;
    Solution() {
        this->m_pData = NULL;
    }
    Solution(char *pData) {
        this->m_pData = pData;
    }

    // Implement an assignment operator
    Solution operator=(const Solution &object) {
        // write your code here
       if (this != &object) {
           delete this->m_pData;
           if (object.m_pData != NULL) {
               m_pData = new char[strlen(object.m_pData)+1];
               strcpy(m_pData,object.m_pData);
           }
       }
       return *this;
    }
};