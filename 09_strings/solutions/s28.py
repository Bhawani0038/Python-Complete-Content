pan = input("Enter a valid-format PAN: ").strip().upper()
valid = (
    len(pan) == 10
    and pan[:5].isalpha()
    and pan[5:9].isdigit()
    and pan[9].isalpha()
)

categories = {
    "P": "individual",
    "C": "company",
    "H": "Hindu Undivided Family",
    "F": "firm or partnership",
    "A": "association of persons",
    "T": "trust",
    "B": "body of individuals",
    "L": "local authority",
    "J": "artificial juridical person",
    "G": "government",
}

if valid:
    print(categories.get(pan[3], "Unknown category"))
else:
    print("Invalid PAN format")
