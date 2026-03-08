# Phase 2: Policy & Governance Rule Definition

## 1. Introduction

This document describes the governance policies designed for detecting and processing sensitive and inappropriate content within user-provided text.

The system focuses on detecting and handling the following types of content:

- Personally Identifiable Information (PII)
- Financial identifiers
- Structured address data
- Offensive and abusive language

The policies are **configuration-driven** and defined externally to ensure flexibility, scalability, and maintainability. Governance rules are stored in **YAML policy files**, allowing the system to load and apply rules dynamically without modifying application code.

---

## 2. Policy Design Basis

The governance rules are created based on three core principles.

### 2.1 Privacy Protection

Sensitive personal and financial data must not be exposed in system output.

### 2.2 Content Moderation

Inappropriate or abusive expressions should be neutralized to maintain respectful communication.

### 2.3 Configurable Governance

Rules must be editable without modifying core application logic. Using **YAML-based policy configuration**, administrators can update or extend rules easily.

---

## 3. Detection Methods Used

The system supports three detection methods.

### 3.1 Regex-Based Detection

Regex-based detection is used for structured data with predictable formats.

**Applied To**

- Email
- Phone Number
- ID / Card Number
- Address

**Reason**

These data types follow defined patterns that can be reliably identified using regular expressions.

---

### 3.2 Keyword-Based Detection

Keyword-based detection is used for content moderation where detection depends on predefined vocabulary.

**Applied To**

- Offensive Words
- Abusive Language

**Reason**

Such content is best controlled using predefined keyword lists that can be expanded over time.

---

### 3.3 None Detection

Used for normal text.

**Purpose**

Ensures regular content passes through the system without modification.

---

## 4. Policy Rules Explanation

### 4.1 Email Detection

The pattern identifies the standard email structure:

- Username  
- `@` symbol  
- Domain  
- Top-level domain  

**Action:** Partial Masking

**Reason:** Protect user identity while retaining minimal readability.

---

### 4.2 Phone Number Detection

The pattern detects:

- 10-digit numbers  
- Optional `+91` country code  
- Valid starting digits  

**Action:** Partial Masking

**Reason:** Phone numbers are directly linked to individuals.

---

### 4.3 ID / Card Number Detection

The pattern detects:

- 16-digit structured numbers  
- Numbers with spaces or hyphens  

**Action:** Block

**Reason:** Financial identifiers are highly sensitive and should be fully removed.

---

### 4.4 Address Detection

The pattern detects:

- House or building number  
- Street name  
- Location suffix (Road, Street, Avenue, etc.)

**Action:** Full Masking

**Reason:** Addresses reveal physical locations and are considered personal data.

---

### 4.5 Offensive Word Detection

Detected using a predefined keyword list.

**Action:** Replace with neutral alternatives.

| Original Word | Replacement |
|---------------|-------------|
| stupid | unwise |
| dumb | uninformed |
| fool | misguided |

**Purpose**

Maintain respectful tone without deleting content entirely.

---

### 4.6 Abusive Language Detection

Detected using a predefined keyword list.

**Action:** Replace with softer expressions.

| Original Word | Replacement |
|---------------|-------------|
| idiot | person |
| moron | individual |
| jerk | rude person |

**Purpose**

Reduce harmful language while preserving sentence structure.

---

### 4.7 Normal Text

Detection Type: None  
Action: Allow

**Purpose**

Ensure safe content remains unchanged.

---

## 5. Governance Actions Defined

| Action | Description |
|------|-------------|
| Mask (Partial) | Hide part of sensitive data |
| Mask (Full) | Hide entire sensitive content |
| Block | Completely remove restricted data |
| Replace | Substitute with neutral equivalent |
| Allow | Leave content unchanged |

---

## 6. Advantages

- Configuration-driven design
- Easy to expand rule list
- Lightweight and fast execution
- Deterministic and explainable behavior
- Policies stored in external **YAML files**
- Privacy-focused enforcement

---

## 7. Limitations

- Regex may miss irregular or obfuscated formats
- Keyword-based detection lacks contextual understanding
- Possible false positives in numeric or address detection
- Does not validate financial data authenticity
- Limited semantic intelligence