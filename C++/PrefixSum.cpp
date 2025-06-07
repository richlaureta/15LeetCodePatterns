#include <iostream>
#include <vector>

class NumArray
{
private:
    std::vector<int> numbers;

public:
    NumArray(std::vector<int> &nums)
    {
        for (int i = 1; i < nums.size(); i++)
        {
            nums[i] += nums[i - 1];
        }
        numbers = nums;
    }

    int sumRange(int left, int right)
    {
        if (left == 0)
        {
            return numbers[right];
        }
        else
        {
            return (numbers[right] - numbers[left - 1]);
        }
    }
};
int main()
{
    std::vector<int> arr = {-2, 0, 3, -5, 2, -1};

    NumArray instance0 = NumArray(arr);
    std::cout << instance0.sumRange(0, 2) << std::endl;
    std::cout << instance0.sumRange(2, 5) << std::endl;
    std::cout << instance0.sumRange(0, 5) << std::endl;

    std::cout << "Exit Success!" << std::endl;

    return EXIT_SUCCESS;
}