# Attack Scenarios



## Scenario 1: Broken Object-Level Authorization



An authenticated user modifies an API request by changing a customer identifier.



### Attack Path



1. Attacker logs into a valid account.

2. Attacker intercepts an API request.

3. Attacker changes `customer_id` or object reference.

4. API returns another customer's data because object-level authorization is missing.



### Impact



- Customer data exposure

- Privacy violation

- Regulatory and reputational risk



### Recommended Controls



- Enforce object-level authorization on every request

- Use deny-by-default access checks

- Add automated authorization test cases

- Log authorization failures



---



## Scenario 2: CI/CD Secret Exposure



A developer accidentally commits a cloud access key into the repository.



### Attack Path



1. Secret is committed to GitHub.

2. Attacker discovers the exposed secret.

3. Attacker uses the secret to access cloud resources.

4. Attacker modifies infrastructure or extracts data.



### Impact



- Cloud account compromise

- Unauthorized deployment changes

- Data exposure



### Recommended Controls



- Secret scanning

- Pre-commit hooks

- Secret vaulting

- Immediate secret rotation

- Least privilege IAM



---



## Scenario 3: Public Object Storage Exposure



A storage bucket is configured for public access.



### Attack Path



1. Uploaded customer files are stored in object storage.

2. Bucket or container policy allows public read access.

3. Attacker accesses files without authentication.



### Impact



- Sensitive document exposure

- Compliance risk

- Customer trust impact



### Recommended Controls



- Private bucket policies

- Block public access

- Encryption at rest

- Storage access logging

- Cloud security posture checks



