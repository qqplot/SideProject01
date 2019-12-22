package dynamic;

public class Execution {
	public static void main(String[] args) {
		int[][] triangle = { { 7 }, { 3, 8 }, { 8, 1, 0 }, { 2, 7, 4, 4 }, { 4, 5, 2, 6, 5 } };
		
		IntegerTriangle sol = new IntegerTriangle();
		int result = sol.solution(triangle);
		System.out.println("result: " + result);

	}
}
