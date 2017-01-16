/*
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/singleton
@Language: C++
@Datetime: 17-01-16 08:35
*/

/*
������������һ�� getInstance ���������ڸ������࣬ÿ�ε��� getInstance ʱ�����ɵõ�ͬһ��ʵ����
*/

class Solution {
public:
    /**
     * @return: The same instance of this class every time
     */
    static Solution* getInstance() {
        // write your code here
        static bool ex = false;
        static Solution* one;
        if(ex == false) {
            one = new Solution();
            ex = true;
            return one;
        }
        return one;
    }
};