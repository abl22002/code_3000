# Homework 5

## 1. Intended User(s)

The intended users of this repository are:
- **Myself** - Ariana Lapaix
- **Course instructors**


## 2. Assessment of Security Threats

If this code or data fell into the wrong hands, the following security concerns exist:

- **Bot detection**: The gradient boosting classifier in mod02_build_bot_predictor.py could potentially be engineered to help automated bots evade detection systems.
- **Data Leaks**: The datasets used within each assignment could expose imformation that can be used to deanonymize users.

## 3. Security Steps 


- **CODEOWNERS file**: Configured with @batmandoescale to ensure that all code changes require approval from an authorized owner, preventing unauthorized modifications to the main branch.

- **Private repository**: Given the sensitive nature of the code, this repository should be private to limit access to authorized users only.

- **Reasons Why Not Completely Necessary**: Overall the code being used is not sensitive and is not intended to be used for any malicious purposes. Since this is a course repository, the information being used may not be sensitive enough to warrant a private repository.

