import pytest
from main import get_matches_result_no_recursion, get_matches_result_recursion, find_x_no_recursion, find_x_recursion


def normalize(paths):
    return sorted(tuple(p) for p in paths)

# Tests: get_matches_result_recursion
class TestGetMatchesResultRecursion:

    def test_k1_returns_two_paths(self):
        result = get_matches_result_recursion(1)
        assert len(result) == 2

    def test_k1_correct_paths(self):
        expected = [
            ['0:0', '1:0'],
            ['0:0', '0:1'],
        ]
        assert normalize(get_matches_result_recursion(1)) == normalize(expected)

    def test_k2_returns_six_paths(self):
        result = get_matches_result_recursion(2)
        assert len(result) == 6

    def test_k2_all_paths_start_at_0_0(self):
        for path in get_matches_result_recursion(2):
            assert path[0] == '0:0'

    def test_k2_all_paths_end_with_score_k(self):
        k = 2
        for path in get_matches_result_recursion(k):
            a, b = map(int, path[-1].split(':'))
            assert max(a, b) == k

    def test_k2_path_length_in_valid_range(self):
        k = 2
        for path in get_matches_result_recursion(k):
            assert k + 1 <= len(path) <= 2 * k + 1

    def test_k3_returns_twenty_paths(self):
        result = get_matches_result_recursion(3)
        assert len(result) == 20

    def test_k1_paths_are_lists(self):
        for path in get_matches_result_recursion(1):
            assert isinstance(path, list)

    def test_each_step_increments_exactly_one_score(self):
        for path in get_matches_result_recursion(2):
            for prev, curr in zip(path, path[1:]):
                pa, pb = map(int, prev.split(':'))
                ca, cb = map(int, curr.split(':'))
                assert (ca - pa, cb - pb) in [(1, 0), (0, 1)]



# Tests: get_matches_result_no_recursion
class TestGetMatchesResultNoRecursion:

    def test_k1_returns_two_paths(self):
        assert len(get_matches_result_no_recursion(1)) == 2

    def test_k1_correct_paths(self):
        expected = [
            ['0:0', '1:0'],
            ['0:0', '0:1'],
        ]
        assert normalize(get_matches_result_no_recursion(1)) == normalize(expected)

    def test_k2_returns_six_paths(self):
        assert len(get_matches_result_no_recursion(2)) == 6

    def test_k2_all_paths_end_with_score_k(self):
        k = 2
        for path in get_matches_result_no_recursion(k):
            a, b = map(int, path[-1].split(':'))
            assert max(a, b) == k

    def test_k3_returns_twenty_paths(self):
        assert len(get_matches_result_no_recursion(3)) == 20

    def test_matches_recursion_for_k1(self):
        assert normalize(get_matches_result_no_recursion(1)) == normalize(get_matches_result_recursion(1))

    def test_matches_recursion_for_k2(self):
        assert normalize(get_matches_result_no_recursion(2)) == normalize(get_matches_result_recursion(2))

    def test_matches_recursion_for_k3(self):
        assert normalize(get_matches_result_no_recursion(3)) == normalize(get_matches_result_recursion(3))

    def test_each_step_increments_exactly_one_score(self):
        for path in get_matches_result_no_recursion(2):
            for prev, curr in zip(path, path[1:]):
                pa, pb = map(int, prev.split(':'))
                ca, cb = map(int, curr.split(':'))
                assert (ca - pa, cb - pb) in [(1, 0), (0, 1)]



# Tests: find_x_recursion
class TestFindXRecursion:

    def test_i0_returns_x_unchanged(self):
        assert find_x_recursion(5, 0) == 5
        assert find_x_recursion(0, 0) == 0
        assert find_x_recursion(-3, 0) == -3

    def test_i1_formula(self):
        x = 1
        expected = (x + 1) / (x + 2)  # 2/3
        assert find_x_recursion(x, 1) == pytest.approx(expected)

    def test_i2_formula(self):
        x = 1
        step1 = (x + 1) / (x + 2)
        expected = (step1 + 1) / (step1 + 2)
        assert find_x_recursion(x, 2) == pytest.approx(expected)

    def test_known_value_x1_i1(self):
        assert find_x_recursion(1, 1) == pytest.approx(2 / 3)

    def test_known_value_x1_i2(self):
        assert find_x_recursion(1, 2) == pytest.approx(5 / 8)

    def test_convergence(self):
        v10 = find_x_recursion(1, 10)
        v11 = find_x_recursion(1, 11)
        assert abs(v10 - v11) < 0.01

    def test_returns_float(self):
        assert isinstance(find_x_recursion(1, 1), float)

    def test_x0_i1(self):
        assert find_x_recursion(0, 1) == pytest.approx(1 / 2)



# Tests: find_x_no_recursion
class TestFindXNoRecursion:

    def test_i0_returns_x_unchanged(self):
        assert find_x_no_recursion(5, 0) == 5
        assert find_x_no_recursion(0, 0) == 0

    def test_i1_formula(self):
        x = 1
        expected = (x + 1) / (x + 2)
        assert find_x_no_recursion(x, 1) == pytest.approx(expected)

    def test_known_value_x1_i1(self):
        assert find_x_no_recursion(1, 1) == pytest.approx(2 / 3)

    def test_known_value_x1_i2(self):
        assert find_x_no_recursion(1, 2) == pytest.approx(5 / 8)

    def test_matches_recursion_various_inputs(self):
        for x in [0, 1, 2, 0.5, -0.5]:
            for i in range(6):
                assert find_x_no_recursion(x, i) == pytest.approx(
                    find_x_recursion(x, i), rel=1e-9
                )

    def test_convergence(self):
        v10 = find_x_no_recursion(1, 10)
        v11 = find_x_no_recursion(1, 11)
        assert abs(v10 - v11) < 0.01

    def test_returns_float(self):
        assert isinstance(find_x_no_recursion(1, 1), float)