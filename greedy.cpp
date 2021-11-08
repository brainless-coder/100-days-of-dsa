#include<iostream>
#include<vector>
#include<algorithm>
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

int main()
{
	activitySelection();
	
	return 0;
}