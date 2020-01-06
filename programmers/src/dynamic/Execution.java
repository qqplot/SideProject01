package dynamic;

public class Execution {
	public static void main(String[] args) {

		// 정수삼각형
		int[][] triangle = { { 7 }, { 3, 8 }, { 8, 1, 0 }, { 2, 7, 4, 4 }, { 4, 5, 2, 6, 5 } };

		IntegerTriangle sol = new IntegerTriangle();
		int result = sol.solution(triangle);
		System.out.println("IntegerTriangle result: " + result);

		// 등굣길
		int m = 4;
		int n = 3;
		int[][] puddles = { { 2, 2 } };
		Gototheschool gts = new Gototheschool();
		result = gts.solution(m, n, puddles);
		System.out.println("Gototheschool result: " + result);

		// N으로 표현
//		int N = 5;
//		int number = 12;
		 int N = 2;
		 int number = 11;
		ExpressAsN ean = new ExpressAsN();
		result = ean.solution(N, number);
		System.out.println("ExpressAsN result: " + result);

	}
}
