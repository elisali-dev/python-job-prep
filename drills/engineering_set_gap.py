# ======= Exercise 1 — Unique capabilities =========
capabilities = [
    "python",
    "sql",
    "python",
    "pytorch",
    "sql",
    "docker",
]

unique_capabilities = set(capabilities)
print(unique_capabilities)
print(f"Chaning it to set to get unique capabilities and the lenght/uniqiue capabilities quantity is {len(unique_capabilities)}")
print(f"Original capabilities list length is {len(capabilities)}")

# ====== Exercise 2 - Capability Matching =====
model_capabilities = {
    "python",
    "sql",
    "pytorch",
    "gpu",
}

required_capabilities = {
    "python",
    "sql",
    "pytorch",
    "docker",
    "aws",
}

matched_capabilities = model_capabilities & required_capabilities
missing_capabilities = required_capabilities - model_capabilities
print(f"Matched capabilities: {matched_capabilities}")
print(f"Missing capabilities: {missing_capabilities}")

#======== Exercise 3 — Extra capabilities ===========

extra_capabilities = model_capabilities - required_capabilities

print(f"Extra capabilities: {extra_capabilities}")

#======== Exercise 4 — All Known Capabilities ===========
all_capabilities = model_capabilities | required_capabilities
print(f"All known capabilities: {all_capabilities}")

# =========== Exercise 5 — Membership ============== 
if "python" in model_capabilities:
    print("Python capability available.")
else:
    print("Python capability missing.")

# ======== Challenge ==============
model_capabilities = [
    " Python ",
    "SQL",
    "python",
    "PyTorch",
    "Docker",
]
capabilities = []
for capability in model_capabilities:
    capability = capability.strip().lower()
    capabilities.append(capability)
print(set(capabilities))