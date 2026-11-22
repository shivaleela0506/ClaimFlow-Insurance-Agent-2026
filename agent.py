print("=" * 50)
print("CLAIMFLOW - Insurance Claims Processing Agent")
print("=" * 50)

claims = {}

while True:

    print("\n----- MENU -----")
    print("1. File New Claim")
    print("2. Check Claim Status")
    print("3. Claim Amount Estimator")
    print("4. Verify Documents")
    print("5. Insurance FAQ")
    print("6. View All Claims")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        claim_id = input("Enter Claim ID: ")
        customer = input("Enter Customer Name: ")
        claim_type = input("Enter Claim Type (Health/Vehicle/Home): ")

        claims[claim_id] = {
            "customer": customer,
            "type": claim_type,
            "status": "Under Review"
        }

        print("✅ Claim Registered Successfully")

    elif choice == "2":

        cid = input("Enter Claim ID: ")

        if cid in claims:
            print("Status:", claims[cid]["status"])
        else:
            print("❌ Claim Not Found")

    elif choice == "3":

        bill = float(input("Enter Total Damage/Bill Amount: "))

        estimated = bill * 0.80

        print("Estimated Insurance Settlement =", estimated)

    elif choice == "4":

        docs = input(
            "Have you submitted ID Proof, Policy Copy and Bills? (yes/no): ")

        if docs.lower() == "yes":
            print("✅ Documents Verified")
        else:
            print("⚠ Missing Documents Detected")

    elif choice == "5":

        print("\nInsurance FAQ")
        print("Q: How long does approval take?")
        print("A: Typically 3-7 working days.")

        print("\nQ: Required documents?")
        print("A: Policy Copy, ID Proof, Bills.")

    elif choice == "6":

        if len(claims) == 0:
            print("No Claims Found")

        else:
            print("\nRegistered Claims")

            for cid, data in claims.items():
                print(
                    f"Claim ID: {cid}, Customer: {data['customer']}, Type: {data['type']}, Status: {data['status']}"
                )

    elif choice == "7":

        print("Thank you for using ClaimFlow.")
        break

    else:
        print("Invalid Choice")
print("CLAIMFLOW - Insurance Claims Processing Agent")
print("=" * 50)

claims = {}

while True:

    print("\n----- MENU -----")
    print("1. File New Claim")
    print("2. Check Claim Status")
    print("3. Claim Amount Estimator")
    print("4. Verify Documents")
    print("5. Insurance FAQ")
    print("6. View All Claims")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        claim_id = input("Enter Claim ID: ")
        customer = input("Enter Customer Name: ")
        claim_type = input("Enter Claim Type (Health/Vehicle/Home): ")

        claims[claim_id] = {
            "customer": customer,
            "type": claim_type,
            "status": "Under Review"
        }

        print("✅ Claim Registered Successfully")

    elif choice == "2":

        cid = input("Enter Claim ID: ")

        if cid in claims:
            print("Status:", claims[cid]["status"])
        else:
            print("❌ Claim Not Found")

    elif choice == "3":

        bill = float(input("Enter Total Damage/Bill Amount: "))

        estimated = bill * 0.80

        print("Estimated Insurance Settlement =", estimated)

    elif choice == "4":

        docs = input(
            "Have you submitted ID Proof, Policy Copy and Bills? (yes/no): ")

        if docs.lower() == "yes":
            print("✅ Documents Verified")
        else:
            print("⚠ Missing Documents Detected")

    elif choice == "5":

        print("\nInsurance FAQ")
        print("Q: How long does approval take?")
        print("A: Typically 3-7 working days.")

        print("\nQ: Required documents?")
        print("A: Policy Copy, ID Proof, Bills.")

    elif choice == "6":

        if len(claims) == 0:
            print("No Claims Found")

        else:
            print("\nRegistered Claims")

            for cid, data in claims.items():
                print(
                    f"Claim ID: {cid}, Customer: {data['customer']}, Type: {data['type']}, Status: {data['status']}"
                )

    elif choice == "7":

        print("Thank you for using ClaimFlow.")
        break

    else:
        print("Invalid Choice")