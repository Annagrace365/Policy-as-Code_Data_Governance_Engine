# Phase 5: Governance Enforcement Engine

## 1. Introduction

This phase implements the **Governance Enforcement Engine**, responsible for applying governance actions to sensitive data detected in user input.

The enforcement engine receives detected entities from the **PII detection module** and applies the appropriate actions defined in governance policies.

These actions include masking sensitive information, blocking restricted data, or replacing inappropriate language.

This phase ensures that sensitive content is **properly sanitized before being returned as system output**.

---

## 2. Responsibilities of the Module

The Enforcement Engine performs the following tasks:

* Receive detected sensitive entities from the detection module
* Identify the corresponding governance policy for each entity
* Apply the defined governance action
* Modify the input text according to enforcement rules
* Produce sanitized output text

This module ensures that all detected sensitive data is **processed according to governance policies**.

---

## 3. Enforcement Workflow

The enforcement engine processes detected entities using the following steps.

1. Receive the original input text
2. Receive detected sensitive entities
3. Identify the policy associated with each entity type
4. Determine the governance action defined in the policy
5. Apply masking, blocking, or replacement to detected values
6. Generate sanitized output text

This workflow ensures that governance actions are **applied consistently across all detected content**.

---

## 4. Governance Actions Implemented

The enforcement engine supports several types of actions.

### Mask

Sensitive data is partially hidden to protect user privacy.

Example:

Email:
[john@example.com](mailto:john@example.com) → jo*************

### Replace

Offensive or inappropriate words are replaced with neutral alternatives.

Example:

stupid → unwise

### Block

Highly sensitive data is completely removed or replaced with a placeholder.

Example:

Credit card number → [BLOCKED]

### Allow

Content that does not violate policies remains unchanged.

---

## 5. Core Enforcement Logic

The enforcement engine processes detected entities through the function:

`enforce(text, detected_items)`

### Parameters

| Parameter      | Description                                                 |
| -------------- | ----------------------------------------------------------- |
| text           | Original input text                                         |
| detected_items | List of sensitive entities detected by the detection module |

### Output

The function returns sanitized text after applying governance actions.

Example:

**Input**

Please contact me at [john@example.com](mailto:john@example.com) or call 9876543210.

**Output**

Please contact me at jo************* or call 98********.

---

## 6. Integration with Other Modules

| Module               | Purpose                                                 |
| -------------------- | ------------------------------------------------------- |
| Policy Loader        | Provides governance policy definitions                  |
| PII Detection Module | Supplies detected sensitive entities                    |
| Pipeline Runner      | Executes enforcement as part of the processing workflow |

This modular integration allows the enforcement engine to **operate independently while relying on external policy definitions**.

---

## 7. Advantages

* Centralized enforcement of governance policies
* Consistent handling of sensitive information
* Flexible action rules defined through policies
* Modular design enabling easy system expansion
* Protects user privacy by sanitizing sensitive data

---

## 8. Limitations

* String replacement may affect repeated patterns in complex text
* Masking logic is currently based on fixed visible characters
* Enforcement does not currently consider contextual meaning
* Overlapping detections may require additional handling

---


