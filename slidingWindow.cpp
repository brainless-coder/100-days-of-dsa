#include<iostream>
#include<vector>
#include<unordered_map>
#include<queue>
using namespace std;

int maxSubArraySumNaive(int *arr, int n, int k) {
    int sum {}, ans = -99999;
    for (int i = 0; i < n-k+1; ++i) {
        sum = 0;
        for (int j = i; j < i+k; ++j) {
            sum += arr[j];
        }
        if (sum > ans)  ans = sum;
    }
    return ans;
}

// Not a very general way for sliding window questions
int maxSubArraySumSlidingWindow1(int *arr, int n, int k) {
    int currSum {}, maxSum {};
    for (int i = 0; i < k; ++i) currSum += arr[i];
    maxSum = currSum;
    
    for (int i = 0, j = k; j < n; i++, j++) {
        currSum += arr[j];
        currSum -= arr[i];
        if (currSum > maxSum)   maxSum = currSum;
    }
    return maxSum;
}

int maxSubArraySumSlidingWindow2(int arr[], int n, int k) {
    int currSum {}, maxSum = -99999;
    for(int i = 0, j = 0; j < n; ++j) {
        currSum += arr[j];
        if (j-i+1 == k) {
            maxSum = max(currSum, maxSum);
            currSum -= arr[i];
            i++;
        }
    }
    return maxSum;
}

void firstNegInEveryWindowNaive(int *arr, int n, int k) {
    for (int i = 0; i < n-k+1; ++i) {
        bool flag = false;
        for (int j = i; j < i+k; ++j) {
            if (arr[j] < 0) {
                cout << arr[j] << " ";
                flag = true;
                break;
            }
        }
        if (!flag)  cout << 0 << " ";
    }
    cout << endl;
}

void firstNegInEveryWindowSlidingWindow(vector<int> vec, int n, int k) {
    queue<int> q;
    int i = 0, j = 0;

    while (j < n) {
        if (vec[j] < 0) q.push(vec[j]);
        if (j-i+1 == k) {
            cout << (q.empty() ? 0 : q.front()) << " ";
            if (!q.empty() && vec[i] == q.front()) {
                q.pop();
            }
            i++;
        }
        j++;
    }
    cout << endl;
}

int occOfAnagram(string s, string patt, int k) {
    unordered_map<char, int> patMap;
    int count {}, n = s.length();
    for(int i = 0; i < patt.length(); ++i) {
        patMap[patt[i]]++;
    }

    int i {}, j {};
    while (j < n) {
        if(patMap.find(s[j]) != patMap.end())
            patMap[s[j]]--;
        if (j-i+1 == k) {
            bool flag = true;
            for(auto itr = patMap.begin(); itr != patMap.end(); ++itr) {
                if (itr->second > 0) {
                    flag = false;
                    break;
                }
            }
            if(flag)    count++;
            if(patMap.find(s[i]) != patMap.end())
                patMap[s[i]]++;
            i++;
        }
        j++;
    }

    return count;
}

// https://leetcode.com/problems/sliding-window-maximum/   
void maxmOfAllSubarrayOfSizeK(int n, vector<int> arr, int k) {
    deque <int> maxm;
    vector<int> ans;
    int i = 0, j = 0;
    
    while(j < n) {
        while(maxm.size() > 0 && maxm.back() < arr[j])
            maxm.pop_back();
        maxm.push_back(arr[j]);

        if(j-i+1 == k) {
            ans.push_back(maxm.front());
            if(maxm.front() == arr[i]) {
                maxm.pop_front();
            }
            i++;
        }
        j++;
    }
    
    for(auto x: ans)
        cout << x << " ";
    cout << endl;
    
}

// Return the size of largest subarray whose sum is K
int largestSubarryofSumKNaive(vector<int> arr, int k) {
    int n = arr.size();
    int i {}, j {}, sum {};
    int ans = 0;

    // O(n^2)
    for(int i = 0; i < n; ++i) {
        sum = 0;
        int currLen = 0;
        for(int j = i; j < n; ++j) {
            sum += arr[j];
            currLen++;
            if(sum == k) {
                ans = max(ans, currLen);
            }
        }
    }

    return ans;
}

int largestSubarryofSumK(vector<int> arr, int k) {
    int n = arr.size();
    int i {}, j {}, maxm {}, sum {};

    while (j < n) {
        sum += arr[j];
        // if (sum < k)    j++;
        if (sum == k) {
            maxm = max(maxm, j-i+1);
        } 
        // Ab agar sum baara hai to j ko aage mat le jao, bcoz ek possible candidate ho sakta hai
        while(sum > k) {
            sum -= arr[i];
            i++;
            if (sum == k) {
                maxm = max(maxm, j-i+1);
            } 
        }
        j++;
    }

    return maxm;
}

int longestSubstringWithKUniqChar(string s, int k) {
    int n = s.length();
    unordered_map<char, int> freq;
    int i {}, j {}, ans {};

    while (j < n) {
        freq[s[j]]++;
        if (freq.size() == k) {
            ans = max(ans, j-i+1);
        }

        while (freq.size() > k) {
            freq[s[i]]--;
            if(freq[s[i]] == 0) {
                freq.erase(s[i]);
            }
            i++;
        }
        j++;
    }

    return ans;
}

// Longest substring without repeating char or with all unique cahracters
int longestSubstringWithoutRepeatingChar(string s) {
        unordered_map<char, int> freq;
        int n = s.length();
        int i = 0, j = 0, ans = 0;
        
        while (j < n) {
            freq[s[j]]++;
            
            if (freq.size() == j-i+1) {
                ans = max(ans, j-i+1);
            }
            
            while (freq.size() < j-i+1) {
                freq[s[i]]--;
                if(freq[s[i]] == 0)
                    freq.erase(s[i]);
                i++;
            }
            j++;
        }
        
        return ans;
    }


int main() {

    // int n, k;
    // cin >> n >> k;
    // int arr[n];
    // for(int i = 0; i < n; ++i)  cin >> arr[i];
    // vector<int> vec;
    // int x;
    // for(int i = 0; i < n; ++i) {
    //     cin >> x;
    //     vec.push_back(x);
    // }

    // cout << maxSubArraySumNaive(arr, n, k) << endl;
    // cout << maxSubArraySumSlidingWindow1(arr, n, k) << endl;
    // cout << maxSubArraySumSlidingWindow2(arr, n, k) << endl;
    // firstNegInEveryWindowNaive(arr, n, k);
    // firstNegInEveryWindowSlidingWindow(vec, n, k);
    
    string s, pattern;
    int k;
    getline(cin, s);
    // getline(cin, pattern);
    cin >> k;
    // cout << occOfAnagram(s, pattern, k);

    // maxmOfAllSubarrayOfSizeK(n, vec, k);

    // Variable sized window
    // cout << largestSubarryofSumKNaive(vec, k) << endl;
    // cout << largestSubarryofSumK(vec, k);
    cout << longestSubstringWithKUniqChar(s, k);
    cout << longestSubstringWithoutRepeatingChar(s);



    return 0;
}