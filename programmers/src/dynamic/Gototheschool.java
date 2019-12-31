package dynamic;

class Gototheschool {

	int M;
	int N;
	int[][] cache;

	public int solution(int m, int n, int[][] puddles) {

		this.M = m;
		this.N = n;
		this.cache = new int[m + 1][n + 1];

		return this.countPath(1, 1, puddles);
	}

	private int countPath(int m, int n, int[][] puddles) {

		// Outside
		if (m > M || n > N)
			return 0;

		// Final Node
		if (m == M && n == N)
			return 1;

		// Puddles
		for (int[] puddle : puddles) {
			if (m == puddle[0] && n == puddle[1]) {
				return 0;
			}
		}

		// Memoization
		int ret = this.cache[m][n];
		if (ret != 0)
			return cache[m][n];

		ret = (countPath(m + 1, n, puddles) + countPath(m, n + 1, puddles))%1000000007;
		cache[m][n] = ret;
		return ret;

	}

}
