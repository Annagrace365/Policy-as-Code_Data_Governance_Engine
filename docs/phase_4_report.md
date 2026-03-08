# Phase 4: PII Detection Module Implementation

## 1. Introduction

This phase implements the **PII Detection Module** of the Content Governance Engine.  
The purpose of this module is to identify sensitive information present in user-provided text.

The detection process uses **governance policies defined in policy files**, which specify patterns and keywords used to identify sensitive data elements. Once detected, the identified entities are forwarded to the governance engine for further processing such as masking, blocking, or replacement.

---

## 2. Responsibilities of the Module

The PII Detection module performs the following tasks:

- Accept input text from the processing pipeline  
- Retrieve governance rules loaded from policy files  
- Apply detection logic based on rule types  
- Identify occurrences of sensitive data  
- Return detected entities for governance enforcement  

---

## 3. Detection Workflow

The PII detection process follows these steps:

1. Input text is received from the pipeline  
2. Governance policies are loaded from the policy configuration files  
3. Each rule is evaluated based on its detection type  
4. Detection methods such as regex matching or keyword matching are applied  
5. Matching entities are recorded along with their types  
6. The list of detected entities is returned to the pipeline  

---

## 4. Detection Methods Implemented

The detection module supports two types of detection mechanisms.

### Regex-Based Detection

Regex matching is used to detect structured data patterns such as:

- Email addresses  
- Phone numbers  
- Identification numbers  
- Address patterns  

The module scans the input text using predefined regular expressions defined in the policy files.

### Keyword-Based Detection

Keyword-based detection is used to identify offensive or abusive language.

The module checks the input text for predefined keywords and records any matches.

---

## 5. Core Function Implementation

The primary function implemented in this module performs the PII detection process.
detect_pii(text, policies)


### Parameters

| Parameter | Description |
|-----------|-------------|
| text | Input text provided by the user |
| policies | Governance policy rules loaded from policy files |

### Output

The function returns a structured list containing detected entities.

Example:
[
{"type": "email", "value": "john@example.com
"},
{"type": "phone", "value": "9876543210"}
]

---

## 6. Example Detection

**Input Text**
Please contact me at john@example.com or call 9876543210.

**Detected Entities**

| Detected Value | Type |
|---------------|------|
| john@example.com | Email |
| 9876543210 | Phone Number |

These detected entities are then passed to the **governance engine** for applying the corresponding actions defined in the policy files.

---

## 7. Integration with Other Modules

| Module | Purpose |
|-------|---------|
| Policy Loader | Loads governance rules from policy files |
| Governance Engine | Applies masking, blocking, or replacement actions |
| Pipeline Runner | Executes the complete system workflow |

This modular design ensures that detection logic remains separate from governance enforcement.

---

## 8. Advantages

- Modular implementation  
- Easy integration with policy-driven governance rules  
- Lightweight detection mechanism  
- Simple and efficient pattern matching  

---

## 9. Limitations

- Regex detection may miss irregular or obfuscated data formats  
- Keyword detection lacks contextual understanding  
- Numeric patterns may occasionally produce false positives  