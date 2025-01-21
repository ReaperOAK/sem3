def generate_gp(first_term, common_ratio, num_terms):
    gp_terms = []
    for i in range(num_terms):
        term = first_term * (common_ratio ** i)
        gp_terms.append(term)
    return gp_terms

# Example usage
first_term = float(input("Enter the first term of the G.P.: "))
common_ratio = float(input("Enter the common ratio of the G.P.: "))
num_terms = int(input("Enter the number of terms in the G.P.: "))

gp_terms = generate_gp(first_term, common_ratio, num_terms)
print("The terms of the G.P. are:", gp_terms)