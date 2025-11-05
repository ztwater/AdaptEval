# This function is adapted to work with a pandas DataFrame.
# The function takes as input a DataFrame with OHLCV data, the index
# of the current candle - 1, and the window size for checking, prd.
# The function returns the pivot value if found, otherwise None.
# It is assumed that the DataFrame has columns "high" and "low"
# which contain the highs and lows of the candle, respectively.


def find_pivot_highs(df, index, prd):
    # Create a window of size (prd * 2 + 1) around the current index
    # Extract values from the "high" column of DataFrame df
    window = df["high"].iloc[index - prd * 2 : index + 1].values

    # Find the maximum value in the last prd elements of the window
    high_max = max(window[-prd:])

    # Find the maximum value in the entire window
    max_value = max(window)

    # Check if the current value is the maximum in the window
    # and if it's greater than the maximum value in the last prd elements
    if max_value == window[prd] and window[prd] > high_max:
        return window[prd]

    return None


def find_pivot_lows(df, index, prd):
    # Create a window of size (prd * 2 + 1) around the current index
    # Extract values from the "low" column of DataFrame df
    window = df["low"].iloc[index - prd * 2 : index + 1].values

    # Find the minimum value in the last prd elements of the window
    low_min = min(window[-prd:])

    # Find the minimum value in the entire window
    min_value = min(window)

    # Check if the current value is the minimum in the window
    # and if it's less than the minimum value in the last prd elements
    if min_value == window[prd] and window[prd] < low_min:
        return window[prd]

    return None
