#include <iostream>
#include <vector>

using namespace std;

double findMaxAverage(vector<int> &nums, int k)
{
    double total = 0;
    size_t leftIndex = 0;
    double maxSum = 0;

    for (size_t i = 0; i < k; ++i)
    {
        total += nums[i];
    }

    maxSum = total;

    for (size_t i = k; i < nums.size(); ++i)
    {
        total += nums[i] - nums[leftIndex];
        leftIndex++;

        if (total > maxSum)
        {
            maxSum = total;
        }
    }

    return maxSum / k;
}

int main()
{
    vector<int> nums = {1, 12, -5, -6, 50, 3};
    int k = 4;

    for (size_t i = 0; i < nums.size(); ++i)
    {
        cout << nums[i] << endl;
    }

    cout << findMaxAverage(nums, k) << endl;

    return EXIT_SUCCESS;
}
