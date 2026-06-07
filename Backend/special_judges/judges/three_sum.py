def normalize_triplets(output):

    triplets = []

    lines = output.strip().splitlines()

    for line in lines:

        nums = list(
            map(
                int,
                line.split()
            )
        )

        nums.sort()

        triplets.append(
            tuple(nums)
        )

    triplets.sort()

    return triplets


def judge_three_sum(
    user_output,
    expected_output,
    testcase
):

    try:

        user_triplets = normalize_triplets(
            user_output
        )

        expected_triplets = normalize_triplets(
            expected_output
        )

        return (
            user_triplets
            ==
            expected_triplets
        )

    except:

        return False