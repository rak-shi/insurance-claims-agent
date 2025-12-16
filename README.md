## Approach

This solution uses a hybrid architecture:
- LLM-based extraction (Groq LLaMA 3.1) for FNOL field parsing
- Deterministic rule-based validation and routing

The LLM is restricted to extraction only.
All business decisions remain rule-driven for explainability and safety.

## Demo Files
- manual_review_fnol.txt → Manual Review
- fasttrack_fnol.txt → Fast-track
- injury_fnol.txt → Specialist Queue
- investigation_fnol.txt → Investigation Flag

## Demo FNOL Files
- manual_review_fnol.txt → Missing fields → Manual Review
- fasttrack_fnol.txt → Damage < 25,000 → Fast-track
- injury_fnol.txt → Injury claim → Specialist Queue
- investigation_fnol.txt → Fraud keywords → Investigation Flag
