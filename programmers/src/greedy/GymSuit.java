package greedy;

import java.util.ArrayList;

public class GymSuit {

	public int solution(int n, int[] lost, int[] reserve) {
		int answer = n - lost.length;

		ArrayList<Integer> reserveList = new ArrayList<>();
		ArrayList<Integer> lostList = new ArrayList<>();

		for (int i = 0; i < lost.length; i++) {
			lostList.add(lost[i]);
		}

		for (int i = 0; i < reserve.length; i++) {
			reserveList.add(reserve[i]);
		}

		for (int i = 0; i < reserveList.size(); i++) {
			for (int j = 0; j < lostList.size(); j++) {
				if (reserveList.get(i) == lostList.get(j)) {
					reserveList.set(i, -1);
					lostList.remove(j);
					answer++;
				}
			}
		}
		reserveList.sort(null);

		for (int i = 0; i < lostList.size(); i++) {
			int lostStudent = lostList.get(i);
			for (int j = 0; j < reserveList.size(); j++) {
				int haveStudent = reserveList.get(j);

				if (lostStudent - 1 == haveStudent || lostStudent + 1 == haveStudent) {
					answer++;
					reserveList.remove(j);
				}
			}

		}
		return answer;
	}

}
