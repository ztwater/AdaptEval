import unittest
from tqdm import tqdm
from joblib import Parallel, delayed

from joblib_progress_bar import tqdm_joblib


class TestTqdmJoblib(unittest.TestCase):
    def test_add_type_annotations(self):
        annotations = tqdm_joblib.__annotations__
        self.assertIn('tqdm_object', annotations)
        self.assertEqual(annotations['tqdm_object'], tqdm)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], None)

    def test_context_manager_behavior(self):
        dummy_tqdm = tqdm(total=10)
        with tqdm_joblib(dummy_tqdm) as progress_bar:
            results = list(Parallel(n_jobs=1)(delayed(lambda x: x)(i) for i in range(10)))
            # results = list(Parallel(n_jobs=2)(delayed(lambda x: x)(i) for i in range(5)))
            self.assertEqual(len(results), 10)
            # Check that the progress bar has been updated correctly
            self.assertEqual(progress_bar.n, 10)
            self.assertEqual(progress_bar.n, progress_bar.total)


if __name__ == '__main__':
    unittest.main()