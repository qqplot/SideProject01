package dynamic;

class ExpressAsN {

	int answer = 9;
	int cnt = 0;

	public int solution(int N, int number) {

		this.dfs(N, number, 0, 0);
		System.out.println("확인: "+this.cnt);
		return (answer > 8) ? -1 : answer;
		
	}

	private void dfs(int N, int number, int idx, int sum) {
		
		cnt++;
		if (idx > 8)
			return;

		if (number == sum)
			this.answer = Math.min(answer, idx);

		int tmp = 0;

		for (int i = 0; i < 8; i++) {
			tmp = tmp * 10 + N;
			dfs(N, number, idx + i + 1, sum + tmp);
			dfs(N, number, idx + i + 1, sum - tmp);
			dfs(N, number, idx + i + 1, sum * tmp);
			dfs(N, number, idx + i + 1, sum / tmp);
		}

	}

}
