/*
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/assignment-operator-overloading-c-only
@Language: C++
@Datetime: 17-01-16 08:22
*/

/*
ʵ�ָ�ֵ��������غ�����ȷ����
�µ����ݿ�׼ȷ�ر�����
�ɵ����ݿ�׼ȷ��ɾ��/�ͷ�
�ɽ��� A = B = C ��ֵ
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