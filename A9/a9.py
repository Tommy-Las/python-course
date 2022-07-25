import csv


def make_set(training_file_name):
    input_set_list = []
    input_file = open(training_file_name, 'r')
    next(input_file)
    input_reader = csv.reader(input_file)

    for line in input_reader:
        line = (float(x) for x in line)

        input_set_list.append(tuple(line))

    return input_set_list


def sum_lists(list1, list2):
    sum_list = []
    for i in range(8):
        sum_list.append(list1[i] + list2[i])
    return sum_list


def make_averages(sum_list, total):
    averages_list = []
    for value in sum_list:
        averages_list.append(value/total)
    return averages_list


def train_classifier(training_set_list):
    benign_list = [0]*8
    benign_count = 0
    malignant_list = [0]*8
    malignant_count = 0

    for patient_tuple in training_set_list:
        if patient_tuple[8] == 0:
            benign_list = sum_lists(benign_list, patient_tuple[:8])
            benign_count += 1
        else:  # == 1
            malignant_list = sum_lists(malignant_list, patient_tuple[:8])
            malignant_count += 1

    benign_averages_list = make_averages(benign_list, benign_count)
    malignant_averages_list = make_averages(malignant_list, malignant_count)

    classifier_list = make_averages(
        sum_lists(benign_averages_list, malignant_averages_list), 2)

    return classifier_list


def classify_test_set_list(test_set_list, classifier_list):
    result_list = []

    for patient_tuple in test_set_list:
        benign_count = 0
        malignant_count = 0

        for i in range(8):
            if patient_tuple[i] > classifier_list[i]:
                malignant_count += 1
            else:  # patient_tuple[i] < classifier_list[i]
                benign_count += 1

        diagnosis = patient_tuple[8]

        result_tuple = (benign_count, malignant_count, diagnosis)
        result_list.append(result_tuple)

    return result_list


def report_results(result_list):
    total_count = 0
    innacurate_count = 0
    for result_tuple in result_list:
        total_count += 1
        benign_count, malignant_count, diagnosis = result_tuple[0:]
        if (benign_count > malignant_count) and diagnosis == 1:
            innacurate_count += 1
        elif (benign_count < malignant_count) and diagnosis == 0:
            innacurate_count += 1

    print(
        f"\nOf {total_count} patients, there were {innacurate_count} inaccuracies")
    accuracy = ((total_count - innacurate_count) / total_count) * 100
    print(f"Accuracy of %{accuracy:.2f}")
    print("Reported the results")


def main():
    file_name = "diabetes.csv"
    training_set_list = make_set(file_name)

    classifier_list = train_classifier(training_set_list)

    result_list = classify_test_set_list(training_set_list, classifier_list)

    report_results(result_list)

    print("\nProgram Finished")


main()
