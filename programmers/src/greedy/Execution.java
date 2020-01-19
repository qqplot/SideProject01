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
		
		
//		String number = "1924";
//		int k = 2;
//		String rigtht_ans = "94";
		
//		String number = "4177252841";
//		int k = 4;
//		String rigtht_ans = "775841";
		String number = "333332";
		int k = 3;
		String rigtht_ans = "333";
		
		
		MakeBigNum mbn = new MakeBigNum();
		String res = mbn.solution(number, k);
		if (rigtht_ans.equals(res))
			System.out.println("MakeBigNum Result: " + res);
		else
			System.out.println("Wrong..");
		
		
	}
}
