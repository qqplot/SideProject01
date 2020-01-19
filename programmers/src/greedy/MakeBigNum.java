package greedy;

class MakeBigNum {

	public String solution(String number, int k) {

		// StringBuffer보다 속도가 빠름
		StringBuilder str = new StringBuilder(number);
		int pointer = -1;
		while (k > 0) {

			pointer++;
			
			// 마지막 숫자의 경우
			if (pointer == str.length() - 1) {

				// 마지막 숫자가 최솟값인 경우
				if (str.charAt(pointer) < str.charAt(pointer - 1)) {
					str.deleteCharAt(pointer);
					str.delete(0, k - 1);
				} else { // 모든 숫자가 동일한 경우
					str.delete(0, k);
				}
				break;
			}

			// 9일 경우 비교 연산하지 않음
			if (str.charAt(pointer) == '9')
				continue;

			
			// 다음 인덱스의 숫자보다 작을 경우
			if (str.charAt(pointer) < str.charAt(pointer + 1)) {
				k--;
				str.deleteCharAt(pointer);
				pointer = -1;
			}

		}
		return str.toString();
	}

}
