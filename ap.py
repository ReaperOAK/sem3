def generate_ap(first_term, common_difference, num_terms):
    ap_terms = []
    for i in range(num_terms):
        term = first_term + i * common_difference
        ap_terms.append(term)
    return ap_terms

# Example usage
first_term = int(input("Enter the first term of the A.P.: "))
common_difference = int(input("Enter the common difference of the A.P.: "))
num_terms = int(input("Enter the number of terms in the A.P.: "))

ap_terms = generate_ap(first_term, common_difference, num_terms)
print("The terms of the A.P. are:", ap_terms)