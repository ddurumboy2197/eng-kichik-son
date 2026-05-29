# test_min.py
import pytest
from min_numbers import find_min

def test_min_numbers():
    assert find_min([1, 2, 3]) == 1
    assert find_min([5, 2, 9]) == 2
    assert find_min([10, 20, 30]) == 10
    assert find_min([1, 1, 1]) == 1
    assert find_min([-1, 0, 1]) == -1
    assert find_min([]) == None
```

```javascript
// minNumbers.test.js
import { findMin } from './minNumbers';

describe('findMin function', () => {
  it('should return the smallest number in an array', () => {
    expect(findMin([1, 2, 3])).toBe(1);
    expect(findMin([5, 2, 9])).toBe(2);
    expect(findMin([10, 20, 30])).toBe(10);
    expect(findMin([1, 1, 1])).toBe(1);
    expect(findMin([-1, 0, 1])).toBe(-1);
    expect(findMin([])).toBeUndefined();
  });
});
