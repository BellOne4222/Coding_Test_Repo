

import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	T = 3

	for tc in range(T):
		n1, n2 = "1001101", "10010"

		if n1 == '0' and n2 == '0':
			print(0)

		else:
			len_n1, len_n2 = len(n1), len(n2)
			if len_n1 != 80:
				n1 = '0'*(80-len_n1)+n1
			if len_n2 != 80:
				n2 = '0'*(80-len_n2)+n2

			rst_num = []
			tmp = 0
			for idx in range(80):
				now_sum = int(n1[79-idx])+int(n2[79-idx])+tmp
				if now_sum <= 1:
					rst_num.append(str(now_sum))
					tmp = 0
				elif now_sum == 2:
					rst_num.append('0')
					tmp = 1
				elif now_sum == 3:
					rst_num.append('1')
					tmp = 1

				if tmp == 1 and idx == 79:
					rst_num.append('1')

			len_rst_num = len(rst_num)
			for c in range(len_rst_num):
				if rst_num[len_rst_num-1-c] == '0':
					rst_num.pop()
				else:
					break
			print(''.join(rst_num[::-1]))