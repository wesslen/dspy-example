# DSPy Translation Optimization - Artifact Reference Guide

## Artifact Pattern Definitions

**0 = No specific artifacts** (baseline banking queries)

**1 = Regional Banking Terminology**
- Canadian French specific terms: "guichet automatique" (ATM), "CELI" (TFSA), "SCHL" (CMHC)
- Spanish specific terms: "cajero automático" (ATM), "plazo fijo" (term deposit)
- Pattern to learn: Use region-appropriate banking vocabulary

**2 = Formality Register Maintenance**
- Spanish: "¿Puede usted...?" (formal "you"), "Pourriez-vous...?" (formal "could you")
- Banking context requires professional/formal register
- Pattern to learn: Maintain formal politeness appropriate for financial services

**3 = Account Type Terminology Patterns**
- "cuenta corriente" = checking account (not "cuenta de cheques")
- "depósito a término" = term deposit
- "compte conjoint" = joint account
- Pattern to learn: Consistent account type terminology across translations

**4 = False Friends and Common Errors**
- "solicitar" = to apply (not "solicit")
- "aplicación" = mobile app (not "application" which is "solicitud")
- "realizar" = to carry out (not "realize" which is "darse cuenta")
- Pattern to learn: Avoid false cognates that look similar but mean different things

**5 = Abbreviation/Acronym Handling**
- TFSA → "compte d'épargne libre d'impôt (CELI)" or just "CELI" in French Canadian
- CMHC → "SCHL" in French Canadian (Société canadienne d'hypothèques et de logement)
- PIN → "NIP" in French Canadian (Numéro d'identification personnel)
- RRSP → stays "REER" in French Canadian (Régime enregistré d'épargne-retraite)
- Pattern to learn: Rules for when to translate, transliterate, or maintain acronyms

**6 = Compound Financial Terms**
- "sobregiro" = overdraft (single concept, not word-by-word)
- "prélèvement automatique" = automatic withdrawal (semantic unit)
- "adelanto en efectivo" = cash advance
- "certificado de inversión garantizado" = guaranteed investment certificate
- Pattern to learn: Translate financial terms as semantic units, not literally

**7 = Temporal/Conditional Context Preservation**
- "que vence el 15 de marzo" = that matures on March 15
- "Si cancelo ahora..." = If I cancel now...
- "cuando estará disponible" = when will it be available
- "realizados este año" = made this year
- Pattern to learn: Preserve temporal and conditional relationships precisely

**8 = Negative Constructions and Politeness**
- "No puedo" → "I cannot" (not "I can't" - too informal)
- "Je n'ai pas reçu" → "I have not received" (formal negative)
- "Je n'ai jamais reçu" → "I never received"
- Pattern to learn: Use formal negatives, avoid contractions in banking context

**9 = Number and Currency Formatting**
- "$1.500,00" → "$1,500.00" (Spanish uses . for thousands, , for decimals)
- "$2.350,99" → "$2,350.99"
- Maintain currency symbols and adapt decimal conventions
- Pattern to learn: Correctly handle numeric and currency format conversions

**10 = Question Structure Types**
- Yes/no questions: "¿Puedo...?" → "Can I...?"
- Information questions: "¿Cuándo...?" → "When...?", "¿Cuánto...?" → "How much...?"
- Embedded questions: "decirme si..." → "tell me if..."
- Pattern to learn: Preserve interrogative intent and grammatical structure

## Dataset Statistics

### Trainset (40 examples)
Artifact distribution:
- 0 (no artifacts): 5 examples
- 1 (Regional terminology): 8 examples  
- 2 (Formality): 11 examples
- 3 (Account types): 7 examples
- 4 (False friends): 3 examples
- 5 (Abbreviations): 5 examples
- 6 (Compound terms): 4 examples
- 7 (Temporal/conditional): 4 examples
- 8 (Negatives/politeness): 6 examples
- 9 (Numbers/currency): 3 examples
- 10 (Question structures): 6 examples

Multiple artifacts per example: 15 examples

### Devset (30 examples)
Artifact distribution:
- 0 (no artifacts): 2 examples
- 1 (Regional terminology): 7 examples
- 2 (Formality): 7 examples
- 3 (Account types): 5 examples
- 4 (False friends): 2 examples
- 5 (Abbreviations): 7 examples
- 6 (Compound terms): 6 examples
- 7 (Temporal/conditional): 6 examples
- 8 (Negatives/politeness): 5 examples
- 9 (Numbers/currency): 4 examples
- 10 (Question structures): 9 examples

Multiple artifacts per example: 18 examples

## How DSPy Should Learn

### Via Instruction Optimization
DSPy should learn to add/refine instructions like:
- "Use Canadian French banking terminology (CELI for TFSA, SCHL for CMHC, NIP for PIN)"
- "Maintain formal register appropriate for banking (use 'puede usted', 'pourriez-vous')"
- "Translate financial compounds as semantic units, not word-by-word"
- "Avoid false cognates: 'aplicación'=app, 'solicitud'=application form"
- "Use formal negatives without contractions in professional contexts"
- "Preserve temporal and conditional relationships precisely"

### Via Few-Shot Example Selection
DSPy should learn to select examples demonstrating:
- Regional terminology variants when new financial terms appear
- Formality patterns when politeness is crucial
- Compound term handling when complex financial concepts arise
- Number formatting when amounts/dates are present
- Question structure preservation for various interrogative types

## Testing Strategy

1. **Train DSPy** on trainset with initial generic prompt
2. **Optimize** using trainset (let DSPy refine instructions or select examples)
3. **Evaluate** on devset - check performance by artifact type
4. **Analyze** which artifacts were learned vs. which need more training data
5. **Iterate** based on per-artifact performance metrics