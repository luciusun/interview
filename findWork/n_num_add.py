// main.cpp
#include <iostream>
#include <vector>
#include <set>
using namespace std;


class Solution {
public:
    vector<vector<int >> fourSum(vector<int > &nums, int target) {

        set<vector<int >> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < int(nums.size() - 3); ++i) {
            for (int j = i + 1; j < int(nums.size() - 2); ++j) {
                int left = j + 1, right = nums.size() - 1;
                while (left < right) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        vector<int> out;
                        out.push_back(nums[i]);
                        out.push_back(nums[j]);
                        out.push_back(nums[left]);
                        out.push_back(nums[right]);
                        res.insert(out);
                        ++left; --right;
                    } else if (sum < target) ++left;
                    else --right;
                }
            }
        }
        return vector<vector<int> > (res.begin(), res.end());
    }
};


void reverse_with_index(vector<vector<int>> vec)
{
    if (vec.empty())
    {
        cout << "The vector is empty!" << endl;
        return;
    }

    int i,j;
    cout << "Use index : " << endl;
    for (i = 0; i < vec.size(); i++)
    {
        for(j = 0; j < vec[0].size(); j++)
            cout << vec[i][j] << " ";
        cout << endl;
    }
}


int main()
{
    vector<int > money = {3978, 2431, 3383, 2556, 1018, 2669, 3260, 3645,4215,439,1460,5651,1382,2243,2811,2445,4293,1230,1462,1280,2880,1667,1324,1619,1471,1345,2226,969,2381,1042,2067,901,1543,1869,1994,950,1412,1049,2073,1467,1452,1044,1650,1518,2283,3236,1796,1688,2161,1196};
//    vector<float > money = {1.1, 2, 3, 4, 5, 6, 7.1, 8, 9};
    vector<vector<int> > anwser;

    Solution simple;
    anwser = simple.fourSum(money, 7419);


    reverse_with_index(anwser);





    return 0;
}
