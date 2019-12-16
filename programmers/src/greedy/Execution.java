package greedy;

public class Execution {
	public static void main(String[] args) {

		// int n = 7;
		// int[] lost = { 2,3,4};
		// int[] reserve = {1,2,3,6 };
		int n = 7;
		int[] lost = { 1, 3, 5 };
		int[] reserve = { 2, 3, 6 };
		// int n = 4;
		// int[] lost = { 1, 2 };
		// int[] reserve = { 1 };
		GymSuit gs = new GymSuit();
		int result = gs.solution(n, lost, reserve);
		System.out.println("Answer: " + result);
	}
}
