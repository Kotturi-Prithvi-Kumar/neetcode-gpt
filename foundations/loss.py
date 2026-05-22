import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        
        shift = z - np.max(z)
        exp = np.exp(shift)
        return np.round(exp / np.sum(exp),4)