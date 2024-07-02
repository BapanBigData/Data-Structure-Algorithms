def extract_string_at_given_key(string, key):
    return string.split(' ')[key - 1]

def sort_strings(strings_keys_mp: list, reversal: str, ordering: str) -> None:
    # Sorting
    strings_keys_mp.sort(key=lambda x: int(x[1]) if ordering == "numeric" else x[1])

    # Reversal
    if reversal == "true":
        strings_keys_mp.reverse()

    # Output
    for pair in strings_keys_mp:
        print(pair[0])
    
    return


if __name__ == "__main__":
    n = int(input("Enter input size:"))

    input_list = []
    for i in range(n):
        temp = input("Enter the string:")
        input_list.append(temp)

    key, reversal, ordering = input("Enter key reversal ordering:").split()

    ## To extract keys for comparison & store them
    vp = [(s, extract_string_at_given_key(s, int(key))) for s in input_list]
    print(vp)
    
    ## print the output
    sort_strings(vp, reversal, ordering)