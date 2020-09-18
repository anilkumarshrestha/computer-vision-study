
def get_peaks(arr_padded):
    """Returns the index of peaks"""

    peaks = np.array([], dtype=int)
    for i in range(1, arr_padded.size - 1):
        if((arr_padded[i]) >= arr_padded[ i-1 ] and (arr_padded[i] >= arr_padded[ i+1 ])):
            # Append the peak index
            peaks = np.append(peaks, i)
    return peaks

if __name__ == "__main__":
    import numpy as np
    import time
    from scipy.signal import find_peaks
    
    # Form an array with random values
    arr = np.random.randint(255, size=1000)
    
    # Add 1 padding on each side to include borders.
    # Here I use minimum value of the array 
    no_of_pad = 1
    arr_padded = np.pad(arr, (no_of_pad,), 'minimum')

    # Find index without padding
    start = time.process_time()
    peaks_no_pad = get_peaks(arr)
    time_get_peaks = time.process_time() - start
    
    # Find index with scipy
    start = time.process_time()
    peaks_sci, _ = find_peaks(arr)
    time_sci = time.process_time() - start

    # Find index with padding.
    # Subtract number of padding from each index
    # to get the actual index
    peaks = get_peaks(arr_padded) - no_of_pad
    
    print("Original array: ", arr)
    print("Index with no padding: ", peaks_no_pad)
    print("Index with scipy: ", peaks_sci)
    print("Index with padding: ", peaks)

    print("Peak values", arr[peaks_no_pad])
    # print(time_get_peaks)
    # print(time_sci)
    print("Time diff (get_peaks - scipy): ", time_get_peaks - time_sci)

