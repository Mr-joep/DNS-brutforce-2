import csv
import string
import itertools

def generate_subdomains(domain, max_length):
    subdomains = []
    characters = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        for subset in itertools.product(characters, repeat=length):
            subdomain = ''.join(subset)
            subdomains.append(subdomain + '.' + domain)
    return subdomains

def save_subdomains_to_csv(subdomains, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subdomain"])
        for subdomain in subdomains:
            writer.writerow([subdomain])

def main():
    domain = input("Enter the domain: ")
    max_length = int(input("Enter the maximum length of subdomain: "))
    
    subdomains = generate_subdomains(domain, max_length)
    filename = "subdomains.csv"
    save_subdomains_to_csv(subdomains, filename)
    print(f"Generated subdomains are saved in '{filename}'.")

if __name__ == "__main__":
    main()
