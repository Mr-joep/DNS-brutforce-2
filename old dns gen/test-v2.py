import csv
import string
import itertools

def generate_subdomains(domain, max_length):
    characters = string.ascii_lowercase + string.digits
    subdomains = []
    for length in range(1, max_length + 1):
        for subset in itertools.product(characters, repeat=length):
            subdomains.append(''.join(subset) + '.' + domain)
    return subdomains

def save_subdomains_to_csv(subdomains, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subdomain"])
        writer.writerows([[subdomain] for subdomain in subdomains])

def main():
    domain = input("Enter the domain: ")
    max_length = int(input("Enter the maximum length of subdomain: "))
    
    subdomains = generate_subdomains(domain, max_length)
    filename = "subdomains.csv"
    save_subdomains_to_csv(subdomains, filename)
    print(f"Generated subdomains are saved in '{filename}'.")

if __name__ == "__main__":
    main()
