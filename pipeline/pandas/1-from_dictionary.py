#!/usr/bin/env python3
""" creating a script defining dp"""

import pandas as pd


data = {
      "First": [0.0, 0.5, 1.0, 1.50],
      "Second": ["one", "two", "three", "four"]
    }
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
