from collections import Counter


def judge_group_anagrams(
    user_output,
    expected_output,
    testcase
):

    try:

        lines = testcase["input"].strip().splitlines()

        words = lines[1].split()

        original_words = Counter(words)

        user_lines = [
            line.strip()
            for line in user_output.strip().splitlines()
            if line.strip()
        ]

        used_words = []

        user_groups = []

        for line in user_lines:

            group = line.split()

            user_groups.append(group)

            used_words.extend(group)

        if Counter(used_words) != original_words:
            return False

        for group in user_groups:

            key = "".join(
                sorted(group[0])
            )

            for word in group:

                if "".join(sorted(word)) != key:
                    return False

        family_count = {}

        for group in user_groups:

            key = "".join(
                sorted(group[0])
            )

            family_count[key] = (
                family_count.get(key, 0)
                + 1
            )

        for count in family_count.values():

            if count > 1:
                return False

        return True

    except:

        return False