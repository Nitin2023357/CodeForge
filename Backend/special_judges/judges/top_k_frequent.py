from collections import Counter


def judge_top_k_frequent(
    user_output,
    expected_output,
    testcase
):

    try:

        lines = testcase["input"].strip().splitlines()

        first_line = lines[0].split()

        n = int(first_line[0])
        k = int(first_line[1])

        nums = list(
            map(
                int,
                lines[1].split()
            )
        )

        user_nums = list(
            map(
                int,
                user_output.split()
            )
        )

        if len(user_nums) != k:
            return False

        if len(set(user_nums)) != k:
            return False

        freq = Counter(nums)

        sorted_freq = sorted(
            freq.values(),
            reverse=True
        )

        kth_frequency = sorted_freq[k - 1]

        valid_numbers = set()

        for num, count in freq.items():

            if count >= kth_frequency:
                valid_numbers.add(num)

        for num in user_nums:

            if num not in valid_numbers:
                return False

        return True

    except:

        return False