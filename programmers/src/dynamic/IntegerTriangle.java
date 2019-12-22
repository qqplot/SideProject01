package dynamic;

class IntegerTriangle {
	public int solution(int[][] triangle) {
		int answer = 0;

		int maxValue = 0;
		int startFloor = 0;
		int startPoint = 0;

		for (int i = 0; i < triangle.length; i++) {
			int[] floor = triangle[i];
			for (int j = 0; j < floor.length; j++) {
				int num = floor[j];
				if (num >= maxValue) {
					maxValue = num;
					startFloor = i;
					startPoint = j;
				}
			}
		}

//		System.out.println("maxValue: " + maxValue + ", startFloor: " + startFloor + ", startPoint: " + startPoint);

		answer = this.findNode(triangle, startFloor, startPoint);

		return answer;
	}

	private int findNode(int[][] triangle, int startFloor, int startPoint) {

		int upResult = 0;
		int downResult = 0;
		int currentPoint = startPoint;

		// up
		for (int f = startFloor; f >= 0; f--) {
			int[] curruentFloor = triangle[f];
			upResult += curruentFloor[currentPoint];

			if (f == 0)
				break;

			int[] nextFloor = triangle[f - 1];
			if (currentPoint == 0) {
				continue;
			}
			if (nextFloor[currentPoint - 1] > nextFloor[currentPoint]) {
				currentPoint--;
			}
		}

		// down
		currentPoint = startPoint; // reset
		for (int f = startFloor; f < triangle.length; f++) {

			int[] curruentFloor = triangle[f];

			downResult += curruentFloor[currentPoint];

			if (f == triangle.length - 1)
				break;

			int[] nextFloor = triangle[f + 1];
			if (nextFloor[currentPoint + 1] > nextFloor[currentPoint]) {
				currentPoint++;
			}
		} // for

//		System.out.println("up result: " + upResult);
//		System.out.println("down result: " + downResult);

		// up & down 스타팅이 겹치므로 한번 빼줘야 한다.
		return upResult + downResult - triangle[startFloor][startPoint];
	}

}
