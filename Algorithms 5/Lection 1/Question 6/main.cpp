#include <iostream>
#include <vector>

using namespace std;

string count_odd(vector<int>& nums) {
    int f = nums[0];
    bool is_odd = (f % 2 != 0);
    vector<char> result;

    for (size_t i = 1; i < nums.size(); ++i) {
        int s = nums[i];

        if (is_odd && s % 2 != 0) {
            result.push_back('x');
            f *= s;  // Оба нечётные → результат остаётся нечётным
        } else {
            result.push_back('+');
            f += s;
            is_odd = (f % 2 != 0);  // Обновляем чётность
        }
    }

    return string(result.begin(), result.end());
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    cout << count_odd(nums) << endl;
    return 0;
}
