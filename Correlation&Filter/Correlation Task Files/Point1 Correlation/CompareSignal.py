# def Compare_Signals(file_name,Your_indices,Your_samples):      
#     expected_indices=[]
#     expected_samples=[]
#     with open(file_name, 'r') as f:
#         line = f.readline()
#         line = f.readline()
#         line = f.readline()
#         line = f.readline()
#         while line:
#             # process line
#             L=line.strip()
#             if len(L.split(' '))==2:
#                 L=line.split(' ')
#                 V1=int(L[0])
#                 V2=float(L[1])
#                 expected_indices.append(V1)
#                 expected_samples.append(V2)
#                 line = f.readline()
#             else:
#                 break
#     print("Current Output Test file is: ")
#     print(file_name)
#     print("\n")
#     if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
#         print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
#         return
#     for i in range(len(Your_indices)):
#         if(Your_indices[i]!=expected_indices[i]):
#             print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one") 
#             return
#     for i in range(len(expected_samples)):
#         if abs(Your_samples[i] - expected_samples[i]) < 0.01:
#             continue
#         else:
#             print("Correlation Test case failed, your signal have different values from the expected one") 
#             return
#     print("Correlation Test case passed successfully")
import os
import numpy as np

def load_signals_from_folder(folder_path):
    """Loads all signals from text files in a given folder."""
    signals = []
    for file_name in sorted(os.listdir(folder_path)):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.txt'):
            with open(file_path, 'r') as f:
                signal = np.array([int(line.strip()) for line in f])
                signals.append(signal)
    return signals

def normalized_cross_correlation(signal1, signal2):
    """Computes the normalized cross-correlation between two signals."""
    mean1, mean2 = np.mean(signal1), np.mean(signal2)
    std1, std2 = np.std(signal1), np.std(signal2)
    norm_signal1 = (signal1 - mean1) / std1
    norm_signal2 = (signal2 - mean2) / std2
    return np.correlate(norm_signal1, norm_signal2, mode='valid')[0]

def classify_signal(test_signal, class_a_folder, class_b_folder):
    """Classifies the test signal based on template matching with signals in two folders."""
    # Load signals from Class A and Class B folders
    class_a_signals = load_signals_from_folder(class_a_folder)
    class_b_signals = load_signals_from_folder(class_b_folder)

    # Compute correlations for Class A
    corr_a = [normalized_cross_correlation(test_signal, sig) for sig in class_a_signals]
    avg_corr_a = np.mean(corr_a)

    # Compute correlations for Class B
    corr_b = [normalized_cross_correlation(test_signal, sig) for sig in class_b_signals]
    avg_corr_b = np.mean(corr_b)

    # Compare average correlations
    return 'Class 1 Down Movement of signal' if avg_corr_a > avg_corr_b else 'Class 2 Up Movement of signal'

# Example usage
def On_Classify_signal():
    # Paths to folders containing Class A and Class B signals
    class_a_folder = r"D:\AAA\Level 4\Semester 7\DSP\Assignments\Correlation\Correlation Task Files\point3 Files\Class 1"
    class_b_folder = r"D:\AAA\Level 4\Semester 7\DSP\Assignments\Correlation\Correlation Task Files\point3 Files\Class 2"

    # Path to Test signal
    test_file_path = r"D:\AAA\Level 4\Semester 7\DSP\Assignments\Correlation\Correlation Task Files\point3 Files\Test Signals\Test1.txt"
    test_file_path2= r"D:\AAA\Level 4\Semester 7\DSP\Assignments\Correlation\Correlation Task Files\point3 Files\Test Signals\Test2.txt"
    # Load Test signal
    with open(test_file_path, 'r') as f:
        test_signal1 = np.array([int(line.strip()) for line in f])
    with open(test_file_path2, 'r') as f:
        test_signal2 = np.array([int(line.strip()) for line in f])

    # Classify Test signal
    result1 = classify_signal(test_signal1, class_a_folder, class_b_folder)
    print(f"The Test_1 signal belongs to: {result1}")
    result2 = classify_signal(test_signal2, class_a_folder, class_b_folder)
    print(f"The Test_2 signal belongs to: {result2}")


