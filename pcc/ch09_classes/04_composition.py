# ============================================================
# Ch09 - 04 Composition
# Knowledge Notes
# ============================================================


# ------------------------------------------------------------
# 1. Inheritance = "is-a"
# ------------------------------------------------------------

# class MLCandidate(Candidate):
#     ...
#
# MLCandidate IS A Candidate.
#
# This relationship makes sense:
#
# MLCandidate
#     ↓
# Candidate


# ------------------------------------------------------------
# 2. Composition = "has-a"
# ------------------------------------------------------------

# Sometimes one object is NOT a special type of another object.
# Instead, one object CONTAINS / USES another object.
#
# Example:
#
# Candidate HAS A ContactInfo.
#
# A Candidate is NOT a ContactInfo.
#
# Therefore inheritance would not make sense.


class ContactInfo:

    def __init__(self, email, city):
        self.email = email
        self.city = city


class Candidate:

    def __init__(self, name, email, city):
        self.name = name

        self.contact = ContactInfo(email, city)


# candidate.contact is another object.
#
# alex = Candidate(
#     "Alex",
#     "alex@example.com",
#     "Detroit",
# )
#
# print(alex.name)
# print(alex.contact.email)
# print(alex.contact.city)


# Mental model:
#
# Candidate object
# │
# ├── name = "Alex"
# │
# └── contact
#       ↓
#       ContactInfo object
#       ├── email
#       └── city


# ------------------------------------------------------------
# 3. Composition means objects can contain other objects
# ------------------------------------------------------------

# self.contact = ContactInfo(...)
#
# self.contact is an ATTRIBUTE,
# but its value happens to be another class instance.


# Therefore:
#
# alex.contact
#
# → ContactInfo object
#
#
# alex.contact.email
#
# → first get alex.contact
# → then access that object's email attribute


# ------------------------------------------------------------
# 4. Why not inheritance?
# ------------------------------------------------------------

# Wrong idea:
#
# class Candidate(ContactInfo):
#
# This would mean:
#
# Candidate IS A ContactInfo
#
# which does not describe the real relationship.


# Better:
#
# Candidate HAS A ContactInfo
#
# → composition


# ------------------------------------------------------------
# 5. Composition is extremely common in real programs
# ------------------------------------------------------------

# An object may use many other objects:
#
# Car HAS AN Engine
# Order HAS Customer information
# Model HAS Layers
# Candidate HAS ContactInfo


# ------------------------------------------------------------
# 6. Very important PyTorch example
# ------------------------------------------------------------

# class CNNPlanner(nn.Module):
#
#     def __init__(self):
#         super().__init__()
#
#         self.conv1 = nn.Conv2d(...)
#         self.relu = nn.ReLU()
#         self.fc = nn.Linear(...)
#
#
# CNNPlanner IS AN nn.Module
# → inheritance
#
#
# CNNPlanner HAS A Conv2d layer
# CNNPlanner HAS A ReLU layer
# CNNPlanner HAS A Linear layer
# → composition


# So one class can use BOTH:
#
# inheritance
# +
# composition


# ------------------------------------------------------------
# 7. Main decision rule
# ------------------------------------------------------------

# Ask:
#
# "Is this object a specialized type of the other object?"
#
# YES:
# → inheritance may make sense
#
#
# "Does this object simply contain/use another object?"
#
# YES:
# → composition may make more sense


# ------------------------------------------------------------
# 8. Mental model
# ------------------------------------------------------------

# Inheritance:
#
# MLCandidate IS A Candidate
#
# class MLCandidate(Candidate)


# Composition:
#
# Candidate HAS A ContactInfo
#
# self.contact = ContactInfo(...)


alex = Candidate(
    "Alex",
    "alex@example.com",
    "Detroit",
)

print(alex.name)
print(alex.contact.email)
print(alex.contact.city)