/*
@Copyright:LintCode
@Author:   yfyan
@Problem:  http://www.lintcode.com/problem/singleton
@Language: C++
@Datetime: 17-01-16 08:35
*/

/*
你的任务是设计一个 getInstance 方法，对于给定的类，每次调用 getInstance 时，都可得到同一个实例。
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