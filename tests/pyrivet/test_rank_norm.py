from pyrivet import rivet, rank
import math

prism_3 = rivet.Bifiltration("x_label", "y_label", [

    [1, 2, 4],
    [2, 4, 5],
    [0, 1, 3],
    [1, 3, 4],
    [0, 2, 3],
    [2, 5, 3],
    [0, 1, 2],
    [3, 4, 5]],
                             appearances=[
    [(0, 0)],
    [(0, 0)],
    [(0, 0)],
    [(0, 0)],
    [(0, 0)],
    [(0, 0)],
    [(4, 0)],
    [(0, 4)]
])

prism_3_shift = rivet.Bifiltration("x_label", "y_label", [
    [ 1, 2, 4],
    [ 2, 4, 5],
    [ 0, 1, 3],
    [ 1, 3, 4],
    [ 0, 2, 3],
    [ 2, 5, 3],
    [ 0, 1, 2],
    [ 3, 4, 5]],
                                   appearances=[

    [(-1, -2)],
    [(-1, -2)],
    [(-1, -2)],
    [(-1, -2)],
    [(-1, -2)],
    [(-1, -2)],
    [(3, -2)],
    [(-1, 2)]
])

prism_3_stretch = rivet.Bifiltration("x_label", "y_label", [

    [1, 2, 4],
    [2, 4, 5],
    [0, 1, 3],
    [1, 3, 4],
    [0, 2, 3],
    [2, 5, 3],
    [0, 1, 2],
    [3, 4, 5]],
                                     appearances=[

    [(0, 0)],
    [(0, 0)],
    [(0, 0)],
    [(0, 0)],
    [(0, 0)],
    [(0, 0)],
    [(4, 0)],
    [(0, 8)]
])

# simple test with rank function at most one
# TODO: Add more tests for rank_norm
def test_rank_norm():
    mod = rivet.compute_bifiltration(prism_3, homology=1)
    val = rank.rank_norm(mod, module2=None, grid_size=65, fixed_bounds=None, use_weights=False, normalize=False,
                         minimum_rank=0)
    assert math.isclose(val, 64, abs_tol=2)


def test_rank_norm_shift():
    mod_shift = rivet.compute_bifiltration(prism_3_shift, homology=1)
    val = rank.rank_norm(mod_shift, module2=None, grid_size=20, fixed_bounds=None, use_weights=False, normalize=False,
                         minimum_rank=0)
    assert math.isclose(val, 64, abs_tol=2)


def test_rank_norm_stretch():
    mod_stretch = rivet.compute_bifiltration(prism_3_stretch, homology=1)
    val = rank.rank_norm(mod_stretch, module2=None, grid_size=20, fixed_bounds=None, use_weights=False, normalize=True,
                         minimum_rank=0)
    assert math.isclose(val, .25, abs_tol=1e-1)

# val = matching_distance.find_offset(math.degrees(math.atan(2)), (1, 3), 0)
# assert math.isclose(val, 1, abs_tol=1e-8)
