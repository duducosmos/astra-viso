"""
Imageutils unit tests.
"""
import unittest
import numpy as np
from astraviso import imageutils as iu

class imageutilstests(unittest.TestCase):
    """
    Imageutils unit test class.
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

class test_poisson_noise(imageutilstests):
    """
    Test poisson_noise function.
    """

    def test_empty_image(self):
        """
        Test output value and type.
        """

        # Allocate placeholder image
        image = np.zeros((512))

        # Add noise
        noisy_image = iu.poisson_noise(image, 0, 1200, 200)

        # Check result
        self.assertIsInstance(noisy_image, np.ndarray, "Output type should be ndarray.")
        self.assertEqual(noisy_image.shape, image.shape, "Image shape should be preserved.")
        self.assertTrue(np.all(noisy_image >= 0), "Image with noise should be strictly positive.")

class test_gaussian_noise(imageutilstests):
    """
    Test gaussian_noise function.
    """

    def test_empty_image(self):
        """
        Test output value and type.
        """

        # Allocate placeholder image
        image = np.zeros((512))

        # Add noise
        noisy_image = iu.gaussian_noise(image, 0, 1200, 200)

        # Check result
        self.assertIsInstance(noisy_image, np.ndarray, "Output type should be ndarray.")
        self.assertEqual(noisy_image.shape, image.shape, "Image shape should be preserved.")

class test_vismag2photon(imageutilstests):
    """
    Test vismag2photon function.
    """

    def test_single(self):
        """
        Test output value and type for single input.
        """

        # Set up visible magnitudes
        vismags = -1

        # Convert to photons
        photons = iu.vismag2photon(vismags, 1, 1, 1)

        # Check output
        self.assertIsInstance(photons, float, "Output type should be float.")
        self.assertGreater(photons, 0, "Photon count must be positive.")

    def test_single(self):
        """
        Test output value and type for multiple input.
        """

        # Set up visible magnitudes
        vismags = np.array([1, 0, -1])

        # Convert to photons
        photons = iu.vismag2photon(vismags, 1, 1, 1)

        # Check output
        self.assertEqual(len(photons), len(vismags), "Output size not equal to input.")
        self.assertIsInstance(photons, np.ndarray, "Output type should be float.")
        self.assertTrue(np.all(photons>0), "Photon counts must be positive.")
        self.assertGreater(photons[2], photons[0], "Incorrect output values.")
        self.assertEqual(photons[1], 1, "Incorrect output value for input 0.")
