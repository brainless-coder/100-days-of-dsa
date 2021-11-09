#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stdio.h>
using namespace std;

struct Activity {
	int start, finish;
};

bool activityComp(Activity a1, Activity a2) {
	return (a1.finish < a2.finish);
}

void activitySelection() {
	int n, x1, x2;
	int ans = 1;
	cin >> n;
	vector<Activity> activity {};
	for(int j = 0; j < n; ++j) {
		cin >> x1 >> x2;
		Activity act {x1, x2};
		activity.push_back(act);
	}

	sort(activity.begin(), activity.end(), activityComp);
	
	int i = 0, j = 1;
	cout << activity[0].start << " " << activity[0].finish << endl;
	for(; j < n; ++j) {
		if(activity[j].start >= activity[i].finish) {
			cout << activity[j].start << " " << activity[j].finish << endl;
			ans++;
			i = j;
		} 
	}

	cout << endl << ans << endl;

}

bool descComp(int a, int b) {
	return a > b;
}

int nikunjAndDonuts(vector<int> arr, int n) {
	int j {}, ans {};
	sort(arr.begin(), arr.end(), descComp);

	for(int i = 0; i < n; ++i) {
		ans += pow(2, j++)*arr[i];
	}

	return ans;
}

struct knapObject {
	int profit, weight;
};

bool knapsackComp(knapObject o1, knapObject o2) {
	double pw1 = double(o1.profit)/o1.weight;
	double pw2 = double(o2.profit)/o2.weight;
	return pw1 > pw2;
} 

void fractionalKnapsack() {
	int n, m, p, w;
	double finalProfit = 0;
	vector<knapObject> KnapsackObjects;
	cin >> n >> m;
	for(int i = 0; i < n; ++i) {
		cin >> p >> w;
		knapObject ob {p, w};
		KnapsackObjects.push_back(ob);
	}
	sort(KnapsackObjects.begin(), KnapsackObjects.end(), knapsackComp);

	int i = 0;
	while(m > 0 and i < n) {
		if (KnapsackObjects[i].weight <= m) {
			m -= KnapsackObjects[i].weight;
			finalProfit += KnapsackObjects[i].profit;
		} else {
			double pw = double(KnapsackObjects[i].profit)/KnapsackObjects[i].weight;
			finalProfit += (pw*m);
			m = 0;
		}
		i++;
	}

	cout << finalProfit << endl;
}

int main()
{
	// activitySelection();
	fractionalKnapsack();


	// int n, x;
	// cin >> n;
	// vector<int> arr {};
	// for(int i = 0; i < n; ++i) {
	// 	cin >> x;
	// 	arr.push_back(x);
	// }
	// cout << nikunjAndDonuts(arr, n) << endl;

	return 0;
}