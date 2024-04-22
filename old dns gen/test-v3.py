import csv
import string
import itertools

def count_subdomains(domain, max_length):
    count = 0
    characters = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        count += len(characters) ** length
    return count

def generate_subdomains(domain, max_length):
    characters = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        for subset in itertools.product(characters, repeat=length):
            subdomain = ''.join(subset)
            yield subdomain + '.' + domain

def save_subdomains_to_csv(subdomains, filename, chunk_size=1000):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subdomain"])
        chunk = []
        for subdomain in subdomains:
            chunk.append([subdomain])
            if len(chunk) == chunk_size:
                writer.writerows(chunk)
                chunk = []
        if chunk:
            writer.writerows(chunk)

def main():
    domain = input("Enter the domain: ")
    max_length = int(input("Enter the maximum length of subdomain: "))
    
    total_subdomains = count_subdomains(domain, max_length)
    print(f"Total number of subdomains to be generated: {total_subdomains}")
    
    subdomains = generate_subdomains(domain, max_length)
    filename = "subdomains3.csv"
    save_subdomains_to_csv(subdomains, filename)
    print(f"Generated subdomains are saved in '{filename}'.")

if __name__ == "__main__":
    main()
