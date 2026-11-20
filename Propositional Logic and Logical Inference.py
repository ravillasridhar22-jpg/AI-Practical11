
# Practical 11: Propositional Logic and Logical Inference

print("====================================")
print("  AI MEDICAL EXPERT SYSTEM")
print("  Using Propositional Logic")
print("====================================")

# Get facts from user
fever = input("Do you have fever? (yes/no): ").lower() == "yes"

cough = input("Do you have cough? (yes/no): ").lower() == "yes"

headache = input("Do you have headache? (yes/no): ").lower() == "yes"

sneezing = input("Do you have sneezing? (yes/no): ").lower() == "yes"

# Store facts
facts = {
    "Fever": fever,
    "Cough": cough,
    "Headache": headache,
    "Sneezing": sneezing
}

print("\n--- Known Facts ---")

for fact in facts:
    print(fact, ":", facts[fact])

print("\n--- Logical Inference ---")

# Rule 1: Fever AND Cough
if fever and cough:
    print("Rule 1: Fever AND Cough")
    print("Conclusion: Flu-like symptoms detected.")

# Rule 2: Sneezing AND Cough
if sneezing and cough:
    print("Rule 2: Sneezing AND Cough")
    print("Conclusion: Possible respiratory irritation.")

# Rule 3: Fever AND Headache
if fever and headache:
    print("Rule 3: Fever AND Headache")
    print("Conclusion: Symptoms require medical attention.")

# Rule 4: No symptoms
if not fever and not cough and not headache and not sneezing:
    print("Conclusion: No symptoms reported.")

# Final result
if fever or cough or headache or sneezing:
    print("\nInference completed successfully.")

print("\nThank you for using the AI Expert System!")
