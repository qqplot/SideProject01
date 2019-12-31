package dynamic;


class IntegerTriangle {

	int[][] cache = new int[500][500];

	public int solution(int[][] triangle) {
		
		int answer = this.findNode(triangle, 0, 0);
//		for(int i=0;i< 500; i++) {
//			for(int j=0;j<500;j++) {
//				if(cache[i][j] != 0) {
//					System.out.println("i: " + i +", j:"+j +", sum: " + cache[i][j]);
//				}
//			}
//		}
			
		return answer;
	}

	private int findNode(int[][] triangle, int startFloor, int startPoint) {

		// 기저 사례: 마지막 층에 도착했을 때
		if (startFloor == triangle.length - 1)
			return triangle[startFloor][startPoint];

		// 메모이제이션
		int ret = this.cache[startFloor][startPoint];
		if(ret != 0)
			return ret;
		
		ret = Math.max(findNode(triangle, startFloor + 1, startPoint + 1),
				findNode(triangle, startFloor + 1, startPoint)) + triangle[startFloor][startPoint];
		
		this.cache[startFloor][startPoint] = ret;
		return ret;

	}

}
